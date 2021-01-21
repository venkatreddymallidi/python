class Student:     
    def __init__(self,name,rollno):#constructor
        self.n=name
        self.r=rollno
        print(name,rollno)
std1=Student("venkat",46)#object creation.object is instance(example of class ,created when we common data in  class for many times
std2=Student("ram",47)#when object created constructed is called until it is in rest
#self is object,when std1 obj is created self is std1,and two parameters from obj std1 is passed to constructor
#then it store like std1.n="venkat",std1.r=46 again for std2 also
