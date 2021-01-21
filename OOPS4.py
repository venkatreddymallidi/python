# class is a collection of member variables and member functions and container(contains mem var &fun) have properties and attributes
class Student:
    def__init__(self,name,rollno):#member function
        self.n=name #member variable
        self.r=rollno #member variable
        print(name,rollno)
        print(self.n,self.r)
    def display(self):#member function
        print(self.n,self.r)
std1=Student("venkat",46)#name and rollno of student1 is stored in std1.object
std2=Student("ram",47)
std1.display()#so details of student1 using std1 object are accesed
st2.display()#display() method print details stored in std2 object because we call it using std2 object
        
