class dog:
    def sound(self):
        print('bow bow')
class cat:
    def sound(self):
        print("meow")    
        
def makesound(animaltype):
    animaltype.sound()
    
cat1=cat() 
dog1=dog() 
makesound(cat1)
makesound(dog1)              