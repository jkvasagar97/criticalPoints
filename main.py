import utils.polynomial as pl
from utils.critpoints import CritPoints as crit
import matplotlib.pyplot as plt
from utils.nearestpoint import NearestPoint
import numpy as np


if __name__ == '__main__':

#    poly_curve = pl.Polynomial([1,0,-7,6])
#    points = poly_curve.sample(-4,4,100)
    points = np.genfromtxt('ellipse.csv', delimiter=',', dtype=None)
    points = points.tolist()
    points = NearestPoint.arrange_points(points)
    crit_points = crit.get_crit_points(points,10,0.0001)
    print(len(points))
    print(len(crit_points))
    
    #ploting both the curves
    x1, y1 = NearestPoint.seprate_xy(points)
    x2, y2 = NearestPoint.seprate_xy(crit_points)
    fig, ax = plt.subplots(2, 1, figsize=(13, 7), sharex=True, sharey=True)
    fig.suptitle('Selecting critical points for an ellipse', size=18)
    ax[0].set_aspect('equal')
    ax[1].set_aspect('equal')
    ax[0].scatter(x1, y1, marker="+", alpha=0.5, color="crimson")
    ax[1].scatter(x2, y2, marker="+", alpha=0.5, color="forestgreen")
    ax[0].set_title("All points representing the ellipse")
    ax[1].set_title("Only critical points to represent the ellipse")
    plt.show()
