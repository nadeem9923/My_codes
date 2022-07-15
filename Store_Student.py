class Student:
    counter = 0
    classname = "MCA1"
    
    def __init__(self, r, n):
        self.rollno = r
        self.name=n
        Student.counter += 1
        
    def display(self):
        print("Roll number :",self.rollno)
        print("Name ",self.name)
        
    #setter method
    def set_name(self,name):
        self.name = name
        
    #getter method
    def get_name(self):
        return self.name
    
    @classmethod
    def displaytotal(cls):
        print("Total Students :",Student.counter)
        
    @staticmethod
    def dispclass():
        print("Student class name is: ",Student.classname)

s1 = Student(1, "Alex")
s1.display()
Student.displaytotal()
s2 = Student(2, "Bob")
s2.display()
Student.displaytotal()
s3 = Student(3,"Mima")
s3.display()
s3.set_name("Andre")
print(s3.get_name())