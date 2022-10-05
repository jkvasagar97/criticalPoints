#Generating data to plot
from ast import main
import mailbox
import numpy as np
import random
import matplotlib.pyplot as plt
import math

class Polynomial:
    def __init__(self, poly ):
        self.poly = []
        self.x = []
        self.y = []
        self.poly = poly
        self.length = len(self.poly)
            
    def find_val(self, x: int):
        '''
        returs value of the ponynomial at a given x
        '''
        result = 0
        for i,co in enumerate(self.poly):
            result += co * pow(x, self.length - i - 1)
        return result
    
    def sample(self, start, end, number):
        """
        returns a list of points sampled from the polynomial
        """
        if start >= end:
            exit(-1)
        interval = (end - start)/ number
        while start <= end:
            self.x.append(start)
            self.y.append(self.find_val(start))
            start += interval
        return self.x, self.y

def get_distance(x,y): #probably won't need this
    '''returns the distance between two points'''
    return math.dist(x,y)

def get_distance(p1,p2,p3):
    '''returns the distance between a line drawn 
    by 1st 2 points and the 3rd point'''
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)
    p3 = np.asarray(p3)
    return np.linalg.norm(np.cross(p2-p1, p1-p3))/np.linalg.norm(p2-p1)
    
def get_crit_points(x,y, boost_factor, cutoff):
    # For every point we need to 
        #find the number in the next progression
        #find the distance of every point to the line connection it 
        #select that point and back to one
        
    crit_x = [x[0]]
    crit_y = [y[0]]
    index = 0
    while(index <= len(x)):
        next_index = index+boost_factor
        if next_index > len(x) - 1:
            break
        for i in range(index, next_index+1):
            distance = get_distance( [x[index],y[index]], [x[next_index],y[next_index]], [x[i],y[i]])
            if cutoff < distance :
                crit_x.append((x[i]))
                crit_y.append(y[i])
                index = i
                break
        index = next_index
    crit_x.append(x[-1])
    crit_y.append(y[-1])
    return crit_x, crit_y
    
if __name__ == '__main__':
    poly_curve = Polynomial([1,0,0,-1000])
    x,y = poly_curve.sample(-20,20,30)
    x_crit,y_crit = get_crit_points(x,y,2,0.05)
    plt.plot(x,y)
    plt.plot(x_crit,y_crit)
    plt.scatter(x_crit, y_crit)
    print(len(x))
    print(len(x_crit))
    plt.show()
