
import numpy as np
import cv2
 
im = cv2.imread('logoonly_squarefit_black_whitebg.png')
im[np.where((im == [0,0,0]).all(axis = 2))] = [128, 128, 128]
cv2.imwrite('logoonly_squarefit_darkgray_whitebg.png', im)
