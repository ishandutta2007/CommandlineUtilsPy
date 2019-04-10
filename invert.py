
import numpy as np
import sys
import cv2

argv = sys.argv[1:]
source_file = argv[0]
dest_file = argv[1]

im = cv2.imread(source_file)
im = (255-im)
cv2.imwrite(dest_file, im)

