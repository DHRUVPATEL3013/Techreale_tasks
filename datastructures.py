l=[1,2,3,4,5,6,7]
l1=["Dhruv","patel","Mamadev"]
l.append(8)
print(f"l : {l}")
l.extend(l1)
print(f"l : {l}")
print(f"l1 : {l1}")

l1.insert(2,7)
print(l1)
l1.remove(7)
print(l1)
l1.pop(1)
print(l1)
l1.pop()
print(l1)
l1.clear()
l1.append("Dhruv")
l1.extend(("Dhruv","Patel","Mamadev","bilimora","Navsari","valsad","Gujrat","Patel","India","Russia"))
print(l1)
print(l1.index("Mamadev",1,7))

print(l1.count("Dhruv"))

l1.sort(key=len,reverse=True)
print(l1)

l2=[3,5,6,7,8,2,3,4,5,8]
l2.reverse()
print(l2)
k=reversed(l2)
for i in k:
    print(i)


a=[1,2,3,4,5,[6,7,8]]
c=a.copy()
c[5].append("Dhruv")
print(c)
print(a)

# ------------------------------- List as a stack ---------------------------

stack=[3,4,5,6,7]
stack.append(8)
stack.append(9)
print(stack)
stack.pop()
stack.pop()
print(stack)

# --------------------------------- List as a Queue ---------------------------

from collections import deque

queue= deque(["Eric", "John", "Michael"])
queue.append("Dhurv")
queue.append("Rolex")
print(queue)
queue.popleft()
print(queue)

# ---------------------------------- List Comprehension ---------------------------

two_table=[f"2 * {i} = {2*i}" for i in range(1,11)]
print(two_table)

# squares=list(map(lambda x:x*x,range(900011)))
# print(squares)

squares=[x * x for x in range(1,11) ]
print(squares)

sample=[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(sample)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

rows=[[row[i]for row in matrix] for i in range(4)]
print(rows)

print(matrix.pop(0))
print(matrix)

# ------------------------------- del statement --------------------------------
k=[1,2,3,4,0,5]
# k.remove(5)
# print(k.remove(4))
# print(k)

del k[0]

print(k)

del k[2:]

print(k)



t=(12345,445677,"Dhruv")
print(type(t))
print(t[1])
u=t,(4676657,85787858)
print(u)
m=([1,2,3],[4,5,6])
empty=()
print(type(empty))
print(empty)

tp="Dhruv",
print(type(tp))
print(tp)
x,y,z=t
print(x,y,z)

 # --------------------------------- sets ------------------------------------

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana','banana'}
print(basket)
print("orange" in basket)
print("aple" in basket)

a=set('aracadabra')
b=set('alacazam')

print(a)
print(b)
print(a-b)
print(a | b)
print( a & b)
print(  a^b )

# -------------------------------- Dictionaries ------------------------------------

tel = {'jack': 4098, 'sape': 4139}
tel["name"]="Dhruv"
print(tel)
print(tel["jack"])

del tel["sape"]
print(tel)
print(list(tel))
print(sorted(tel))
print("name" in tel)
print("jack" not in tel)

sd=dict([("name","Dhruv"),("city","Bilimora"),("phone",9313152833)])
print(sd)

f={x: x**2 for x in range(5)}
print(f)

ki=dict(name="Dhruv", age=22, country="india")
print(ki)

for key,value in ki.items():
    print(key,value)


lis=["tic","tac","toe"]
for i,v in enumerate(lis):
    print(i,v)


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for x,y in zip(questions,answers):
    print(x,y)


import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
new_values=[]

for x in raw_data:
    if math.isnan(x):
        pass
    else:
        new_values.append(x)
print(new_values)
