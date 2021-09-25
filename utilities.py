import numpy as np


def convolution(original_img, kernel):
    """
    Funtion to convolute kernel on a given image

    :param original_img: original image provided by user
    :param kernel: kernel of 3X3, 5X5, 7X7
    :return: result: resulting image obtained by convolution of kernel on original image
    """
    edges = int(kernel.shape[0] / 2)
    new_img = np.zeros((original_img.shape[0] + edges + 1, original_img.shape[1] + edges + 1))
    new_img[edges:new_img.shape[0] - 1, edges:new_img.shape[1] - 1] = original_img
    result = np.zeros(new_img.shape)

    for m in np.arange(edges, new_img.shape[0] - edges):
        for n in np.arange(edges, new_img.shape[1] - edges):
            curr_region = new_img[m - edges:m + edges + 1, n - edges:n + edges + 1]
            curr_result = curr_region * kernel
            score = np.sum(curr_result)
            result[m, n] = score * (1 / np.sum(kernel))

    return result[edges:result.shape[0] - edges, edges:result.shape[1] - edges]
