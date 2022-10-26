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
    xs, ys = NearestPoint.seprate_xy(points)
    plt.plot(xs,ys)
    xs, ys = NearestPoint.seprate_xy(crit_points)
    plt.plot(xs,ys)
    plt.scatter(xs, ys)
    plt.show()
