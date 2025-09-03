
# # class MyClass():
# #     def __init__(self,name,age,city):
# #         self.name=name
# #         self.age=age
# #         self.city=city
# #     def display_user(self):
# #         print(f"Name : {self.name}")
# #         print(f"Age : {self.age}")
# #         print(f"City : {self.age}")
# # mycl=MyClass("Dhruv",22,"Bilimora")
# # mycl.display_user()

# # ----------------------- Polymorphism -----------------------------

# class Animal():
#     def speak(self):
#         print("Animal can Speak")
# class Cat():
#     def speak(self):
#         print("Cat Meow")
# class Dog():
#     def speak(self):
#         print("Dog Bark")

# anmimal=Animal()
# anmimal.speak()
# cat=Cat()
# cat.speak()

# dog=Dog()
# dog.speak()

# class Bird():
#     def fly(self):
#         print("Bird can fly")


# class Sparrow(Bird):
#     def fly(self):
#         print("Sparrow can fly")


# class Parrot(Bird):
#     def fly(self):
#         print("Parrot can fly")


# sparrow=Sparrow()
# sparrow.fly()

# parrot=Parrot()
# parrot.fly()


# # ------------------------- Inheritence ---------------------------------
#                        # ------------ single inheritence -------------------
# class Parent():
#     def func1(self):
#         print("this function is in the parent class")
     
# class Child(Parent):
#     def func2(self):
#         print("this function is in the Child class")

# obj=Child()
# obj.func1()
# obj.func2()

# #   --------------------------  Multiple Inheritence -----------------------------

# class Mother():
#     mother_name=""
#     def mother(self):
#         print(self.mother_name)
# class Father():
#     father_name=""
#     def father(self):
#         print(self.father_name)

# class Son(Mother,Father):
#     def parents(self):
#         print("Father : ",self.father_name )
#         print("Mother : ",self.mother_name)
    
# son=Son()
# son.mother_name="ABC"
# son.father_name="XYZ"
# son.parents()


# # ---------------------------- Multilevel inheritence ------------------------

# class GrandFather():
#     def __init__(self,grandfathername):
#         self.grandfathername=grandfathername

# class Father(GrandFather):
#     def __init__(self,fathername,grandfathername):
#         self.fathername=fathername
#         super().__init__(grandfathername)

# class Son(Father):
#     def __init__(self,sonname,fathername, grandfathername):    
#         self.sonname=sonname
#         super().__init__(fathername, grandfathername)

#     def family_member(self):
#         print(f"father :{self.fathername}")
#         print(f"Grandfather : {self.grandfathername}")
#         print(f"Son : {self.sonname}")
        

# s1=Son("abc","pqr","xyz")
# print(s1.grandfathername)
# s1.family_member()

# # --------------------------- Hierarchical Inheritance ------------------------------

# class Parent():
#     def func1(self):
#         print("this function is in parent class")

# class Child1(Parent):
#     def func2(self):
#         print("this function is in child 1 class")

# class Child2(Parent):
#     def func3(self):
#         print("this function is in child 2 class")


# obj1=Child1()
# obj2=Child2()

# obj1.func1()
# obj1.func2()

# obj2.func1()
# obj2.func3()


# #-------------------------------- Hybrid inheritence ----------------------------

# class School():
#     def func1(self):
#         print("this function is in the School class")


# class Student1(School):
#     def func2(self):
#         print("this function is in the student 1")
# class Student2(School):
#     def func3(self):
#         print("this function is in the student 2")

# class Student3(Student1,School):
#     def func4(self):
#         print("this function is in the student 3")

# st1=Student1()
# st2=Student2()
# st3=Student3()

# st1.func1()
# st1.func2()

# st3.func1()
# st3.func2()
# st3.func4()


# #--------------------------------- Abstraction -------------------------------------

# from abc import ABC,abstractmethod

# class Car(ABC):
#     @abstractmethod
#     def start(self):
#         pass
    
# class BMW(Car):
#     def start(self):
#         print("bmw engine started by button")
# class Audi(Car):
#     def start(self):
#         print("Audi engine stared by key")
    
# bm=BMW()
# ad=Audi()

# bm.start()
# ad.start()



#    ----------------------- Public Variables ----------------------------

# class Myclass():
#     def __init__(self,name,email,phone,accountnumber):
#         self.name=name
#         self.email=email #---> public varibles
#         self._phone=phone    #--> protected varibles
#         self.__accountnumber=accountnumber #----> Private varibles


# mycls=Myclass("Dhruv","dh@gmail.com",9078675645,1234567890)
# print(mycls.name)
# print(mycls.email)
# print(mycls._phone)
# print(mycls._Myclass__accountnumber)   # to access private varible 

# ------------------------- dataclasess ----------------------------------
from dataclasses import dataclass
@dataclass
class Product():
    name:str
    price:float
    quantity: int

laptop=Product("laptop",25000,2)

print(laptop)

# --------------------------- iterators --------------------------------------

s="Dhruv"
it=iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#  ---------------------------- Generators ----------------------------------

def sample():
    for i in range(10):
        yield i
sm=sample()
print(next(sm))
print(next(sm))
print(next(sm))
print(next(sm))

# ------------------------ Decorators ---------------------------------

def wrapper(func):
    def inner(a):
        print("first")
        func(a)
        print("third")
    return inner
@wrapper
def sample(a):
    print(a)

sample("Second")

