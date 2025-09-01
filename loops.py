
# # ---------------- for loop -----------------------

# words=["Dhruv","patel","mamadev","bilimora"]
# for word in words:
#     print(word, len(word))

# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# for user,val in users.copy().items():
#     if val=='inactive':
#         users.pop(user)
# print(users)

# # ----------- range function ---------------- #

# for i in range(5):
#     print(i)

# print(list(range(5,10)))
# print(list(range(0,10,3)))
# print(list(range(10,0,-3)))

# a=['Dhruv','Patel','Mamadev','Bilimora']
# for i in range(len(a)):
#     print(i,a[i])
# print(sum(range(5)))    

# ---------------------------------break and continue statement -----------------------------
even=[]
for i in range(1,20):
    if i%2==0:
       even.append(i)
       if len(even)>=5:
           break
       else:
           
           continue
print(even)
        
# ------------------------- for else loop ----------------------------------------

# number=int(input("enter the number : "))
# for i in range(2,number):
#     if number%i==0:
#         print("it is not prime number")
#         break
# else:
#     print("it is prime number")

# --------------------- pass statement ---------------------------------------

for i in range(10):
    pass
# --------------------- match statement ------------------------------------
number =700
print("djhdhjh")
match number:
    case 300:
        print("it is 300")
    case 400:
        print("it is 400")
    case 500:
        print("it is 500")
    case 600 | 700 | 800:
        print(f"it is {number}")
    case _:
        print("there is no matching case")

match (0,0):
    case (0,0):
        print("its an origin")
    case (0,y):
        print(f"y is {y}")
    case (x,0):
        print(f"x is {x}")
    case _:
        print("there is no matching case")

    