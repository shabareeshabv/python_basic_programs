class car:
    def turnon(self):
        print("start")
        return self
    def drive(self):
        print("ddrive")
        return self
    def breake(self):
        print("break")
        return self
    def breake1(self):
        print("break")
        return self
car=car() 
#car.turnon().drive()
#car.breake().breake1()
car.turnon().drive().breake().breake1()

     
            