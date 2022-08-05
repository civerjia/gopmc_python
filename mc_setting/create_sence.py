import numpy as np
try:
    from get_range_shifter_volume import get_RangeShifterZidx
    from material_dict import materials
except:
    from .get_range_shifter_volume import get_RangeShifterZidx
    from .material_dict import materials
import matplotlib.pyplot as plt
class scene():
    def __init__(self) -> None:
        pass
    def create_simple_scene(self,E,x,y):
        phantom = np.load('./Phantom/head.npz')
        if (x is None) or (y is None):
            head = phantom['head']
        else:
            head = phantom['head'][x[0]:x[1],y[0]:y[1],:]
        self.dx = phantom['dxyz'][0] / 10.
        self.dy = phantom['dxyz'][1] / 10.
        self.dz = phantom['dxyz'][2] / 10.
        phantom.close()
        phantom_size = head.shape
        self.RangeShifter_idx = get_RangeShifterZidx(E,self.dz)
        # range shifter end location , any object should be placed behind this 
        RangeShifterloc_end = 34.78# cm
        offset = 2
        self.phantom_idx = np.ceil((RangeShifterloc_end + offset)/self.dz).astype(np.int32) + np.arange(phantom_size[2])
        # single layer PCB(1.6mm) water equivalent thickness
        wet = 0.29# cm
        numLayer = 66
        gap = 2
        idx = np.ceil((numLayer-1)*wet/self.dz).astype(np.int32)
        self.MLSIC_idx = np.ceil((gap)/self.dz).astype(np.int32) + self.phantom_idx[-1] + np.arange(idx)

        m = materials()
        self.Nz = self.MLSIC_idx[-1]+1
        self.Nx = phantom_size[0]
        self.Ny = phantom_size[1]
        self.image = m['Air']*np.ones((self.Nx,self.Ny,self.Nz),dtype=np.short)
        if self.RangeShifter_idx is not None:
            self.image[:,:,self.RangeShifter_idx] = m['Lexan']
        else:
            self.RangeShifter_idx = np.arange((34.78/self.dz).astype(np.int32)+1)
        self.image[:,:,self.phantom_idx] = head.astype(dtype=np.short)
        self.image[:,:,self.MLSIC_idx] = m['Water']

if __name__ =='__main__':
    s = scene()
    # ROI: reduce useless computation
    x = [160,361]
    y = [160,361]
    s.create_simple_scene(200,x,y)
    print(s.MLSIC_idx)
    plt.imshow(s.image[:,:,300])
    plt.show()
    plt.plot(range(np.size(s.image,2)),s.image[100,100,:])
    plt.show()