import os
from pathlib import Path
import pydicom
import numpy as np
from pydicom import dcmread
import pydicom
import matplotlib.pyplot as plt
import csv
import threading
import time
folderprefix = "/media/user/Data/doc/manifest-1600709154662/"
# ds = dcmread(folderpath + "1-001.dcm")

# type(ds.PixelData)
# len(ds.PixelData)
# arr = ds.pixel_array

# plt.imshow(arr, cmap="gray")
# plt.show()

def main():
    with open(folderprefix + 'metadata_large.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    large_dirs = [
        x
        for xs in data
        for x in xs
    ]

    for item in large_dirs:
        folderpath = folderprefix + item
        while threading.active_count() >= 10:
            print(">=10 threads running, waiting...")
            time.sleep(10)
        print("Starting " + folderpath)
        t = threading.Thread(target=conversion, args=(folderpath,))
        t.start()



def conversion(folderpath):
    dicom_imgs = None
    for root, _, filenames in os.walk(folderpath):
        sorted_filenames = sorted(filenames)
        for filename in sorted_filenames:
            # print("Processing " + filename)
            dcm_path = Path(root, filename)
            if dcm_path.suffix == ".dcm":
                try:
                    dicom = pydicom.dcmread(dcm_path, force=True)
                except IOError as e:
                    print(f"Can't import {dcm_path.stem}")
                else:
                    if (dicom_imgs is None):
                        dicom_imgs = np.zeros((dicom.pixel_array.shape[0], dicom.pixel_array.shape[1], 1))
                    if (dicom_imgs.shape[0] == dicom.pixel_array.shape[0] and dicom_imgs.shape[1] == dicom.pixel_array.shape[1]):
                        dicom_imgs = np.dstack((dicom.pixel_array, dicom_imgs))
                    else:
                        dicom_imgs = None
                        continue

        if (dicom_imgs is not None):
            pathParts = root.split('/')
            folder_out_path = pathParts[-3] + "/" + pathParts[-2] + "/" + pathParts[-1]
            if (not os.path.exists("/media/user/Data/doc/npy-out/" + folder_out_path)):
                os.makedirs("/media/user/Data/doc/npy-out/" + folder_out_path)
            filenameout = "/media/user/Data/doc/npy-out/" + folder_out_path + "-patient-" + pathParts[-3].split('-')[-1] + ".npy"
            with open(filenameout, "wb") as f:
                print("Completed " + filenameout)
                np.save(f, dicom_imgs)
        dicom_imgs = None

main()
