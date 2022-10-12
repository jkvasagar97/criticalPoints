import utils.polynomial as pl
from utils.critpoints import CritPoints as crit
import matplotlib.pyplot as plt

if __name__ == '__main__':
    poly_curve = pl.Polynomial([1,0,1,-1000])
    x,y = poly_curve.sample(-20,20,60)
    x_crit,y_crit = crit.get_crit_points(x,y,5,0.1)
    plt.plot(x,y)
    plt.plot(x_crit,y_crit)
    plt.scatter(x_crit, y_crit)
    print(len(x))
    print(len(x_crit))
    plt.show()
