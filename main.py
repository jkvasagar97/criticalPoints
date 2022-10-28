import utils.polynomial as pl
from utils.critpoints import CritPoints as crit
import matplotlib.pyplot as plt
from utils.nearestpoint import NearestPoint
import numpy as np
import time

if __name__ == '__main__':

    points = np.genfromtxt('data/ellipse.csv', delimiter=',', dtype=None)

    #shuffling the arraged point in random
    np.random.shuffle(points)

    points = points.tolist()

    start = time.time()
    #arrangin the points using nearest neighbour 
    points = NearestPoint.arrange_points(points)
    end = time.time()

    print("Sorting :", (end-start) * 10**3, "ms")

    start = time.time()
    #finding the critical points using peasewise linearization
    crit_points = crit.get_crit_points(points,10,0.0001)
    
    end = time.time()
    print("Crit points :", (end-start) * 10**3, "ms")


    print(len(points))
    print(len(crit_points))
    
    #ploting both the curves
    x1, y1 = NearestPoint.seprate_xy(points)
    x2, y2 = NearestPoint.seprate_xy(crit_points)
    fig, ax = plt.subplots(2, 1, figsize=(13, 7), sharex=True, sharey=True)
    fig.suptitle('Selecting critical points for an ellipse', size=18)
    ax[0].set_aspect('equal')
    ax[1].set_aspect('equal')
    ax[0].scatter(x1, y1, marker="+", alpha=0.5, color="forestgreen")
    ax[1].scatter(x2, y2, marker="+", alpha=0.5, color="crimson")
    ax[0].set_title("All points representing the ellipse")
    ax[1].set_title("Only critical points to represent the ellipse")
    plt.plot(x1,y1)
    plt.show()
