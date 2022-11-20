from utils.critpoints import CritPoints as crit
from utils.noise import add_noise
from utils.nearestpoint import arrange_points
from utils.shape_modeling import get_cutoff_vector_and_val, get_random_scale_vals, get_mean_shape
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np
import time
import numpy as np

if __name__ == '__main__':
    
    img_raw = Image.open('data/eli.jpeg')
    img_raw = ImageOps.grayscale(img_raw)
    img_raw = np.asarray(img_raw)

    print("Processing Image")
    
    img = np.zeros(img_raw.shape)

    start = time.time()

    #Converting the matrix into a 1, 0 matrix to get countur points
    for i, row in enumerate(img_raw):
        for j, pixel in enumerate(row):
            if pixel < 20:
                img[i][j] = 1

    end = time.time()
    
    points = np.nonzero(img)

    print("Processing Image to matrix:", (end-start) * 10**3, "ms")
    print('Length of points:', len(points[0]))
    
    #referance point to start the arranging of contour points
    ref_point = (points[0][len(points[0]) - 1], points[1][len(points[0]) - 1])
    print('Starting point:', ref_point)

    start = time.time()
    arranged_points = arrange_points(img, ref_point)
    end = time.time()

    print('Length of arranged points:', len(arranged_points))
    print("Sorting points: ", (end-start) * 10**3, "ms")

    #finding the critical points using peasewise linearization
    start = time.time()
    mother_shape = crit.get_crit_points(arranged_points,4,0.4)
    end = time.time()

    print("Crit points :", (end-start) * 10**3, "ms")
    print("Length of crit points", len(mother_shape))

    #flatening to make a column vector
    mother_shape = np.reshape(mother_shape, len(mother_shape)*2, order='F')
    
    #Adding noise to mother shaape
    variations = add_noise(mother_shape, 50)
    variations = np.transpose(variations)

    #Generating Mean shape
    mother_shape = get_mean_shape(variations)

    #finding covariance matrix
    cov_matrix = np.cov(variations)

    #finding eigen values of covariance matrix
    eig_val, eig_vector = np.linalg.eigh(cov_matrix)
    
    #reversing because they are ordered in ascending
    eig_vector = eig_vector[::-1]
    eig_val = eig_val[::-1]
    
    p_matrix, b_scale = get_cutoff_vector_and_val(eig_val, eig_vector, 0.99)

    random_shapes = [mother_shape]
    # Generating ten random similar shapes
    for i in range(8):
        #get randomised value for b
        temp = get_random_scale_vals(b_scale)
        #X = mean(X) + Pb
        x = mother_shape + np.matmul(temp, p_matrix)
        random_shapes.append(x)

    #plotting the graphs
    figure, axis = plt.subplots(3, 3)
    no_of_points = int(mother_shape.shape[0]/2)
    for index, x in enumerate(random_shapes):
        if index == 0:
            axis[0, 0].set_title("Mean Shape")
        else:
            axis[int(index/3), index%3].set_title("Generated Shape {}".format(index))
        axis[int(index/3), index%3].plot(x[:no_of_points], x[no_of_points:])
        axis[int(index/3), index%3].axis('off')
    
    plt.show()
