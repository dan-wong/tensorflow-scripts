import sys
import os
import PIL.Image as Image
import numpy as np
import tensorflow as tf
from shutil import move

IMAGE_SHAPE = (250, 250)

def classify_image(dir_path):
	model = tf.keras.models.load_model('trained_model.h5')

	files = os.listdir(dir_path)
	file_count = str(len(files))
	counter = 1

	os.makedirs(dir_path+'/car', exist_ok=True)
	os.makedirs(dir_path+'/normal', exist_ok=True)
	os.makedirs(dir_path+'/person', exist_ok=True)
	os.makedirs(dir_path+'/black', exist_ok=True)
	
	for file in files:
		if (os.path.isdir(file)):
			continue
		image = Image.open(dir_path+'/'+file).resize(IMAGE_SHAPE)
		image = np.array(image)/255.0
		result = model.predict(image[np.newaxis, ...])
		
		print(result)
		#if (result[0] < 0.3):
		#	move(dir_path+'/'+file, dir_path+'/interesting/'+file)
		#	print(str(counter) + '/' + file_count + ' - ' + file + ' is interesting')
		#else:
		#	move(dir_path+'/'+file, dir_path+'/normal/'+file)
		#	print(str(counter) + '/' + file_count + ' - ' + file + ' is normal')
		#counter += 1
	
def main():
    classify_image(sys.argv[1])
	
if __name__ == '__main__':
    main()