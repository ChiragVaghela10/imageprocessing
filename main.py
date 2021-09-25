from skimage import color, io
import matplotlib.pyplot as plt

from utilities import *


img = io.imread('img/Lenna.png')
img = color.rgb2gray(img)
mat = np.array([
        # [1, 1, 1, 1, 1],
        # [1, 1, 1, 1, 1],
        # [1, 1, 1, 1, 1],
        # [1, 1, 1, 1, 1],
        # [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ])

final_img = convolution(img, mat)
plt.imshow(final_img).set_cmap('gray')

# comment out line above and uncomment this to see original image
# plt.imshow(img).set_cmap('gray')
plt.show()
