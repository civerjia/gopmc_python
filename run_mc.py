import appgopmc_dose
import numpy as np
import os 
from scipy.io import savemat
import matplotlib.pyplot as plt

pmc = appgopmc_dose.appgopmc_dose()

cwd = os.getcwd()
current_file_path = os.path.dirname(os.path.abspath(__file__))
if cwd != current_file_path:
    os.chdir(current_file_path)

pencilbeam_cfg_path = 'C:/Users/Public/Data/gopmcdose_v4a_py/goPMC_dose/pencilbeam.cfg'

image = np.zeros((100*100*1600,1),dtype=np.short)
dose = pmc.run(pencilbeam_cfg_path,image)
totalDose = np.array(dose).reshape((1600,100,100))
savemat("totalDose.mat", {'totalDose':totalDose})
fig,ax = plt.subplots()
ax.matshow(totalDose[800,:,:])
plt.show()