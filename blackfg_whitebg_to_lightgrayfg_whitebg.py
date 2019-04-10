
import numpy as np
import cv2

argv = sys.argv[1:]
source_file = argv[0]
dest_file = argv[1]

im = cv2.imread(source_file)
im[np.where((im == [0,0,0]).all(axis = 2))] = [211,211,211]
cv2.imwrite(dest_file, im)


