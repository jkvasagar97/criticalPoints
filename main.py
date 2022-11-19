from PIL import Image, ImageOps
from utils.critpoints import CritPoints as crit
import matplotlib.pyplot as plt
from utils.nearestpoint import arrange_points
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

    start = time.time()
    #finding the critical points using peasewise linearization
    mother_shape = crit.get_crit_points(arranged_points,4,0.4)
    end = time.time()

    print("Crit points :", (end-start) * 10**3, "ms")
    print("Length of crit points", len(mother_shape))
    
    #Generating variations of mother shaape
    

    #ploting both the curves
    xs = [x[0] for x in mother_shape]
    ys = [x[1] for x in mother_shape]

    x1 = [x[0] for x in arranged_points]
    y1 = [x[1] for x in arranged_points]

    plt.plot(x1,y1)
    plt.plot(xs,ys)

    plt.show()
