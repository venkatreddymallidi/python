class Student:
    def __init__(self):
        print("constructor accessed")
    def display(self):
        print("normal method is accessed")
std1=Student()#an object is created of Student class
              #then automatically constructed called when object is created
std1.display()#any noraml method is accessed by object of that class and
              # call it by using that class object
