import numpy as np
def get_RangeShifterStatus(Ein):
    Energies = np.array([25.840,29.930,33.470,36.900,40.060,
            43.090,45.850,48.600,51.200,53.740,
            56.090,58.460,60.740,62.980,65.080,
            67.210,69.260,71.300,73.230,75.180,
            77.070,78.950,80.730,82.550,84.310,
            86.070,87.560,89.270,90.930,92.600,
            94.180,95.800,97.380,98.960,100.11,
            101.60,103.08,104.54,105.99,107.42,
            108.84,110.24,111.63,113.01,114.38,
            115.73,117.07,118.41,119.73,121.04,
            122.34,123.63,124.91,126.18,127.44,
            128.70,129.94,131.18,132.41,133.63,
            134.84,135.59,136.05,137.24,138.43,
            139.22,139.62,142.71,146.24,149.66,
            152.99,156.30,159.60,162.75,165.93,
            168.99,172.10,175.13,178.10,181.06,
            184.02,186.98,189.85,192.64,195.46,
            198.22,201.06,201.54,203.76,206.47,
            227.10])
    matched_idx = np.argmin(np.abs(Ein - Energies))
    E = Energies[matched_idx]
    print('Matched energy = ',E,' MeV')
    if np.abs(E - 25.84)<1e-1 :
        RangeShifterStatus = np.flip(np.array([1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 33.47)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
    elif np.abs(E - 40.06)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
    elif np.abs(E - 45.85)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 51.20)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 56.09)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
    elif np.abs(E - 60.74)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
    elif np.abs(E - 65.08)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 69.26)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 73.23)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1]))
    elif np.abs(E - 77.07)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1]))
    elif np.abs(E - 80.73)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 84.31)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 87.56)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]))
    elif np.abs(E - 90.93)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]))
    elif np.abs(E - 94.18)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 97.38)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 29.93)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 36.90)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
    elif np.abs(E - 43.09)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
    elif np.abs(E - 48.60)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 53.74)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 58.46)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
    elif np.abs(E - 62.98)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
    elif np.abs(E - 67.21)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 71.30)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 75.18)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1]))
    elif np.abs(E - 78.95)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1]))
    elif np.abs(E - 82.55)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 86.07)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 89.27)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 92.60)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]))
    elif np.abs(E - 95.80)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 98.96)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 206.47)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0]))
    elif np.abs(E - 203.76)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0]))
    elif np.abs(E - 201.06)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0]))
    elif np.abs(E - 198.22)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]))
    elif np.abs(E - 195.46)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1]))
    elif np.abs(E - 192.64)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1]))
    elif np.abs(E - 189.85)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1]))
    elif np.abs(E - 186.98)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1]))
    elif np.abs(E - 184.02)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]))
    elif np.abs(E - 181.06)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]))
    elif np.abs(E - 178.10)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1]))
    elif np.abs(E - 175.13)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1]))
    elif np.abs(E - 172.10)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]))
    elif np.abs(E - 168.99)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]))
    elif np.abs(E - 165.93)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1]))
    elif np.abs(E - 162.75)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1]))
    elif np.abs(E - 159.60)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1]))
    elif np.abs(E - 156.30)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1]))
    elif np.abs(E - 152.99)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1]))
    elif np.abs(E - 149.66)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1]))
    elif np.abs(E - 146.24)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1]))
    elif np.abs(E - 142.71)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1]))
    elif np.abs(E - 139.22)<1e-1:
        RangeShifterStatus = np.flip(np.array([0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1]))
    elif np.abs(E - 135.59)<1e-1:
        RangeShifterStatus = np.flip(np.array([1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]))
    elif np.abs(E - 100.11)<1e-1:
        RangeShifterStatus = np.array([1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0])
    elif np.abs(E - 101.60)<1e-1:
        RangeShifterStatus = np.array([1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1])
    elif np.abs(E - 103.08)<1e-1:
        RangeShifterStatus = np.array([1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0])
    elif np.abs(E - 104.54)<1e-1:
        RangeShifterStatus = np.array([1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1])
    elif np.abs(E - 105.99)<1e-1:
        RangeShifterStatus = np.array([1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0])
    elif np.abs(E - 107.42)<1e-1:
        RangeShifterStatus = np.array([1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1])
    elif np.abs(E - 108.84)<1e-1:
        RangeShifterStatus = np.array([1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
    elif np.abs(E - 110.24)<1e-1:
        RangeShifterStatus = np.array([1,1,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1])
    elif np.abs(E - 111.63)<1e-1:
        RangeShifterStatus = np.array([1,1,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0])
    elif np.abs(E - 113.01)<1e-1:
        RangeShifterStatus = np.array([1,1,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1])
    elif np.abs(E - 114.38)<1e-1:
        RangeShifterStatus = np.array([1,1,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
    elif np.abs(E - 115.73)<1e-1:
        RangeShifterStatus = np.array([1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1])
    elif np.abs(E - 117.07)<1e-1:
        RangeShifterStatus = np.array([1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0])
    elif np.abs(E - 118.41)<1e-1:
        RangeShifterStatus = np.array([1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1])
    elif np.abs(E - 119.73)<1e-1:
        RangeShifterStatus = np.array([1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0])
    elif np.abs(E - 121.04)<1e-1:
        RangeShifterStatus = np.array([1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1])
    elif np.abs(E - 122.34)<1e-1:
        RangeShifterStatus = np.array([1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0])
    elif np.abs(E - 123.63)<1e-1:
        RangeShifterStatus = np.array([1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1])
    elif np.abs(E - 124.91)<1e-1:
        RangeShifterStatus = np.array([1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0])
    elif np.abs(E - 126.18)<1e-1:
        RangeShifterStatus = np.array([1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1])
    elif np.abs(E - 127.44)<1e-1:
        RangeShifterStatus = np.array([1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0])
    elif np.abs(E - 128.70)<1e-1:
        RangeShifterStatus = np.array([1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1])
    elif np.abs(E - 129.94)<1e-1:
        RangeShifterStatus = np.array([1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
    elif np.abs(E - 131.18)<1e-1:
        RangeShifterStatus = np.array([1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1])
    elif np.abs(E - 132.41)<1e-1:
        RangeShifterStatus = np.array([1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0])
    elif np.abs(E - 133.63)<1e-1:
        RangeShifterStatus = np.array([1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1])
    elif np.abs(E - 134.84)<1e-1:
        RangeShifterStatus = np.array([1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
    elif np.abs(E - 136.05)<1e-1:
        RangeShifterStatus = np.array([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1])
    elif np.abs(E - 137.24)<1e-1:
        RangeShifterStatus = np.array([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0])
    elif np.abs(E - 138.43)<1e-1:
        RangeShifterStatus = np.array([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1])
    elif np.abs(E - 139.62)<1e-1:
        RangeShifterStatus = np.array([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0])
    elif np.abs(E - 201.54)<1e-1:
        RangeShifterStatus = np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif np.abs(E - 227.10)<1e-1:
        RangeShifterStatus = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    else:
        print('No matched energy! Set to Maximum energy')
        RangeShifterStatus = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    return RangeShifterStatus == 1
    
if __name__ == '__main__':
    print(get_RangeShifterStatus(-10))