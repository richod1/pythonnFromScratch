class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def __str__(self):

        return f"my first name is {self.fname} and my lastname is {self.lname}"

    def printName(self):
        print(self.fname,self.lname)
person1=Person("Degraft","Frimpong")
print(person1)


person1.printName()

# creating child class
class Student(Person):
    def __init__(self,firstname,lastname,year):
        super().__init__(firstname,lastname)
        self.graduationyear=year

    def welcome(self):
        print("welcome  ",self.fname,self.lname, "to clas of ",self.graduationyear)
    
student=Student("Mike","oslean",2019)

print(student.welcome())

def greeting(name):
    print("Hello " + name)