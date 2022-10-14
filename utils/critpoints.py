import numpy as np
import math

class CritPoints:
    @staticmethod
    def get_distance(x,y): #probably won't need this
        '''returns the distance between two points'''
        return math.dist(x,y)

    @staticmethod
    def get_distance(p1,p2,p3):
        '''returns the distance between a line drawn 
        by 1st 2 points and the 3rd point'''
        p1 = np.asarray(p1)
        p2 = np.asarray(p2)
        p3 = np.asarray(p3)
        return np.abs(np.linalg.norm(np.cross(p2-p1, p1-p3))/np.linalg.norm(p2-p1))
    
    @staticmethod
    def get_crit_points(points, step, cutoff):
        # For every point we need to 
            #find the number in the next progression
            #find the distance of every point to the line connection it 
            #select that point and back to one
            
        crit_points = [points[0]]
        index = 0
        print(len(points))
        while(index < len(points)):
            next_index = index+step
            if next_index >= len(points) :
                break
            for i in range(index, next_index):
                distance = CritPoints.get_distance( points[index], points[next_index], points[i])
                print(index, next_index, i)
                if cutoff < distance :
                    crit_points.append(points[i])
                    index = i
                    break
            index = next_index
        crit_points.append(points[-1])
        return crit_points
    