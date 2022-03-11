
import cv2
import numpy as np
from PIL import ImageDraw
from PIL import Image

full_path = r'C:\Users\ngcc\PycharmProjects\python_lib_test\img\냥.jpg'
img = Image.open(full_path)

pixel = (100, 50, 90)
for i in range(1, img.height):
    img.putpixel((1, i), pixel)
    img.putpixel((2, i), pixel)
    img.putpixel((3, i), pixel)
    img.putpixel((4, i), pixel)
    img.putpixel((i, img.height-1), pixel)

for i in range(1, img.width):
    img.putpixel((1, i), pixel)
    img.putpixel((2, i), pixel)
    img.putpixel((3, i), pixel)
    img.putpixel((4, i), pixel)
    img.putpixel((img.width-1, i), pixel)
img.save("2.jpg")



cv2.imshow('sample2',img)
cv2.waitKey()
cv2.destroyAllWindows()

x, h, w, y = 80, 90, 100, 105
img_small2 = img.resize((300, 300))
draw = ImageDraw.Draw(img_small2)
draw.line([(x+30, y), (x-10, y+h), (x+w-20, y+h+50), (x+w+40, y+47), (x+30, y)], fill="red", width=2)

img_small2
