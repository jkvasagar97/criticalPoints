import utils.polynomial as pl
from utils.critpoints import CritPoints as crit
import matplotlib.pyplot as plt
from utils.arrangepoints import ArrangePoints

def seprate_xy(points):
    xs = [x[0] for x in points]
    ys = [x[1] for x in points]
    return xs, ys

if __name__ == '__main__':
    poly_curve = pl.Polynomial([1,-2,100])
    points = poly_curve.sample(-20,20,100)
    crit_points = crit.get_crit_points(points,2,0.0001)
    print(len(points))
    print(len(crit_points))
    xs, ys = seprate_xy(points)
    plt.plot(xs,ys)
    xs, ys = seprate_xy(crit_points)
    plt.plot(xs,ys)
    plt.scatter(xs, ys)
    plt.show()