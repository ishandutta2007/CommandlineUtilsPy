from PIL import Image
import numpy as np
import cv2
import sys
import argparse

argv = sys.argv[1:]
source_file = argv[0]
dest_file = argv[1]


img = Image.open(source_file)
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save(dest_file, "PNG")


