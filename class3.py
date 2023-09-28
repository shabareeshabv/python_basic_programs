class student:
    clg='xys'
    def __init__(self,rollno,name):
       self.rollno=rollno
       self.name=name
    def display(self):
        print("studet name",self.name)
        print("student roll number",self.rollno)
        print("college",student.clg)
student1=student("001","shabari")
student1.display()
student2=student("002","shabareesh")
student2.display()
 
             