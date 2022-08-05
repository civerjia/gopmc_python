import numpy as np
try:
    from get_range_shifter_status import get_RangeShifterStatus
except:
    from .get_range_shifter_status import get_RangeShifterStatus
def get_RangeShifterZidx(E,dz):
    #start location in cm
    RangeShifterPlatesLocStart = np.array([0,6.14,9.31,10.32,12.02,13.72,15.42,17.12,18.82,20.52,22.22,23.92,25.62,27.32,29.02,30.72,32.96,34.60])
    RangeShifterPlatesThickness = np.array([5.81,2.90,0.72,1.44,1.44,1.44,1.44,1.44,1.44,1.44,1.44,1.44,1.44,1.44,1.44,1.44,0.36,0.18])# in cm
    RangeShifterPlatesLocEnd = RangeShifterPlatesLocStart + RangeShifterPlatesThickness
    zidx_start = RangeShifterPlatesLocStart/dz
    zidx_end = RangeShifterPlatesLocEnd/dz

    status = get_RangeShifterStatus(E)
    if np.any(status):
        zidx_start_valid = zidx_start[status].astype(np.int32)
        zidx_end_valid = zidx_end[status].astype(np.int32)
        zidx_valid = np.arange(zidx_start_valid[0],zidx_end_valid[0]+1)
        for idx in range(1,len(zidx_start_valid)):
            zidx_valid = np.append(zidx_valid,np.arange(zidx_start_valid[idx],zidx_end_valid[idx]+1))
    else:
        zidx_valid = None
    
    return zidx_valid
if __name__ == '__main__':
    E = 0
    dz = 0.01
    zidx_valid = get_RangeShifterZidx(E,dz)
    print(zidx_valid)
