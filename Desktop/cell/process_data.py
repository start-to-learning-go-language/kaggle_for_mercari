import numpy as np
import matplotlib.pyplot as plt
import pickle
import os

#画像をnumpyのarrayとして取得して返す。
def img_to_np(img_path):
	img = plt.imread(img_path)
	return img

#指定したサイズになるようにinput_arrayの真ん中を切り取って返す。output_shapeはtupleかlistで。
#U-Netのup-convolutionで使う。
def rescale(input_array, output_shape):
	i = len(input_array.shape)
	y, x = input_array.shape[i-3], input_array.shape[i-2]
	y_, x_ = output_shape[0], output_shape[1]
	y_start = (y - y_) // 2
	x_start = (x - x_) // 2
	if len(input_array.shape) == 3:
		return input_array[y_start: y_start + y_, x_start: x_start + x_, :]
	elif len(input_array.shape) == 2:
		return input_array[y_start: y_start + y_, x_start: x_start + x_]
	else:
		return input_array[:, y_start: y_start + y_, x_start: x_start + x_, :]

#画像のarrayをロードする。
def load_array(name):
	with open(name, 'rb') as f:
		x = pickle.load(f)
		return x

#画像のarrayを保存する。
def save_array(z, name):
	with open(name, 'wb') as f:
		pickle.dump(z, f)

#画像をグレースケールに変換。
def rgb2gray(rgb):
	return np.dot(rgb, [0.299, 0.587, 0.114])

#まとめてグレースケールに変換。
def rgb2gray_array(rgb_array):
	l = []
	for x in rgb_array:
		x_ = rgb2gray(x)
		l.append(x_)
	return np.array(l)

#画像をarrayとして取得して、保存する。既に保存してあったら、必要ない。
def image_to_array_file():
	x = []
	y_ = []
	y__ = []
	for i in range(10):
		tmp_x = img_to_np('band/' + str(i) + '.bmp')
		tmp_y_ = img_to_np('band/' + str(i) + '.0.png')
		tmp_y__ = img_to_np('band/' + str(i) + '.1.png')
		x.append(tmp_x)
		y_.append(tmp_y_)
		y__.append(tmp_y__)

	x = np.array(x)
	y_ = np.array(y_)
	y__ = np.array(y__)

	gray_x = rgb2gray_array(x)
	gray_y_ = rgb2gray_array(y_)
	gray_y__ = rgb2gray_array(y__)

	try:
		os.mkdir('band_bin')
	except:
		pass

	save_array(x, 'x')
	save_array(y_, 'y_')
	save_array(y__, 'y__')
	save_array(gray_x, 'gray_x')
	save_array(gray_y_, 'gray_y_')
	save_array(gray_y__, 'gray_y__')

#折りたたんで拡張。
def replicate(input_array, h_or_v, m):
    n = input_array.shape[0]
    a = np.identity(n)
    if h_or_v == 'h':
        a = np.hstack((a[:,:m][:,::-1],a,a[:,n-m:][:,::-1]))
        return np.dot(input_array, a)
    elif h_or_v == 'v':
        a = np.vstack((a[:m,:][::-1,:],a,a[n-m:,:][::-1,:]))
        return np.dot(a, input_array)
    else:
        print('put "h" or "v" as 2nd parameter')

#ミラーリング
def mirror(input_array, output_size):
    n = input_array.shape[0]
    m = (output_size - n) // 2
    input_array = replicate(input_array, 'h', m)
    input_array = replicate(input_array, 'v', m)
    return input_array

#nc比を計算する。
def n_c_ratio(n,c):
	n_size = len(np.where(n!=0)[0])
	c_size = len(np.where(c!=0)[0])
	return n_size / c_size

'''
gray_c = load_array('gray_y_')
gray_n = load_array('gray_y__')

n_c_ratio_list = []

for i in range(10):
	ratio = n_c_ratio(gray_n[i], gray_c[i])
	ratio = (ratio // 0.01)
	n_c_ratio_list.append(ratio)

l = []

for x in n_c_ratio_list:
	tmp = [0.]*100
	tmp[int(x)] += 1.
	l.append(tmp)
	print(tmp)

l = np.array(l)

with open('data/ncratio','wb') as f:
	pickle.dump(l, f)



with open('band_bin/ncratio', 'rb') as f:
	l = pickle.load(f)

print(l)
'''

















