# inheritance
class Person:
    def __init__(self,fname,lname,nc,city):
        self.fname=fname
        self.lname=lname
        self.nc=nc
        self.city=city
    
    def setFname(self,fname):
        self.fname=fname
    def getFname(self):
        return self.fname

    def setLname(self,lname):
        self.lname=lname
    def getLname(self):
        return self.lname
    
    def setNc(self,nc):
        self.nc=nc
    def getNc(self):
        return self.nc

    def setCity(self,city):
        self.city=city
    def getCity(self):
        return self.city 
    
    def __str__(self):
        return f"{self.fname} {self.lname} {self.city} {self.nc}"

class Employee(Person):
    def __init__(self,fname,lname,nc,city,salary):
        super().__init__(fname,lname,nc,city)
        self.salary=salary
    
    def setSalary(self,salary):
        self.salary=salary
    def getSalary(self):
        return self.salary
    
    def __str__(self):
        return f"{self.fname} {self.lname} {self.city} {self.nc} {self.salary}"

employee=Employee("amir","hajitabar",205,"babol",2000)

print(employee.getLname())
print(employee.getFname())
print(employee)

# multi level inheritance
'''
    GrandParent
    Parent--->GrandParent
    Children-->Parent--->GrandParent
'''
# multiple inheritance
'''
    A
    B
    C--->A,B
'''
