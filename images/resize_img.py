# Resize images to set resolution
# pip install opencv-python
import cv2
import os

imgs = os.listdir("img")
new_resolution = (300, 200)
# print(imgs)
for img in imgs:
    image = cv2.imread("img/" + img)
    resized_image = cv2.resize(image, new_resolution, interpolation=cv2.INTER_LINEAR)
    cv2.imwrite("img_resized/" + img, resized_image)
