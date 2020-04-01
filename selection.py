import os
import random

from shutil import move

os.makedirs('dataset/train/car', exist_ok=True)
os.makedirs('dataset/train/normal', exist_ok=True)
os.makedirs('dataset/train/person', exist_ok=True)
os.makedirs('dataset/train/black', exist_ok=True)

os.makedirs('dataset/validation/car', exist_ok=True)
os.makedirs('dataset/validation/normal', exist_ok=True)
os.makedirs('dataset/validation/person', exist_ok=True)
os.makedirs('dataset/validation/black', exist_ok=True)

files = os.listdir('dataset/car')
file_count = len(files)
counter = 1

for file in files:
	if random.randint(1, 100) <= 80:
		move('dataset/car/'+file, 'dataset/train/car/'+file)
	else:
		move('dataset/car/'+file, 'dataset/validation/car/'+file)
	print('Moving car ' + str(counter) + ' of ' + str(file_count))
	counter += 1

files = os.listdir('dataset/normal')
file_count = len(files)
counter = 1
for file in files:
	if random.randint(1, 100) <= 80:
		move('dataset/normal/'+file, 'dataset/train/normal/'+file)
	else:
		move('dataset/normal/'+file, 'dataset/validation/normal/'+file)
	print('Moving normal ' + str(counter) + ' of ' + str(file_count))
	counter += 1
	
files = os.listdir('dataset/person')
file_count = len(files)
counter = 1
for file in files:
	if random.randint(1, 100) <= 80:
		move('dataset/person/'+file, 'dataset/train/person/'+file)
	else:
		move('dataset/person/'+file, 'dataset/validation/person/'+file)
	print('Moving person ' + str(counter) + ' of ' + str(file_count))
	counter += 1
	
files = os.listdir('dataset/black')
file_count = len(files)
counter = 1
for file in files:
	if random.randint(1, 100) <= 80:
		move('dataset/black/'+file, 'dataset/train/black/'+file)
	else:
		move('dataset/black/'+file, 'dataset/validation/black/'+file)
	print('Moving black ' + str(counter) + ' of ' + str(file_count))
	counter += 1