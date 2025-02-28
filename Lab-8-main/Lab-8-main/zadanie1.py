import cv2
from matplotlib import pyplot as plt

image = cv2.imread('variant-8.jpg')
height = image.shape[0]
width = image.shape[1]
new_image = image[height//2-200:height//2+200,width//2-200:width//2+200]
cv2.imwrite('new_variant-8.jpg', new_image)
