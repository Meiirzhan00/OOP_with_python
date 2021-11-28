class Shape():
    def __init__(self):
        print('Shape created')
    def draw(self):
        print('Drawing shape')
    def area(self):
        print('Calc area')
    def perometer(self):
        print('Calc perimeter')

class Rectange(Shape):
    def __init__(self, width, height):
        Shape.__init__(self)
        self.width = width
        self.height = height

        print('Rectangle created')

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*(self.width+self.height)

    def draw(self):
        print(f'Drawing rectangle with width = {self.width} and height = {self.height}')

rect = Rectange(10,15)
#
# print(rect.area())
# print(rect.perimeter())
# print(rect.draw())

class Triangle(Shape):
    def __init__(self, a, b, c):
        Shape.__init__(self)

        self.a = a
        self.b = b
        self.c = c
        print('Triangle created')

    def draw(self):
        print(f'Drawing triangle with sides = {self.a}, {self.b}, {self.c}')

    def area(self):
        s = (self.a + self.b + self.c)/2
        return math.sqrt(s*(s - self.a)*(s - self.b)*(s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

triangle = Triangle(10,12,14)

# triangle.draw()
# print(triangle.area())
# print(triangle.perimeter())

for shape in [rect,triangle]:
    shape.draw()
