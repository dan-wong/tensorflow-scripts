import os
import cv2

from shutil import move

os.makedirs('dataset/normal', exist_ok=True)
os.makedirs('dataset/car', exist_ok=True)
os.makedirs('dataset/person', exist_ok=True)
os.makedirs('dataset/black', exist_ok=True)

def showImageAndReadResult(file):
	img = cv2.imread(file, 1)
	imgSmall = cv2.resize(img, (1000, 751))
	cv2.imshow('image', imgSmall)
	key = cv2.waitKey(0)
	cv2.destroyAllWindows()
	return key

files = os.listdir()
for file in files:
	if str(os.path.splitext(file)[1]) == '.jpg':
		key = showImageAndReadResult(file)
		if key == 49: # 1 - normal
			move(file, 'dataset/normal/' + file)
		elif key == 50: # 2 - car
			move(file, 'dataset/car/' + file)
		elif key == 51: # 3 - person
			move(file, 'dataset/person/' + file)
		elif key == 48: # 0 - black
			move(file, 'dataset/black/' + file)
		
