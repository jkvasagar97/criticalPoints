class ArrangePoints:
    @staticmethod
    def nearest_point(center, points):
        points.sort(key = lambda K: (K[0] - center[0]) **2 + (K[1] - center[1])**2)
        return points[1]

    @staticmethod
    def switch_points():
        pass

    @staticmethod
    def arrange_points():
        pass
