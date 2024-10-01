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
        self.balance=balance

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
        return f'{self.id} {self.name} {self.fatherName} {self.balance}'

# employee Class
class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

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
    
    # setter and getter for salary
    def setSalary(self,salary):
        self.salary=salary
    def getSalary(self):
        return self.salary
    
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
        if isValidId(id):
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
    # if we dont have customer in list 
    if len(customers)==0:
        print("-------we dont have customer in our bank------------")
        time.sleep(2)
    else:
        for customer in customers:
            print(customer)
        time.sleep(2)

    # if customers:
    #     for customer in customers:
    #         print(customer)
    # else:
    #     print("-------we dont have customer in our bank------------")
    #     time.sleep(2)


# function for search customer base id
def searchCustomerById():
    id = int(input("please enter customer id for search: "))
    for customer in customers:
        if customer.getId()==id:
            print(customer)
            time.sleep(2)
            break
    else:
        print(f"-------we dont customer with this id {id} -------------")
        time.sleep(2)

# function for edit customer
def editCustomer():
    id=int(input("please enter id: "))
    for customer in customers:
        # find customer
        if customer.getId()==id:
            option=int(input("1-name\n2-fathername\n3-balance\nenter option: "))
            # update customer name
            if option==1:
                newName=input("please enter new name for update name: ")
                customer.setName(newName)
                print("-------cutomer name updated------------")

            # update customer fathername
            elif option==2:
                newFatherName=input("please enter new fatherName: ")
                customer.setFatherName(newFatherName)
                print("-------cutomer name updated------------")

            # update customer balance
            elif option==3:
                newBalance=int(input("please enter new balance: "))
                customer.setBalance(newBalance)
                print("-------cutomer name updated------------")
            time.sleep(2)
            break
    
    # not found customer
    else:
        print(f"-------we dont customer with this id {id} -------------")
        time.sleep(2)

# function for delete customer 
def deleteCustomer():
    id=int(input("please enter id: "))
    # id--> index in list --->del customers[index]
    index=-1
    for i in range(0,len(customers)):
        if customers[i].getId()==id:
            index=i
            break

    if index==-1:
        print(f"-------we dont customer with this id {id} -------------")
        time.sleep(2)
    else:
        del customers[index]
        print("------ customer deleted---------")
        time.sleep(2)
    
# function for request loan
def requestLoan():
    id=int(input("please enter id: "))
    for customer in customers:
        if customer.getId()==id:
            # get loan value from user
            value=int(input("please enter loan value: "))
            # check value less than balance
            if customer.getBalance()>=value:
                customer.setBalance(customer.getBalance()+value)
                print("--------- loan paid -------------")
                time.sleep(2)
            break
    else:
        print(f"-------we dont customer with this id {id} -------------")
        time.sleep(2)


while True:
    opt=int(input("1-add Customer\n2-show Customers\n3-search customer\n4-edit customer\n5-delete customer\n6-request loan\n12-exit\nenter option: "))
    if opt==1:
        addCustomer()
    elif opt==2:
        showCustomers()
    elif opt==3:
        searchCustomerById()
    elif opt==4:
        editCustomer()
    elif opt==5:
        deleteCustomer()
    elif opt==6:
        requestLoan()
    elif opt==12:
        break




