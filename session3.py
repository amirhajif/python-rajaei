# users=["amir","reza","ahmad"]
# username=input("please enter username: ")

# if username in users:
#     print("exist")
# else:
#     print("not-exist")

# if username not in users:
#     print("not-exist")
# else:
#     print("exist")

# students=["amir"]
# if len(students)==0:
#     print("we dont have student")
# else:
#     print("we have student")

# if students:
#     print("we have students")
# else:
#     print("we dont have students")

# seasson=int(input("plese enter seasson: "))
# match seasson:
#     case 1:
#         print("bahar")
#     case 2:
#         print("tabestan")
#     case 3:
#         print("paiiz")
#     case 4:
#         print("zemestan")
#     case _:
#         print("invalid input")

# students=["mohammad","ali","reza"]
# for student in students:
#     print(student)
    
# numbers=[20,15,14,17,16]
# sum=0
# for number in numbers:
#     # sum=sum+number
#     # print(sum)
#     sum+=number
# print(sum)

# numbers=[10,12,0,-5,-6,0,20]
# # yek barname ke tedad adad haye + - 0 ro be man bege
# pcounter,zcounter,ncounter=0,0,0
# for number in numbers:
#     if number>0:
#         pcounter+=1
#     elif number==0:
#         zcounter+=1
#     else:
#         ncounter+=1

# print(pcounter,zcounter,ncounter)

# range
# print(list(range(0,10)))
# for i in range(0,10):
#     print("hello")

# number=int(input("please enter number: "))
# # 0.......20
# for i in range(0,number+1,3):
#     print(i)

# break - continue
# for i in range(0,10):
#     if i==6:
#         continue
#     print(i)


# n=int(input("please enter number: "))
# # 5--->1*2*3*4*5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)


# n=int(input("please enter number: "))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

score=int(input("please enter score: "))
days=int(input("days of trip: "))
if days==0:
    print(20)
elif days==7:
    print(score)
else:
    print(score-days)
