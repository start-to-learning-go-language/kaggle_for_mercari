import numpy as np
import matplotlib.pyplot as plt
import pickle
import os
import process_data as processer

if not os.path.exists('band'):
    print('no band')
else:
    if os.path.exists('data'):
        pass
    else:
        os.mkdir('data')

    image = []
    cell = []
    nucleus = []

    files = os.listdir('band/')

    for file in files:
        if '.bmp' in file:
            image_path = 'band/' + file
            cell_path = 'band/' + file.replace('.bmp', '.mask.0.png')
            nucleus_path = 'band/' + file.replace('.bmp', '.mask.1.png')

            image_array = processer.img_to_np(image_path)
            cell_array = processer.img_to_np(cell_path)
            nucleus_array = processer.img_to_np(nucleus_path)

            image.append(image_array)
            cell.append(cell_array)
            nucleus.append(nucleus_array)

        else:
            pass

    image = np.array(image)
    cell = np.array(cell)
    nucleus = np.array(nucleus)

    image = processer.rgb2gray_array(image)

    with open('data/image', 'wb') as f:
        pickle.dump(image, f)

    cell = cell[:, :, :, 0]
    nucleus = nucleus[:, :, :, 0]
    ncratio = []

    for i in range(len(cell)):
        cell_sum = np.sum(cell[i])
        nucleus_sum = np.sum(nucleus[i])
        ncratio.append(nucleus_sum / cell_sum)

    ncratio = np.array(ncratio)

    with open('data/cell', 'wb') as f:
        pickle.dump(cell, f)
    with open('data/nucleus', 'wb') as f:
        pickle.dump(nucleus, f)
    with open('data/ncratio', 'wb') as f:
        pickle.dump(ncratio, f)









































