import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pickle

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

x = load_array('x')

print(x.shape)













