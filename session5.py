# user={
#     "username":"amirhossein",
#     "password":"amir123",
#     "age":23,
# }

# print(user.keys())
# print(user.values())

# for key,value in user.items():
#     print(f"{key}--->{value}")

# [('username', 'amirhossein'), ('password', 'amir123'), ('age', 23)]

# print(user.items())

# del user["age"]
# print(user)

# print(user["fatherName"])
# print(user.get("fatherName","we dont have this key in dict"))


# user["email"]="amir@gmail.com"
# print(user)

# user["password"]="amir@123"
# print(user)

# print(user)
# print(user["password"])

# admin={
#     "username":"admin",
#     "password":"admin"
# }

# username=input("please enter username: ")
# password=input("please enter password: ")

# if username==admin["username"] and password==admin["password"]:
#     print("login")
# else:
#     print("invalid password or username")

# 1-signup 2- login 3- show users
# users=[]
# while True:
#     opt=int(input("1-signup\n2-login\n3-show users\n4-exit\nenter option:"))
#     if opt==1:
#         username=input("please enter username: ")
#         password=input("please enter password: ")
#         user={
#             "username":username,
#             "password":password
#         }
#         users.append(user)
#         print("------user created---------")
#     elif opt==2:
#         username=input("please enter username: ")
#         password=input("please enter password: ")
#         for user in users:
#             if user["username"]==username and user["password"]==password:
#                 print("-------welcome to website--------")
#                 break
#         else:
#             print("-----invalid username/password-------")
#     elif opt==3:
#         if users:
#             for user in users:
#                 for key,value in user.items():
#                     print(f"{key}--->{value}")
#                 print("--------------------")
#         else:
#             print("we dont have user")
#     elif opt==4:
#         break

'''
[
    {
            "username":"amir",
            "password":"amir123"
    },
    {
            "username":"reza",
            "password":"reaza123"
    },
    {
            "username":"jafar",
            "password":"jafar123"
    },
]  

username--->amir
password-->amir123
------------------
username--->reza
password--->reza123
-----------------
'''

# programmers={
#     "amir":"front",
#     "reza":"security",
#     "mohammad":"ui/ux",
#     "ahmad":"back",
# }

# for key in sorted(programmers.keys()):
#     print(f"{key}--->{programmers[key]}")

'''
ahmad--->back
amir--->front
mohammad--->ui/ux
reza--->security
'''


programmers={
    "amir":["pyton","js"],
    "ahmad":["js","c#"],
    "reza":["python","js","c#"]
}

for name,languages in programmers.items():
    print(name+":")
    counter=1
    for language in languages:
        print(f"\t{counter}-{language}")
        counter+=1

'''
amir:
    1-python
    2-js
ahmad
    1-js
    2-c#
reza:
    1-pyhton
    2-js
    3-c#
'''
