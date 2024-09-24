'''
user:
    username
    password
    age

'''

# user={
#     "username":"amir",
#     "password":"amir123",
#     "age":23
# }

class User:
    # built-in
    # constructor-sazandeh-initializer
    def __init__(self,username,password,age):
        self.username=username
        self.password=password
        self.age=age

# instance-OBJECT
# user=User("amirhossein","amir123",23)

# # connect attribute 
# print(user.username)
# print(user.password)
# print(user.age)

# # separate
# user2=User("reza","mohammadi",34)
# print(user2.password)


class Rectangle:
    def __init__(self,tol,arz):
        self.tol=tol
        self.arz=arz
    
    # method
    # self---> pointer-esharegar--->object called method
    def area(self):
        return self.tol*self.arz
    def env(self):
        return self.tol*2 + self.arz*2




rectAngle=Rectangle(5,4)
print(rectAngle.area())
print(rectAngle.env())

rectAngle2=Rectangle(8,6)
print(rectAngle2.area())

'''
method:
    class function
    can access with object with .
    should pass self
'''


# name="amir"
# print(name.upper())
