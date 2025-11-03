class shape:
    def area(self):
        return 0
    
class rectangle(shape):
    def area(self):
        lenght = 5
        width = 3
        return lenght*width
    
class cirlce(shape):
    def area(self):
        radius = 4
        return 3.14 * radius * radius
    
shapes = [rectangle(),cirlce()]
for s in shapes:
    print("Area: ",s.area())