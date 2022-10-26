import utils.polynomial as pl
from utils.critpoints import CritPoints as crit
import matplotlib.pyplot as plt
from utils.nearestpoint import NearestPoint


if __name__ == '__main__':
    poly_curve = pl.Polynomial([4,0,-0])
    points = poly_curve.sample(-2,2,50)
    points = NearestPoint.arrange_points(points)
    crit_points = crit.get_crit_points(points,2,0.001)
    print(len(points))
    print(len(crit_points))
    xs, ys = NearestPoint.seprate_xy(points)
    plt.plot(xs,ys)
    xs, ys = NearestPoint.seprate_xy(crit_points)
    plt.plot(xs,ys)
    plt.scatter(xs, ys)
    plt.show()
