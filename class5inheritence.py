class animal:
    def eat(self):
        print("eating")
class dog(animal):
    def bark(self):
        print("bark")
d=dog()
d.eat()                
d.bark()


#another one
class animal1:
    def __init__(self,name):
        self.name=name
class dog(animal1):
    def display(self):
        print(self.name)
d=dog("babydog")                
d.display()