def sample_function():
    print("this is a sample function")

sample_function()

# function with parameters
def sum(a,b):
    print(a+b)
sum(7,8)

#  ------- default arguments --------------

def multiply(a,b=8):
    print(a * b )
multiply(5)

# ----------------------- keyword arguments -----------------------
def division(a,b):
    print(a/b)
division(b=9,a=8)

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

pos_only_arg(8)
kwd_only_arg(arg=8)

 # -------------arbitory arguments ----------------------------- #

def concat(*args,sep="/"):
    print(args)
    c=sep.join(args)
    print(c)
concat("Dhruv","Patel","Mamadev","Bilimora")

def concat_1(*args,sep="/"):
    print(args)
    c=sep.join(args)
    print(c)
concat("Dhruv","Patel","Mamadev","Bilimora",sep=".")

print(list(range(0,10)))
ran=(5,10)
print(list(range(*ran)))

def dict_arg(**kwargs):
    for i in kwargs:
        print(i,kwargs[i])
dict_arg(name="Dhruv",surname="Patel")

#  ------------------------------ lambda functions ----------------------------------

square=lambda a:a*a
ans=square(3)
print(ans)

# ------------------------------------- DOC String ------------------------------------

def my_function():
    """this is a sample function for introduce the doc string"""
    pass

print(my_function.__doc__)