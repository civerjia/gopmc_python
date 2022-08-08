import numpy as np
import os
try:
    from create_sence import scene
except:
    from .create_sence import scene
class geometry:
    def __init__(self,path) -> None:
        """instantiation

        Args:
            path (string): i.e. C:\\Users\\Public\\Data\\gopmc_python
        """
        self.path = path.replace('\\','/')

        ## fixed values
        self.data_type = 'short' # short or int
        self.byte_order = 0#fixed 0: least significant bit first(0001)  1:most significant bit first(1000)
        # not used
        self.translation = [0,0,0]
        self.rotation = [0,0,0]
        self.referenceImageIsocenter = [0,0,0]
        self.reverseX = 0
        self.reverseY = 0
        self.reverseZ = 0
        self.ImageOrientationPatient = [1,0,0,0,1,0,0,0,1]
    def set_header(self, Nx = 51,Ny = 51,Nz = 120,dx = 0.1,dy = 0.1,dz = 0.1,center = [0,0,0]):
        """set geo_phantom.header parameters with user input

        Args:
            Nx (int, optional): Number of voxel x. Defaults to 51.
            Ny (int, optional): Number of voxel y. Defaults to 51.
            Nz (int, optional): Number of voxel z. Defaults to 120.
            dx (float, optional): x voxel size(cm). Defaults to 0.1.
            dy (float, optional): y voxel size(cm). Defaults to 0.1.
            dz (float, optional): z voxel size(cm). Defaults to 0.1.
            center (list, optional): center of whole image volume(cm). Defaults to [0,0,0].
        """
        ## header arguments
        # number of voxels
        self.Nx = Nx
        self.Ny = Ny
        self.Nz = Nz
        # voxel size (cm)
        self.dx = dx
        self.dy = dy  
        self.dz = dz
        # first voxel index
        self.first_idx = [0,0,0]
        self.center = center# unit(cm)
        # first voxel center position (cm)
        self.x0 = (self.first_idx[0] - (self.Nx-1))*self.dx/2 + self.center[0]
        self.y0 = (self.first_idx[1] - (self.Ny-1))*self.dy/2 + self.center[1]
        self.z0 = (self.first_idx[2] - (self.Nz-1))*self.dz/2 + self.center[2]
    def set_header_default(self):
        ## header arguments
        # number of voxels
        self.Nx = 100
        self.Ny = 100
        self.Nz = 1600
        # voxel size (cm)
        self.dx = 0.1
        self.dy = 0.1   
        self.dz = 0.01
        # first voxel index
        self.first_idx = [0,0,0]
        self.center = [0,0,0]# unit(cm)
        # first voxel center position (cm)
        self.x0 = (self.first_idx[0] - (self.Nx-1))*self.dx/2 + self.center[0]
        self.y0 = (self.first_idx[1] - (self.Ny-1))*self.dy/2 + self.center[1]
        self.z0 = (self.first_idx[2] - (self.Nz-1))*self.dz/2 + self.center[2]
    def set_cfg(self,energy = 110.0,spot_size = [0,0],num_particle = 1e6,rx = 0,ry = 0,rz = 0,src_center = [0,0,-40]):
        """ set pencilbeam.cfg parameters with user input

        Args:
            energy (float, optional): proton beam energy(MeV). Defaults to 110.0.
            spot_size (list, optional): [x size, y size] beam spot size (cm), sqare beam shape. Defaults to [0,0].
            num_particle (int, optional): number of proton particles. Defaults to 1e6.
            rx (int, optional): rotation around x-axis: angle(degree). Defaults to 0.
            ry (int, optional): rotation around y-axis: angle(degree). Defaults to 0.
            rz (int, optional): rotation around z-axis: angle(degree). Defaults to 0.
            src_center (list, optional): beam source center position(cm) [x,y,z], beam direction is [0,0,1] by default
        """
        ## cfg arguments
        self.min_energy = 1.0
        self.energy = energy
        self.spot_size = spot_size# beam spot size (cm), sqare beam shape
        self.num_particle = num_particle# integer, num of particles
        self.src_center = src_center# beam source center position(cm)
        # rotation mode: 
        # Rz()*Ry()*Rx()*init_vec
        # beam initial direction vector
        self.beam_init_vec = np.array([[0,0,1]]).T# show be column vector
        self.rot_x = rx# rotation around x-axis: angle(degree)
        self.rot_y = ry# rotation around x-axis: angle(degree)
        self.rot_z = rz# rotation around x-axis: angle(degree)
    def set_cfg_default(self):
        ## cfg arguments
        self.min_energy = 1.0
        self.energy = 110.0
        self.spot_size = [0.6,0.6]# beam spot size (cm), spare beam shape
        self.num_particle = 1e6# integer, num of particles
        self.src_center = [0,0,self.z0-1]# beam source center position(cm)
        # rotation mode: 
        # Rz()*Ry()*Rx()*init_vec
        # beam initial direction vector
        self.beam_init_vec = np.array([[0,0,1]]).T# show be column vector
        self.rot_x = 0# rotation around x-axis: angle(degree)
        self.rot_y = 0# rotation around y-axis: angle(degree)
        self.rot_z = 0# rotation around z-axis: angle(degree)

        #cfg_file = self.create_cfg_file(cfg_filename,self.path)
    def set_header_from_scene(self,s):
         ## header arguments
        # number of voxels
        self.Nx = s.Nx
        self.Ny = s.Ny
        self.Nz = s.Nz
        # voxel size (cm)
        self.dx = s.dx
        self.dy = s.dy   
        self.dz = s.dz
        # first voxel index
        self.first_idx = [0,0,0]
        self.center = [0,0,0]# unit(cm)
        # first voxel center position (cm)
        self.x0 = (self.first_idx[0] - (self.Nx-1))*self.dx/2 + self.center[0]
        self.y0 = (self.first_idx[1] - (self.Ny-1))*self.dy/2 + self.center[1]
        self.z0 = 0
    def set_cfg_for_MLSIC(self,x,y):
        ## cfg arguments
        self.min_energy = 1.0
        self.energy = 227.1
        self.spot_size = [6,6]# beam spot size (cm), sqare beam shape
        self.num_particle = 1e6# integer, num of particles
        self.src_center = [x,y,self.z0-1]# beam source center position(cm)
        # rotation mode: 
        # Rz()*Ry()*Rx()*init_vec
        # beam initial direction vector
        self.beam_init_vec = np.array([[0,0,1]]).T# show be column vector
        self.rot_x = 0# rotation around x-axis: angle(degree)
        self.rot_y = 0# rotation around y-axis: angle(degree)
        self.rot_z = 0# rotation around z-axis: angle(degree)

    def Rx(self,degree):
        x = np.pi*degree/180.
        # rotation matrix
        r = np.array([[1   ,        0,        0],
                    [  0   ,np.cos(x),-np.sin(x)],
                    [  0   ,np.sin(x), np.cos(x)]])
        return r
    def Ry(self,degree):
        x = np.pi*degree/180.
        # rotation matrix
        r = np.array([[np.cos(x),  0, np.sin(x)],
                    [  0        ,  1,        0],
                    [ -np.sin(x),  0, np.cos(x)]])
        return r
    def Rz(self,degree):
        x = np.pi*degree/180.
        # rotation matrix
        r = np.array([[np.cos(x),-np.sin(x),     0],
                    [  np.sin(x), np.cos(x),     0],
                    [  0        ,         0,     1]])
        return r
    def create_cfg_file(self,cfg_filename = 'pencilbeam.cfg'):
        """ create cfg_filename file and save it in ./Phantom/

        Args:
            cfg_filename (str, optional): file name. Defaults to 'pencilbeam.cfg'.
        """
        physics_path = self.path + "/input/"
        cfg_file = self.path+'/Phantom/'+cfg_filename
        self.cfg_file = cfg_file
        file = open(cfg_file, "w+") 
        # header = open(self.path+'geo_phantom.header', "w+") 
        macro_cross_section_file = 'mcpro_G4.imfp'
        assert os.path.exists(physics_path+macro_cross_section_file),(physics_path+macro_cross_section_file+' not exist!')
        mass_stopping_power_ratio_file = 'mcpro.mater'
        assert os.path.exists(physics_path+mass_stopping_power_ratio_file),(physics_path+mass_stopping_power_ratio_file+' not exist!')
        restricted_stopping_power_in_water_file = 'mcpro3.rstpw'
        assert os.path.exists(physics_path+restricted_stopping_power_in_water_file),(physics_path+restricted_stopping_power_in_water_file+' not exist!')
        density_correction_factor_file = 'densityCorrection.dat'
        assert os.path.exists(physics_path+density_correction_factor_file), (physics_path+density_correction_factor_file+' not exist!')
        # setup physic and LUT
        file.write('physics.macro_cross_section.file=%s%s\n'% (physics_path,macro_cross_section_file))
        file.write('physics.mass_stopping_power_ratio.file=%s%s\n' % (physics_path,mass_stopping_power_ratio_file))
        file.write('physics.restricted_stopping_power_in_water.file=%s%s\n' % (physics_path,restricted_stopping_power_in_water_file))
        file.write('physics.density_correction_factor.file=%s%s\n' % (physics_path,density_correction_factor_file))
        #
        min_simulation_energy=self.min_energy# 1.0 MeV
        assert self.min_energy <= self.energy,'self.energy < self.min_energy!'
        file.write('cfg.min_simulation_energy=%f\n' % min_simulation_energy)

        # load geometry setting
        #geo_phantom is geometry file name, .header is file extension
        geometry_path = self.path+'/Phantom/geo_phantom'# water_phan_HU_40cm  geo_phantom
        assert os.path.exists(geometry_path+'.header'),(geometry_path+'.header'+' not exist!')
        file.write('in.ct.file=%s\n' % geometry_path)

        # proton beam setting
        spot_size = self.spot_size# [0, 0] [x,y] size unit(cm), square beam shape
        file.write('cfg.spot_size=%f\t%f\n' % (spot_size[0],spot_size[1]))
        energy = self.energy# 110.0 proton energy MeV
        file.write('cfg.source.energy=%f\n' % energy)
        num_of_particles = self.num_particle
        file.write('cfg.number_simulation_particles=%d\n' % num_of_particles)
        src_center = self.src_center# [0,0,-20][x,y,z] unit(cm)
        file.write('cfg.source.center=%f\t%f\t%f\n' % (src_center[0],src_center[1],src_center[2]))

        # normalized direction vector(degree)
        beam_direction_vec = self.Rz(self.rot_z)@(self.Ry(self.rot_y)@(self.Rx(self.rot_x)@self.beam_init_vec))

        file.write('cfg.source.direction=%f\t%f\t%f\n' % (beam_direction_vec[0],beam_direction_vec[1],beam_direction_vec[2]))
        # add opencl file path(not used)
        file.write('cl.directory=%s\n' % (self.path+'/cl_files/'))
        # output directory
        self.outputdir = './output/'
        file.write('output.directory=%s\n' % self.outputdir)
        file.close()
    def create_header_file(self):
        """create geo_phantom.header file and save it in ./Phantom/
        """
        header_file = self.path+'/Phantom/'+'geo_phantom.header'
        file = open(header_file, "w+") 

        file.write('imageType =\n')#not used
        file.write('data_type = %s\n' % self.data_type)#fixed data type, short or int
        file.write('byte_order = %d\n' % self.byte_order)
        file.write('bytes_pix = 2\n')

        file.write('vol_min = 0\n')
        file.write('vol_max = 4096\n')

        file.write('x_dim = %d\n' % self.Nx)
        file.write('y_dim = %d\n' % self.Ny)
        file.write('z_dim = %d\n' % self.Nz)

        file.write('x_pixdim = %f\n' % self.dx)
        file.write('y_pixdim = %f\n' % self.dy)
        file.write('z_pixdim = %f\n' % self.dz)

        # first voxel position
        file.write('x_start = %f\n' % self.x0)
        file.write('y_start = %f\n' % self.y0)
        file.write('z_start = %f\n' % self.z0)

        file.write('date =\n')
        file.write('time =\n')
        file.write('db_name =\n')
        file.write('uid =\n')
        file.write('referenceUID =\n')
        file.write('originalUID =\n')

        file.write('patientPosition =\n')
        file.write('FrameOfReferenceUID =\n')

        file.write('translation = [%f\t%f\t%f]\n' % (self.translation[0],self.translation[1],self.translation[2]))
        file.write('rotation = [%f\t%f\t%f]\n' % (self.rotation[0],self.rotation[1],self.rotation[2]))
        file.write('referenceImageIsocenter = [%f\t%f\t%f]\n' % (self.referenceImageIsocenter[0],self.referenceImageIsocenter[1],self.referenceImageIsocenter[2]))

        file.write('reverseX = %d\n' % self.reverseX)
        file.write('reverseY = %d\n' % self.reverseY)
        file.write('reverseZ = %d\n' % self.reverseZ)

        file.write('ImageOrientationPatient = [%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d]\n' % (
            self.ImageOrientationPatient[0],self.ImageOrientationPatient[1],self.ImageOrientationPatient[2],
            self.ImageOrientationPatient[3],self.ImageOrientationPatient[4],self.ImageOrientationPatient[5],
            self.ImageOrientationPatient[6],self.ImageOrientationPatient[7],self.ImageOrientationPatient[8]))

        file.write('LinearMeasureUnit = cm\n')
        file.write('TransformMatrix =\n')

        file.close()


if __name__ == '__main__':
    geo = geometry(r'C:/Users/Public/Data/gopmc_python')
    # geo = geometry(r'/Users/shuangzhou/projects/gopmc_python')
    geo.set_header_default()
    geo.set_cfg_default()
    geo.create_cfg_file('pencilbeam.cfg')
    geo.create_header_file()
