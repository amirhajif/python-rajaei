# FILE
'''
variable,collection

run--> allocate
stop-->de-allocate

re-run---> empty
'''
# file=open("datas.txt")

# file=open("datas.txt","r")

# content=file.read()
# print(content)

# print(file.read())

# for line in file:
#     print(line.strip())

# content=file.readlines()
# print(content)
# map
# contentWitOutEnter=list(map(lambda line:line.strip(),content))
# print(contentWitOutEnter)

# file.close()

# create-write
# file=open("products.txt","w")

# file.write("apple\nsamsung\nxiaomi\nhuawei")

# check is exist not create again - write
# file=open("products.txt","a")
# file.write("\nsony")

# file=open("products2.txt","a")
# file.write("\nsony")

# Error-handling
number1=10
number2=0

try:
    print(number1/number2)  
except:
    print("we have an Error,check number2")
else:
    print("we dont have error in process")
finally:
    print("my app is finished")

