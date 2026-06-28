class Area_shapes:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def rectangle_area(self):
        return self.length * self.breadth
    
    def square_area(self):
        return self.length**2
    

a1 = Area_shapes(10, 20)
print(a1.rectangle_area())

a2 = Area_shapes(2 , 20)
print(a2.rectangle_area())

a2_1 = Area_shapes(2,2)
print(a2_1.square_area())
