#just a test class to teset looping 
#import Image from PIL
import os
import glob
import cv2 

Folder_B = "test_a/07-windows-masked/"
OUTPUT = "data_batch/B/"
i = 0
count = 0
#loop and read
#data_path = os.listdir(pathName + '/' + )

#images = [cv2.imread(file) for file in glob.glob(os.path.join(Folder_B, '*.jpg'))]
#for img in images:

for filename in os.listdir(Folder_B):
    try:
        image = cv2.imread((os.path.join(Folder_B, filename)))
        scale_percent = 60 
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(os.path.join(OUTPUT, filename[:-10] + ".jpg"), resized)
        i +=1
        print(i)
    except Exception:
        print(filename)
   
        


#loop and write