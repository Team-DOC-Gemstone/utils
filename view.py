import SimpleITK as sitk
import matplotlib.pylab as plt
ct_scans = sitk.GetArrayFromImage(sitk.ReadImage("/media/arjun/Data/doc-data/subset0/1.3.6.1.4.1.14519.5.2.1.6279.6001.100684836163890911914061745866.mhd", sitk.sitkFloat32))
plt.figure(figsize=(20,16))
plt.gray()
plt.subplots_adjust(0,0,1,1,0.01,0.01)
print("Length" + str(len(ct_scans)))
for i in range(30):
    plt.subplot(5,6,i+1), plt.imshow(ct_scans[i]), plt.axis('off')
    # use plt.savefig(...) here if you want to save the images as .jpg, e.g.,
plt.show()
