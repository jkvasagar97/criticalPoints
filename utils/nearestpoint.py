from array import array
import math

class NearestPoint:
    @staticmethod
    def is_same_points(p1,p2):
        print(p1, p2)
        return p1[0] == p2[0] and p1[1] == p2[1]

    @staticmethod
    def is_in_proximity(center, point, eps, disctance_cal):
        if (disctance_cal(center, point) > eps):
            return False
        return True

    @staticmethod
    def manhattan_distance(p1,p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    @staticmethod
    def eqi_distance(p1,p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    @staticmethod
    def nearest_point(center, points):
        '''
        For every point we will check if it is in the near proximity of center
        '''
        distance = 1
        while(True):
            for i, point in enumerate(points):
                if not NearestPoint.is_same_points(center,point):
                    if NearestPoint.is_in_proximity(center, point, distance, NearestPoint.eqi_distance):
                        return i
            distance += 1
                    
    @staticmethod
    def arrange_points(points):
        temp = points.copy()
        arranged_array=[]
        next_point = temp.pop(0)
        while len(temp) > 0:
            arranged_array.append(next_point)           
            next_index = NearestPoint.nearest_point(next_point, temp)
            next_point = temp.pop(next_index)
        return arranged_array