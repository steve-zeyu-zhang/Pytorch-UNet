import cv2
import numpy as np
import os
def To3(path):
	files = os.listdir(path)
	for file in files:
		img = cv2.imread(path+file)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		img2 = np.zeros_like(img)
		img2[:,:,0] = gray
		img2[:,:,1] = gray
		img2[:,:,2] = gray
		print(file)
		cv2.imwrite(path+file, img2)

To3(r'/home/abc/Pytorch-UNet/test_img/')
