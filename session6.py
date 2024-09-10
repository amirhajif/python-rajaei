# print("hello")

# # definition
# def sayHello():
#     print("hello world")

# # call
# sayHello()


# f(x)=3x+5
# def f(x):
#     print(3*x+5)

# f(10)
# f(int(input("please enter number: ")))
# number=int(input("please enter x: "))
# f(number)

# def checkEvenOrOdd(number):
#     if number%2==0:
#         print("even")
#     else:
#         print("odd")

# def factoriel(number):
#     fact=1
#     for i in range(1,number+1):
#         fact*=i
#     print(fact)

# def rectangleArea(tol,arz):
#     print(tol*arz)

# # keyword argument - default value for argument
# def introduce(name,age,city):
#     print(f"my name is {name} and {age}year`s old and from {city}")

# def authotize(username,password,isLogin):
#     if isLogin==None:
#         print("at first login")
#     else:
#         print("login")

# def sum(m,n,a=4,b=5):
#     print(m+n+a+b)

# sum(m=5,n=6,b=4)

# introduce(age=23,city="babol",name="amir")
# introduce("amir",23)
# introduce("amir",23)
# introduce("amir",23,"babol")

# authotize("amir","amir123",True)

# rectangleArea(10,5)
# factoriel(5)
# checkEvenOrOdd(10)

# name="amir hossein"
# print(len(name))
# return


def m2(n):
    return n*2
    return n*3

def factoriel(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    
    return fact

def introduce(name,age,city):
    # message=f"my name is {name} and {age} year`s old and from {city}"
    # return message

    return f"my name is {name} and {age} year`s old and from {city}"

def isEven(number):
    if number%2==0:
        return True
    else:
        return False
  
# result=isEven(10)
# # print(result)
# if result:
#     print("even")
# else:
#     print("odd")

# print(introduce("amir",23,"babol"))

# javab=factoriel(5)
# print(javab)

# # stop ball ---> shoot
# result=m2(10)
# print(result)

# # shoot
# print(m2(10))


# todo-list
todos=[]

def createTodo(id,title,isDone):
    return {
        "id":id,
        "title":title,
        "isDone":isDone    
    }

def addTodo():
    id=int(input("please enter id: "))
    title=input("please enter title: ")
    isDone=False
    todo=createTodo(id,title,isDone)
    todos.append(todo)
    print("--------task added------------")

def showTasks():
    for todo in todos:
        print(f"id-->{todo['id']}\ntitle--->{todo['title']}")
        if todo["isDone"]:
            print("status-->done")
        else:
            print("status-->pending")

def finishTask():
    id=int(input("id of task: "))
    for todo in todos:
        if todo["id"]==id:
            todo["isDone"]=True
            break
    else:
        print("we dont have todo with this id")


while True:
    opt=int(input("1-add\n2-finish task\n3-show tasks\n4-exit\nenter option:"))
    if opt==1:
        addTodo()
    elif opt==2:
        finishTask()
    elif opt==3:
        showTasks()
    elif opt==4:
        break
