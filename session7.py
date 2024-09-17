def sumNumbers(n):
    if n==0:
        return 0
    else:
        return n+sumNumbers(n-1)
    
# def feactoriel(n):
#     if n==1:
#         return 1
#     else:
#         return n*feactoriel(n-1)
    
def fibo(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

# print(fibo(6))
    
# print(sumNumbers(5))
# print(feactoriel(5))

# def reastaurnat(*foods):
#     # print(foods)
#     print("--------we have this foods-----------")
#     for food in foods:
#         print(food)

# reastaurnat("burger","pizza","sandwich","kebab")

# def restaurant(**foods):
#     # print(foods)
#     print("--------we have this foods-----------")
#     for food,price in foods.items():
#         print(f"{food}---->{price}")

# restaurant(burger=2000,sandwich=1500,kebab=3000)

# def m2(n):
#     return n*2

# m2=lambda n:n*2
# print(m2(5))

# add = lambda a,b:a+b
# print(add(5,6))

# numbers=[2,4,1,5,67,10,23,17]

# newNumbers=[]
# newNumbers=list()

# for number in numbers:
#     newNumbers.append(number*2)

# print(newNumbers)

# numbers=[2,4,1,5,67,10,23,17]

# newNumbers=list(map(lambda number:number*2,numbers))
# print(newNumbers)

# def multiplyTwo(number):
#     return number*2

# newNumbers=list(map(multiplyTwo,numbers))
# print(newNumbers)

# numbers=[2,4,1,5,67,10,23,17]

# def checkEven(number):
#     if number%2==0:
#         return True
#     else:
#         return False

# # filteredNumbers=list(filter(lambda number:number%2==0,numbers))
# filteredNumbers=list(filter(checkEven,numbers))
# print(filteredNumbers)

# newNumbers=[]
# for number in numbers:
#     if number%2==0:
#         newNumbers.append(number)

# print(newNumbers)

# import functions

# functions.sayHello()
# functions.reastaurnat("burger","pizza","kebab")

# from functions import sayHello,feactoriel

# print(feactoriel(5))

# from functions import *

# sayHello()
# feactoriel()
# reastaurnat()

# from functions import feactoriel as f

# print(f(5))

# import functions as f
# print(f.feactoriel(5))

# import math

# print(math.sqrt(36))
# print(math.pi)
# print(math.pow(2,5))

# import time

# print("----------before delay---------")

# time.sleep(3)

# print("----------after delay---------")

# import random

# print(random.randint(10,100))

# users=["amir","reza","ahmad","mohammad","jafar"]
# print(random.choice(users))

# import datetime

# # print(datetime.datetime.now())
# date=datetime.datetime.now()
# print(date.strftime("%A"))

# import requests

# cars={"benz","bmw","pride","prado","suzuki"}

# print(cars)
# cars.add("audi")
# print(cars)

# cars.remove("benzamir")
# cars.discard("benzamir")
# print(cars)

numbers1={1,2,3,4,5}
numbers2={5,6,7,8,9,10}

# allNumbers=numbers1.union(numbers2)
# print(allNumbers)

# numbers1.update(numbers2)
# print(numbers1)

# intersection=numbers1.intersection(numbers2)
# print(intersection)


numbers1.intersection_update(numbers2)
print(numbers1)
