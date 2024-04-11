# Convert JPG files to PNG
# pip install opencv-python
import cv2
import os

imgs = os.listdir("img")
# print(imgs)
for img in imgs:
    # get name
    img_name = img[:-4]
    image = cv2.imread("img/" + img_name + ".jpg", 1)
    cv2.imwrite("img_png/" + img_name + ".png", image)
