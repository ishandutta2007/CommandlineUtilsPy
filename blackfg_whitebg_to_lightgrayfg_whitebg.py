
import numpy as np
import cv2
 
im = cv2.imread('logoonly_squarefit_blackfg_whitebg.png')
im[np.where((im == [0,0,0]).all(axis = 2))] = [211,211,211]
cv2.imwrite('logoonly_squarefit_lightgrayfg_whitebg.png', im)

