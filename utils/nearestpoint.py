import math

class NearestPoint:
    @staticmethod
    def seprate_xy(points):
        xs = [x[0] for x in points]
        ys = [x[1] for x in points]
        return xs, ys

    @staticmethod
    def is_same_points(p1,p2):
        return p1[0] == p2[0] and p1[1] == p2[1]

    @staticmethod
    def eqi_distance(p1,p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    @staticmethod
    def is_in_proximity(center, point, eps):
        if (NearestPoint.eqi_distance(center, point)  < eps):
            return True
        return False

    @staticmethod
    def next_point(center, points):
        '''
        For every point we will check if it is in the near proximity of center
        '''
        neighbour_distance = 0.0001
        while(True):
            for point in points:
                if NearestPoint.is_same_points(center, point):
                    continue
                if NearestPoint.is_in_proximity(center, point, neighbour_distance):
                    return point
            neighbour_distance = neighbour_distance + 0.0001

    @staticmethod 
    def find_referance_point (points):
        """
        To find the starting point to arrange
        """
        xs,ys = NearestPoint.seprate_xy(points)
        left_most_index = xs.index(min(xs))
        return [xs[left_most_index], ys[left_most_index]]


    @staticmethod
    def arrange_points(points):
        temp = points.copy()
        arranged_array=[]
        next_point = NearestPoint.find_referance_point(points)
        temp.pop(temp.index(next_point))
        while len(temp) > 0:
            arranged_array.append(next_point)           
            next_point = NearestPoint.next_point(next_point, temp)
            temp.pop(temp.index(next_point))
        return arranged_array