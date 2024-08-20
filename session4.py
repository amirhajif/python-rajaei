# n=int(input("please enter numbr: "))
# counter=0
# for i in range(1,n+1):
#     if n%i==0:
#         counter+=1

# if counter<=2:
#     print("prime")
# else:
#     print("not-prime")

# for i in range(2,n):
#     if n%i==0:
#         counter+=1
#         break

# if counter>0:
#     print("not-prime")
# else:
#     print("prime")

# isPrime=True
# for i in range(2,n):
#     if n%i==0:
#         isPrime=False
#         break

# if isPrime:
#     print("prime")
# else:
#     print("not-prime")


# if isPrime==False:
#     print("not-prime")
# else:
#     print("prime")

# for i in range(2,n):
#     if n%i==0:
#         print("not-prime")
#         break
# else:
#     print("prime")

# i=0
# while i<5:
#     print("hello")
#     i+=1

# factoriel
# n=int(input("please enter number: "))
# i=1
# fact=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)

# n=int(input("please enter number: "))
# i,sum=1,0
# while i<n:
#     if n%i==0:
#         sum+=i
#     i+=1

# if sum==n:
#     print("kamel")
# else:
#     print("kamel nist")

# while True:
#     option=int(input("1-sayHello\n2-sayGoodbye\n3-sayName\n4-exit\nenter option: "))
#     if option==1:
#         print("hello")
#     elif option==2:
#         print("bye")
#     elif option==3:
#         print("amir")
#     elif option==4:
#         break

# scores=[]
# while True:
#     score=int(input("please enter score: "))
#     if score==-1:
#         break
#     scores.append(score)

# print(sum(scores)/len(scores))


# n=int(input("please enter number: "))
# sum=0
# while n>0:
#     sum+=n%10
#     n=n//10
# print(sum)


# degrees=(180,360,540)
# print(degrees)
# print(type(degrees))
# degrees[0]=150
# degrees=(250,360,140)
# print(degrees[0])
# for degree in degrees:
#     print(degree)

user={
    "username":"amirhossein",
    "password":"amir123",
    "age":23,
    "isProgrammer":True,
    "programmingLanguages":["cpp","c#","python"],
    "languages":("persian","english")
}
print(user)
print(user["age"])









