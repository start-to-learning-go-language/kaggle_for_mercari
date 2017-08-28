import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pickle
import os

def img_to_np(img_path):
	img = plt.imread(img_path)
	return img

def rescale(input_array, output_shape):
	y, x = input_array.shape[0], input_array.shape[1]
	y_, x_ = output_shape[0], output_shape[1]
	y_start = (y - y_) // 2
	x_start = (x - x_) // 2
	return input_array[y_start: y_start + y_, x_start: x_start + x_, :]

def load_array(name):
	with open('band_bin/' + name, 'rb') as f:
		x = pickle.load(f)
		return x

def save_array(z, name):
	with open('band_bin/' + name, 'wb') as f:
		pickle.dump(z, f)

def image_to_array_file():
	x = []
	y_ = []
	y__ = []
	for i in range(10):
		tmp_x = rescale(img_to_np('band/' + str(i) + '.bmp'), (348,348))
		tmp_y_ = rescale(img_to_np('band/' + str(i) + '.0.png'), (348,348))
		tmp_y__ = rescale(img_to_np('band/' + str(i) + '.1.png'), (348,348))
		x.append(tmp_x)
		y_.append(tmp_y_)
		y__.append(tmp_y__)

	x = np.array(x)
	y_ = np.array(y_)
	y__ = np.array(y__)

	try:
		os.mkdir('band_bin')
	except:
		pass

	save_array(x, 'x')
	save_array(y_, 'y_')
	save_array(y__, 'y__')

x = load_array('x')
y_ = load_array('y_')
y__ = load_array('y__')

print(x.shape)
print(y_.shape)
print(y__.shape)
























