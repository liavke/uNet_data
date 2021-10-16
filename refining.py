import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

img = cv2.imread('0010-001197-before.png' )

cv2.imwrite("some_image.bmp", img )

blur = cv2.blur(img,(5,5))

cv2.imwrite("0010-001197-blured.png", blur)

smooth = cv2.addWeighted(blur,1.5,img,-0.5,0)

cv2.imwrite("0010-001197-smoothed.png", smooth)

sigma = 0.33

v = np.median(img)
lower = int(max(0, (1.0 - sigma) * v))
upper = int(min(255, (1.0 + sigma) * v))
edged = cv2.Canny(img, lower, upper)

cv2.imwrite("0010-001197-edged.png", edged)





gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# threshold to binary
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]

# apply morphology
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# find contours - write black over all small contours
letter = morph.copy()
cntrs = cv2.findContours(morph, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cntrs = cntrs[0] if len(cntrs) == 2 else cntrs[1]
for c in cntrs:
    area = cv2.contourArea(c)
    if area < 100:
        cv2.drawContours(letter,[c],0,(0,0,0),-1)
    cv2.imwrite("refined_image.png", letter)



#TODO: loop saving

def loopThroughFolder(imga):
    os.listdir(FOLDER_A)






#plt.subplot(121),plt.imshow(img),plt.title('Original')

#plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
#plt.xticks([]), plt.yticks([])
#plt.show()