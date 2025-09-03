# # # try:
# # #     open("database.sqlite")
# # # except OSError:
# # #     raise RuntimeError("unable to handle error")

# # # ---------------------- raisng exceptions-------------------------

# # # x="helllo world"

# # # if type(x) is not int:
# # #     raise TypeError("only integres are allowed")

# # # num=-1
# # # if num<0:
# # #     raise Exception("sorry no numbers below zero")

# # # ----------------------------- exception chaining --------------------------

# # # try:
# # #     int("hello world")
# # # except ValueError as e:
# # #     raise RuntimeError("Failed to Process input",e)


# # # def func():
# # #     raise ConnectionError()
# # # try:
# # #     func()
# # # except ConnectionError as err:
# # #     raise RuntimeError('Failed to open Database')


# # # -------------------- userdefine  exceptions ----------------------

# # class InvalidAgeError(Exception):
# #     def __init__(self, age,msg="Age must be between 0 and 120"):
# #         self.age=age
# #         self.msg=msg
# #         super().__init__(self.msg)

# #     def __str__(self):
# #         return f"{self.age} --> {self.msg}"
    
# # def set_age(age):
# #     if age < 0 or age > 120:
# #         raise InvalidAgeError(age)
# #     else:
# #         print(f"age set to : {age}")
# # try:
# #     set_age(189)
# # except InvalidAgeError as e:
# #     print(e)


# # ---------------------------------- Defining Clean up Actions------------------------

# def divide(x,y):
#     try:
#         result=x/y
#     except ZeroDivisionError:
#         print("you are dividing by zero")
#     else:
#         print(f"answer is : {result}")
#     finally:
#         print("execution completed.")
# divide(9,9)


# with open("sample.txt","r") as file:
#     content=file.read()
#     print(content)


# def f():
#     exc=[OSError('error 1'),SystemError('error 2')]
#     raise ExceptionGroup('there were problems',exc)
# f()
# try:
#     f()
# except Exception as e:
#     print(f'caught {e} : e')


# --------------------------- Enriching Exceptions with Notes ---------------------------
x=9
y=0
try:
    re=x/y
except Exception as e:
    e.add_note("number can not be divisible by Zero")
    raise
    

