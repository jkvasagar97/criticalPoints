import numpy as np

def add_noise(default_shape, no_of_variation):
    noise_shape = no_of_variation, default_shape.shape[0], default_shape.shape[1]
    variation = np.zeros(noise_shape)
    noises = np.random.normal(0, 1, noise_shape)

    #Adding noise to default shape to generate variations
    for i, noise in enumerate(noises):
        variation[i] = np.add(default_shape, noise)

    return variation