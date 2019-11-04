import os
import numpy as np
import glob
import shutil
import time
'''for root, dirs, files in os.walk("/home/anshuman/3/anshu_first_training"):
    print("root: ", root)
    print("dirs: ", dirs)
    #print(files)'''


'''for dirs in os.listdir("/home/anshuman/3/anshu_first_training"):
    #print("root: ", root)
    print("dirs: ", dirs)
    #print(files)'''
while True:
    list_dir = []
    for f in os.scandir("/home/anshuman/3/anshu_first_training"):
        if f.is_dir():
            print("path: ", f.path)
            print(f.path.split("-")[1])
            list_dir.append(f.path.split("-")[1])
            
    print("Before: ", list_dir)
    list_dir = np.sort(list_dir)
    print("After: ", list_dir)

    for i in range(len(list_dir) - 1):
        for name in glob.glob("/home/anshuman/3/anshu_first_training/*" + list_dir[i]):
            print("Deleting: ", name)
            shutil.rmtree(name)
            print("Done!!!")
    time.sleep(9)


