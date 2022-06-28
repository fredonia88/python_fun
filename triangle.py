class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        x = float(x)
        y = float(y)
        x = self.getx() - x
        y = self.gety() - y
        
        return math.hypot(x, y)
        
    def distance_from_point(self, point):
        x = float(point._Point__x)
        y = float(point._Point__y)
        x = self.getx() - x
        y = self.gety() - y
        
        return math.hypot(x, y)

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3

    def perimeter(self):
        d1 = self.vertice1.distance_from_point(self.vertice2) 
        d2 = self.vertice2.distance_from_point(self.vertice3)
        d3 = self.vertice3.distance_from_point(self.vertice1)
        
        return d1 + d2 + d3

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
