# --------------------------reading the file-----------------------

with open("sample.txt","r") as file:
    content=file.read()
    print(content)
    file.close()

# ------------------------ write into the file --------------------------
with open("sample.txt","w") as file:
    file.write("My name is Dhruv patel")
    file.close()

# --------------------------- append the content into the file --------------------------
with open("sample.txt","a") as file:
    file.write("My name is Dhruv patel")
    file.write("i am from Mamadev")
    file.close()
#  -------------------------- open file in both mode reading and writing--------------------------
with open("sample.txt" ,"w+") as file:
   
    file.write("my name is Dhruv Patel")
    file.seek(0)
    f=file.read()
    print(f)
    file.close()

# ------------------------------ open the file into both mode reading and appending mode
with open("sample.txt","a+") as file:
    file.write("i am from Bilimora\n")
    file.write("Python is the Programming Language")
    content=file.readlines()
    print(content)
    file.close()

# ----------------------------------  json file handling ----------------------------------

# import json
# x={"name":"Dhruv","age":22,"city":"Navsari"}
# y=json.dumps(x)

# print(y)
import json
x='{"name":"Dhruv","age":22,"city":"Navsari"}'

y=json.loads(x)
print(y)
