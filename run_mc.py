import appgopmc_dose as gopmc
import mc_setting as mc
import numpy as np
import os 
from scipy.io import savemat
import matplotlib.pyplot as plt
import napari
import time

pmc = gopmc.appgopmc_dose()

def change_dir():
    cwd = os.getcwd()
    current_file_path = os.path.dirname(os.path.abspath(__file__))
    if cwd != current_file_path:
        os.chdir(current_file_path)
    return current_file_path

def Water(E):
    current_file_path = change_dir()
    geo = mc.geometry(current_file_path)
    Nx = 51
    Ny = 51
    Nz = 360
    dx = 0.1
    dy = 0.1
    dz = 0.1
    energy = E # MeV
    spot_size = [0,0]# beam spot size (cm), sqare beam shape
    num_particle = 1e6# integer, num of particles
    geo.set_header(Nx,Ny,Nz,dx,dy,dz)
    geo.set_cfg(energy,spot_size,num_particle)
    
    geo.create_cfg_file('pencilbeam.cfg')
    geo.create_header_file()
    # .transpose(2, 1, 0) is required for matlab
    image = np.array(np.zeros((geo.Nx,geo.Ny,geo.Nz)),dtype=np.short).transpose(2, 1, 0).flatten()
    mc.write_image(image,current_file_path + '\\Phantom\\')
    start = time.time()
    dose = pmc.run(geo.cfg_file,image)
    print("Total time = ",time.time() - start)
    totalDose = np.array(dose).reshape((geo.Nz,geo.Nx,geo.Ny)).transpose(2, 1, 0)
    savemat(geo.outputdir+'waterDose'+str(E)+'.mat',{'totalDose':totalDose, 'dx':geo.dx, 'dy':geo.dy, 'dz':geo.dz})
def MLSIC():
    current_file_path = change_dir()
    geo = mc.geometry(current_file_path)
    E = 200 # MeV
    x = 0 # unit cm
    y = 0 # unit cm
    s = mc.scene()
    # x_ROI = None
    # y_ROI = None
    x_ROI = [160,361] # idx 0~511
    y_ROI = [160,361] # idx 0~511
    # x_ROI = 255 + np.array([-50,50],dtype=np.int32)
    # y_ROI = 255 + np.array([-50,50],dtype=np.int32)
    s.create_simple_scene(E,x_ROI,y_ROI)
    geo.set_header_from_scene(s)
    geo.set_cfg_for_MLSIC(x,y)
    geo.create_cfg_file('pencilbeam.cfg')
    geo.create_header_file()
    image = np.array(s.image,dtype=np.short).transpose(2, 1, 0).flatten()
    mc.write_image(image,current_file_path + '\\Phantom\\')
    start = time.time()
    dose = pmc.run(geo.cfg_file,image)
    print("Total time = ",time.time() - start)
    totalDose = np.array(dose).reshape((geo.Nz,geo.Nx,geo.Ny)).transpose(2, 1, 0)
    savemat(geo.outputdir +"MLSICdose.mat", {'totalDose':totalDose, 'RangeShifter':s.RangeShifter_idx, 'Phantom':s.phantom_idx, 'MLSIC':s.MLSIC_idx })
    savemat(geo.outputdir +"MLSICscene.mat", {'scene':s.image, 'RangeShifter':s.RangeShifter_idx, 'Phantom':s.phantom_idx, 'MLSIC':s.MLSIC_idx })
    # viewer = napari.view_image(totalDose, rgb=False)
    # napari.run()  # start the event loop and show viewer
def call_exe():
    current_file_path = change_dir()
    geo = mc.geometry(current_file_path)
    E = 230 # MeV
    x = 0 # unit cm
    y = 0 # unit cm
    s = mc.scene()
    # x_ROI = None
    # y_ROI = None
    x_ROI = [160,361] # idx 0~511
    y_ROI = [160,361] # idx 0~511
    # x_ROI = 255 + np.array([-50,50],dtype=np.int32)
    # y_ROI = 255 + np.array([-50,50],dtype=np.int32)
    s.create_simple_scene(E,x_ROI,y_ROI)
    geo.set_header_from_scene(s)
    geo.set_cfg_for_MLSIC(x,y)
    geo.create_cfg_file('pencilbeam.cfg')
    geo.create_header_file()
    image = np.array(s.image,dtype=np.short).transpose(2, 1, 0).flatten()
    mc.write_image(image,current_file_path + '\\Phantom\\')
    start = time.time()
    os.system('appgopmc_dose.exe --config ./Phantom/pencilbeam.cfg')
    print("Total time = ",time.time() - start)
if __name__ == '__main__':
    # MLSIC()
    # for e in range(25,181):
    #     Water(e)
    Water(110)
    # call_exe()