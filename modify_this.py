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
current_file_path = change_dir()
geo = mc.geometry(current_file_path)

name2 = 'CT.1.3.12.2.1107.5.1.7.130094.30000022051213533424400000'# 214->348
path2 = 'C:/Users/shuangzhou/Downloads/Head_Phantom/head2/'
idx2 = np.arange(214,348)
head,dxyz = mc.read_3d_head_phantom(path2,name2,idx2)
# save it for later use or don't save
# np.savez('./Phantom/head.npz', head=head, dxyz=dxyz)

#transpose(2, 1, 0) is required for matlab
image = np.array(head,dtype=np.short).transpose(2, 1, 0).flatten()
header_name = 'geo_phantom'
mc.write_image(image,current_file_path + '\\Phantom\\',header_name+'.img')

Nx = 51
Ny = 51
Nz = 360
dx = 0.1#cm
dy = 0.1
dz = 0.1
E = 110.0
energy = E # MeV
spot_size = [0,0]# beam spot size (cm), sqare beam shape
num_particle = 1e6# integer, num of particles
geo.set_header(Nx,Ny,Nz,dx,dy,dz)# see comments
geo.set_cfg(energy,spot_size,num_particle)# see comments
geo.create_cfg_file('pencilbeam.cfg')
geo.create_header_file(header_name + '.header')

start = time.time()
dose = pmc.run(geo.cfg_file,image)
print("Total time = ",time.time() - start)
totalDose = np.array(dose).reshape((geo.Nz,geo.Nx,geo.Ny)).transpose(2, 1, 0)

viewer = napari.view_image(totalDose, rgb=False)
napari.run()  # start the event loop and show viewer

matData_filename = 'waterDose'+str(E)
savemat(geo.outputdir+matData_filename+'.mat',{'totalDose':totalDose, 'dx':geo.dx, 'dy':geo.dy, 'dz':geo.dz})