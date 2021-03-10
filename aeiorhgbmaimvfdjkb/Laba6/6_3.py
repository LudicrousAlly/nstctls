import numpy as np
from PIL import Image
from tifffile import imsave


im = Image.open('tiff.tiff')
imarray = np.array(im)

third = []

for i in range(len(imarray)):
    third.append([0]*len(imarray[i]))
    for j in range(len(imarray[i])):
        third[i][j] = [0]*3

for i in range(len(imarray)):
    for j in range(len(imarray[i])):
        with np.errstate(divide='ignore'):
            third[i][j][0] = (abs(imarray[i][j][1] - imarray[i][j][2])*255//abs(imarray[i][j][1] + imarray[i][j][2]))

        third[i][j][1] = 0
        third[i][j][2] = 0

third = np.array(third, dtype='Int32')


thirdchannel = Image.fromarray(third.astype('uint8'))

imsave('result.tif', third.astype('uint8'))

thirdchannel.show()

im.show()