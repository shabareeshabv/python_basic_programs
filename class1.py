#class person:
 #   def name(self):
        
  #      print("helooo")
#person1=person()  
#person1.name()      
class person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("helo",self.name)
person1=person('amul')  
person1.display() 

#below is function call
person("amul").display()         
