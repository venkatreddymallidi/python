class Student:
    def __init__(self,name,rollno): #__init__ constructor called when obj is created
        self.n=name                  #constructor have 3 parameters self gets std1 then std1.n=name later 2nd object created self=std2    
        self.r=rollno               #here self seperate details of students
    def display(self):              
        print(self.n,self.r)
std1=Student("venkat",46) #obj is created for student 1 and sending details of student
std1.display()             #calling normal method By using object of std1 then details of student 1 is printed because self=std1
std2=Student("lovely",45)  #here std2 self=std2 details of student 2 is stored in std2.n,std2.r
std2.display()             #calling display function to print details of student 2 by using object(std2)
