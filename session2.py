# scores=[20,5,17,19,16]
# users=["amir","reza","ahmad"]

# print(scores)
# print(type(scores))
# print(scores[0])
# print(len(scores))
# print(users[-1])
# print(scores[1:4])

# students=["mohammad","ali","ahmad"]
# # update element
# students[1]="alireza"
# print(students)
# # add item (append)
# students.append("mohammad reza")
# print(students)
# # add item in special index
# students.insert(2,"amir")
# print(students)


# scores=[20,15,14,9]
# del (by index)
# del scores[2]
# print(scores)

# pop
# pop vs append
# deletedScore=scores.pop()
# print(scores)
# print(deletedScore)

# deleted=scores.pop(2)
# print(deleted)
# print(scores)

cars=["pride","pego","samand","pego","arizo"]

# cars.remove("pego")
# print(cars)

# numbers=[20,14,9,78,49,124,12]
# numbers.sort()
# print(numbers)

# cars.sort()
# print(cars)

# mix=["amir",12,"reza",16]
# mix.sort()
# print(mix)

# numbers.sort(reverse=True)
# print(numbers)

# users=["amir","reza","ahmad","ali"]
# print(sorted(users))
# print(users)

# users=["amir","reza","ahmad","ali"]
# users.reverse()
# print(users)
# print(len(users))

# numbers=[20,14,9,78,49,124,12]
# print(max(numbers)) 
# print(min(numbers)) 
# print(sum(numbers))
# print(sum(numbers)/len(numbers))

# a=20
# b=a
# a=30
# print(a)
# print(b)

# copy list
# pythonStudents=["ahmad","ali","reza"]
# students=pythonStudents[:]

# pythonStudents.append("katiosha")
# students.append("amir")
# print(pythonStudents)
# print(students)

# number=int(input("please enter number: "))
# > = 0--->mosbat else manfi

# if number>=0:
#     print("mosbat")
# else:
#     print("manfi")


# number1=int(input("please enter number1: "))
# number2=int(input("please enter number2: "))

# if number1==number2:
#     print("equal")
# else:
#     print("not-equal")

# if number1 != number2:
#     print("not-equal")
# else:
#     print("equal")

# username=input("please enter username: ")
# password=input("please enter password: ")

# if username=="admin" and password=="admin":
#     print("login")
# else:
#     print("invalid username/password")

# yek adad daryaft va fasl e moadel an ra namayesh dahad
seasson=int(input("please enter seasson: "))
if seasson==1:
    print("bahar")
elif seasson==2:
    print("tabestan")
elif seasson==3:
    print("paiiz")
elif seasson==4:
    print("zemestan")
else:
    print("invalid input,tray later")
