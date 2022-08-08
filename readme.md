




minimum example:
- conda activate base
- pip install -r requirements.txt
- python run_mc.py
- it will call Water(110), calculate 110MeV no size proton beam in water phantom. results save in ./output/totalDose.img, you can read it in matlab
    ```matlab
        fileID = fopen([path,'/output/totalDose.img'],'r');
        temp = fread(fileID,'float');
        dose = reshape(temp,51,51,360);
    ```
- in water example, it may take 1min at low energy, but it becomes fast when the energy is high, 7 sec at 180MeV
- Things you can modify in Water(E) function:
    ``` python
    Nx = 51
    Ny = 51
    Nz = 360
    dx = 0.1#cm
    dy = 0.1
    dz = 0.1
    energy = E # MeV
    spot_size = [0,0]# beam spot size (cm), sqare beam shape
    num_particle = 1e6# integer, num of particles
    geo.set_header(Nx,Ny,Nz,dx,dy,dz)# see comments
    geo.set_cfg(energy,spot_size,num_particle)# see comments
    ```

How to load CT images:
- import lib
    ```python
    import appgopmc_dose as gopmc
    import mc_setting as mc
    import numpy as np
    import os 
    from scipy.io import savemat
    import matplotlib.pyplot as plt
    import napari
    import time
    ```
- prepare MC engine
    ```python
    pmc = gopmc.appgopmc_dose()
    def change_dir():
        cwd = os.getcwd()
        current_file_path = os.path.dirname(os.path.abspath(__file__))
        if cwd != current_file_path:
            os.chdir(current_file_path)
        return current_file_path
    current_file_path = change_dir()
    geo = mc.geometry(current_file_path)
    ```
- read dicom files with read_dicom.py, costumize your own path, filename and index. Then convert dicom files to a single 3d numpy array
    ```python
    name2 = 'CT.1.3.12.2.1107.5.1.7.130094.30000022051213533424400000'# 214->348
    path2 = 'C:/Users/shuangzhou/Downloads/Head_Phantom/head2/'
    idx2 = np.arange(214,348)
    head,dxyz = read_3d_head_phantom(path2,name2,idx2)
    # save it for later use or don't save
    np.savez('./Phantom/head.npz', head=head, dxyz=dxyz)
    ```
- write the 3D numpy array into 1D binary file
    ```python
    #transpose(2, 1, 0) is required for matlab
    image = np.array(head,dtype=np.short).transpose(2, 1, 0).flatten()
    mc.write_image(image,current_file_path + '\\Phantom\\')
    ```
- create a geometry for the CT file (see minimum example)
    ```python
    geo.set_header(Nx,Ny,Nz,dx,dy,dz)# see comments
    geo.set_cfg(energy,spot_size,num_particle)# see comments
    ```
- build your geometry
    ```python
    geo.create_cfg_file('pencilbeam.cfg')
    geo.create_header_file()
    ```
- run
    ```python
    start = time.time()
    dose = pmc.run(geo.cfg_file,image)
    print("Total time = ",time.time() - start)
    totalDose = np.array(dose).reshape((geo.Nz,geo.Nx,geo.Ny)).transpose(2, 1, 0)
    ```
- plot results in python
    ```python
    viewer = napari.view_image(totalDose, rgb=False)
    napari.run()  # start the event loop and show viewer
    ```
- save results to matlab
    ```python
    savemat(geo.outputdir+'waterDose'+str(E)+'.mat',{'totalDose':totalDose, 'dx':geo.dx, 'dy':geo.dy, 'dz':geo.dz})
    ```
- read data in matlab (see minimum example)

# Don't want to run with python
- get geometry and img files ready
- open cmd in current folder
- `appgopmc_dose.exe --config ./Phantom/pencilbeam.cfg`

# matlab_func
    All files in it are not used for IMPT, they are used for MLSIC
# Important files 
``` python
appgopmc_dose.cp39-win_amd64.pyd
# GPU Monte Carlo engine, python module
# import appgopmc_dose
# pmc = appgopmc_dose.appgopmc_dose()
# dose = pmc.run(cfg_file,image) # cfg_file: full path of pencilbeam.cfg file, image: flatten 3d numpy array (placeholder,not used)
appgopmc_dose.exe
# os.system('appgopmc_dose.exe --config ./Phantom/pencilbeam.cfg')
# results saved in, output/totalDose.img and output/totalDose.header

Phantom.cl, ParticleStatus.cl, Macro.h, randomKernel.h
# they will be read by Monte Carlo engine should not change, don't move to other folder
```