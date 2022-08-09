import numpy as np
import matplotlib.pyplot as plt
try:
    from create_sence import scene
except:
    from .create_sence import scene
def write_image(image,path,filename = 'geo_phantom.img'):
    # write to file
    image.flatten().astype(np.short).tofile(path+filename)
if __name__ =='__main__':
    s = scene()
    # ROI: reduce useless computation
    # x_ROI = [160,361]
    # y_ROI = [160,361]
    x_ROI = None
    y_ROI = None
    s.create_simple_scene(200,x_ROI,y_ROI)
    plt.imshow(s.image[:,:,300])
    plt.show()
    plt.plot(range(np.size(s.image,2)),s.image[100,100,:])
    plt.show()
    image = np.array(s.image,dtype=np.short).flatten()
    path = './Phantom/'
    write_image(image,path)