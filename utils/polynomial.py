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
