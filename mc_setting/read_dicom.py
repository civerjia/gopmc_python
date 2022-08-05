from fileinput import filename
import pydicom
import numpy as np
import napari
import matplotlib.pyplot as plt
def show_head_phantom_slice(path,name,idx):
    filename = name+str(idx)+'.dcm'
    ds = pydicom.dcmread(path+filename)
    plt.imshow(ds.pixel_array, cmap=plt.cm.bone) 
    plt.show()
    dxyz = np.array([ds.PixelSpacing[0],ds.PixelSpacing[1],ds.SliceThickness])
    print('dxyz = ', dxyz,' mm')
    print('RescaleSlope = ',ds.RescaleSlope)
    print('RescaleIntercept = ',ds.RescaleIntercept)
def read_3d_head_phantom(path,name,idx):
    head = np.zeros((512,512,len(idx)))
    for i in idx:
        filename = name+str(i)+'.dcm'
        ds = pydicom.dcmread(path+filename)
        head[:,:,i-idx[0]] = np.array(ds.pixel_array*ds.RescaleSlope + ds.RescaleIntercept)
    dxyz = np.array([ds.PixelSpacing[0],ds.PixelSpacing[1],ds.SliceThickness])
    return head, dxyz
def get_phantom():
    name2 = 'CT.1.3.12.2.1107.5.1.7.130094.30000022051213533424400000'# 214->348
    path2 = 'C:/Users/shuangzhou/Downloads/Head_Phantom/head2/'
    idx2 = np.arange(214,348)
    head,dxyz = read_3d_head_phantom(path2,name2,idx2)
    return head, dxyz
if __name__ == '__main__':
    name1 = 'CT.1.3.12.2.1107.5.1.7.130094.30000022051213434086400000'# 233->420
    name2 = 'CT.1.3.12.2.1107.5.1.7.130094.30000022051213533424400000'# 214->348
    path1 = 'C:/Users/shuangzhou/Downloads/Head_Phantom/head1/'
    path2 = 'C:/Users/shuangzhou/Downloads/Head_Phantom/head2/'
    idx1 = np.arange(233,421)
    idx2 = np.arange(214,348)
    # show_head_phantom_slice(path2,name2,300)
    # head1,_ = read_3d_head_phantom(path1,name1,idx1)
    # viewer = napari.view_image(head1, rgb=False)
    # napari.run()  # start the event loop and show viewer
    head,dxyz = read_3d_head_phantom(path2,name2,idx2)
    np.savez('./Phantom/head.npz', head=head, dxyz=dxyz)