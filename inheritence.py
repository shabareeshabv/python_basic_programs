class new:
    def display(self):
        print("this is new ")
class new1(new):
    def printing(self):
        print("derived class")  
class new2(new1):
    def show(self):
        print("nothing")
p=new2()
p.show()
p.printing()                      
p.display()
p1=new1()
p1.display()