import numpy as np

def add_noise(default_shape, no_of_variation):

    noises = np.random.normal(0, 1, (no_of_variation, default_shape.shape[0]))

    #Adding noise to default shape to generate variations
    variation = np.copy(default_shape)
    for noise in noises:
        variation = np.row_stack((variation, np.add(default_shape, noise)))
        
    return variation[1:]