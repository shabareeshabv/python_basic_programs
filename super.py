#super function used to give access to the methods of a parent class
class Rect:
    def __init__(self,length,width):
        self.length=length
        self.width=width
class Square(Rect): 
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length * self.width 
        
class Cube(Rect): 
    def __init__(self,length,width,height):
        super().__init__(length,width) 
        self.height=height       

    def volume(self):
        return self.length*self.width*self.height
square=Square(3, 3) 
cube=Cube(3, 3, 3) 
print(square.area())
print(cube.volume())