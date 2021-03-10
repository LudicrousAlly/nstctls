import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import matplotlib.cbook as cbook

with cbook.get_sample_data('C:\\Users\\ilyat\\Desktop\\University\\Python\\Laba5\\qwe.jpeg') as image_file:
    image = mpimg.imread(image_file)

fig, ax = plt.subplots()
fig1, ax1 = plt.subplots()

ax.imshow(image)

grayscale = np.dot(image[..., :3], [0.299, 0.587, 0.114])

ax1.imshow(grayscale, cmap=plt.get_cmap("gray"))

plt.show()