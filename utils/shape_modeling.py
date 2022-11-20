import numpy as np

def rand_float_range(start, end):
    return np.random.random() * (end - start) + start

def get_mean_shape(variations):
    return variations.sum(axis=1)/variations.shape[1]

def get_cutoff_vector_and_val(eig_val, eig_vector, cuttoff):
    total = np.sum(eig_val)
    sum_val = 0

    for i, val in enumerate(eig_val):
        sum_val = sum_val + val
        if(sum_val/total > cuttoff):
            break
    
    return eig_vector[:i], eig_val[:i]

def get_random_scale_vals(eig_val):
    temp = np.zeros(eig_val.shape)
    for index, val in enumerate(eig_val):
        start = 3.0 * (val ** 0.5)
        temp[index] = rand_float_range(start, -1 * start)

    return temp
