from skimage import io
import matplotlib.pyplot as plt

image = io.imread('C:\\Users\\ilyat\\Desktop\\University\\Python\\Laba6\\tiff.tiff')
plt.hist(image[:, :, 0].ravel(), bins = 256, color = 'red', alpha = 0.5)
plt.hist(image[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
plt.hist(image[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5)
plt.xlabel('Intensity Value')
plt.ylabel('Count')
plt.ylim(0, 60000)
plt.xlim(0, 255)
plt.legend(['Red Channel', 'Green Channel', 'Blue Channel'])
plt.show()