import cv2 
import os

Folder_B = "data_batch/TODO/"
OUTPUT = "data_batch/test/"
scale_percent = 60 

for filename in os.listdir(Folder_B):
    try:
        image = cv2.imread(filename,  cv2.IMREAD_UNCHANGED)
        cv2.imwrite(os.path.join(OUTPUT, filename[:-10] + "resized.png"), img)
    except Exception:
        print(filename)


"""gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        letter = morph.copy()
        cntrs = cv2.findContours(morph, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cntrs = cntrs[0] if len(cntrs) == 2 else cntrs[1]
        for c in cntrs:
            area = cv2.contourArea(c)
            if area < 100:
                cv2.drawContours(letter,[c],0,(0,0,0),-1)"""