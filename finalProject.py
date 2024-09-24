import time
# 2 blank lists for customers,employees
customers=[]
employees=[]

# cutomer class
class Customer:
    def __init__(self,id,name,fatherName,balance):
        self.id=id
        self.name=name
        self.fatherName=fatherName
        self.balace=balance

    # setter and getter for id
    def setId(self,id):
        self.id=id
    def getId(self):
        return self.id
    
    # setter and getter for name
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    
    # setter and getter for fatherName
    def setFatherName(self,fatherName):
        self.fatherName=fatherName
    def getFatherName(self):
        return self.fatherName
    
    # setter and getter for balance
    def setBalance(self,balance):
        self.balance=balance
    def getBalance(self):
        return self.balance

    def __str__(self):
        return f'{self.id} {self.name} {self.fatherName} {self.balace}'

# employee Class
class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    
    def __str__(self):
        return f'{self.id} {self.name} {self.salary}' 

# function for check customer id unique or not
def isValidId(id):
    for customer in customers:
        if customer.getId()==id:
            return False
    return True

# function for add customer
def addCustomer():
    while True:
        id=int(input("please enter id: "))
        if isValidId(id)==True:
            break
        else:
            print("-----id exist try again--------")

    # get infos from customer 
    name=input("please enter name: ")
    fatherName=input("please enter fatherName: ")
    balance=int(input("please enter balance: "))

    # create object 
    customer=Customer(id,name,fatherName,balance)

    # add object to list
    customers.append(customer)

    print("--------customer created-------")
    time.sleep(2)

# function for show customers infos
def showCustomers():
    for customer in customers:
        print(customer)

while True:
    opt=int(input("1-add Customer\n2-show Customers\n12-exit\nenter option: "))
    if opt==1:
        addCustomer()
    elif opt==2:
        showCustomers()
    elif opt==12:
        break


