class person:
    def display(self):
        
     print("hello")
p=person()
p.display()    


#to avoid self we use @staticmethod
class person:
    @staticmethod
    def display():
        
     print("hello")
p=person()
p.display()