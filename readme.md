unit is cm

``` python

appgopmc_dose.cp39-win_amd64.pyd
# GPU Monte Carlo engine, python module
# import appgopmc_dose
# pmc = appgopmc_dose.appgopmc_dose()
# dose = pmc.run(cfg_file,image) # cfg_file: full path of pencilbeam.cfg file, image: flatten 3d numpy array (placeholder,not used)
appgopmc_dose.exe
# os.system('appgopmc_dose.exe --config ./Phantom/pencilbeam.cfg')
# results saved in, output/totalDose.img and output/totalDose.header

geometry.set_header( Nx = 51,Ny = 51,Nz = 120,dx = 0.1,dy = 0.1,dz = 0.1,center = [0,0,0])
#center : center of whole image volume

geometry.set_cfg(energy = 110.0,spot_size = [0,0],num_particle = 1e6,rx = 0,ry = 0,rz = 0)
#spot_size : spot size of proton beam, unlike TOPAS, #the beam shape is square
# rotation mode: Rz()*Ry()*Rx()*[0,0,1] angle in degree

geometry.set_header_from_scene(s)
# create geometry from CT scene

mc_setting.get_RangeShifterStatus(Ein) 
# Mevion S250i range shifter setting, 
# input : energy
# return on/off of each range shifter slab

mc_setting.get_RangeShifterZidx(E,dz) 
# range shifter thickness and location, convert range shifter to voxelized 3d array
# input : energy, depth voxel size
# return z idx occupied by range shifter

mc_setting.materials()
# return dictionary of {material:HU value}

mc_setting.read_dicom.py
# read dicom files in local hard drive, convert it into 3d numpy array, saved in ./Phantom/*.npy file

mc_setting.write_image(image,path)
# write 3d numpy array to ./Phantom/geo_phantom.img file, it will read by Monte Carlo engine later

Phantom.cl, ParticleStatus.cl, Macro.h, randomKernel.h
# they will be read by Monte Carlo engine should not change, don't move to other folder

```
matlab_func : only `rw_img.m` is used for IMPT, others files are for MLSIC

minimum example:
- run_mc.py with Water function

How to load CT images:
- read dicom files with read_dicom.py, costumize your own path and filename
- convert dicom files to a single 3d numpy array
- create a scene with the CT file
- build your geometry
- run

```python
image = np.array(image,dtype=np.short).transpose(2, 1, 0).flatten()
mc.write_image(image,current_file_path + '\\Phantom\\')
start = time.time()
dose = pmc.run(geo.cfg_file,image)
print("Total time = ",time.time() - start)
totalDose = np.array(dose).reshape((geo.Nz,geo.Nx,geo.Ny)).transpose(2, 1, 0)
```

