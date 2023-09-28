class car:
    def __init__(self):
        self.__updatesoftware()# private method because it statrt from __
    def drive(self):
        print("driving")    
    def __updatesoftware(self):
        print("updating software")   
blackcar=car()         
blackcar.drive()
black.__updatesoftware()# in this methos we cant accesss out side the class