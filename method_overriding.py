class A:
    def display(self):
        print("method belongs to A")
class B(A):
    def display(self):
        print("method belongs to b")
    
b1=A()
b1.display()        