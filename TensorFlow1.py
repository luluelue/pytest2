# this is tensorflow

import pickle
import numpy as np
import os

CIFAR_DIR = "F:\pydata\cifar-10-batches-py"
print(os.listdir(CIFAR_DIR))

with open(os.path.join(CIFAR_DIR, "data_batch_1"), 'rb') as f:
    data = pickle.load(f, encoding='bytes')
    print(type(data))
    print(data.keys())
    print(data[b'data'].shape)

    print(data[b'labels'])
    print(data[b'batch_label'])
    print(data[b'filenames'])

    image_arr = data[b'data'][100]
    image_arr = image_arr.reshape(3, 32, 32)
    image_arr = image_arr.transpose(1, 2, 0)
    # import matplotlib.pyplot as plt
    from matplotlib.pyplot import imshow
    import pylab

    imshow(image_arr)
    pylab.show()
