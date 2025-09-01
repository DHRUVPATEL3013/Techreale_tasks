squares=[2,4,8,16,32]
print(squares)


print(squares[0])
print(squares[-1])

print(squares[:6])

cubes=[1,8,27,65,125]
print(squares+cubes)

cubes[3]=64
print(cubes)

cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

characters=['a','b','c','d','e','f','g','h']
characters[2:5]=['C','D','E']
print(characters)
characters[2:5]=[]
print(characters)
# characters[:]=[]
print(characters)
print(len(characters))
a=[1,2,3]
b=['a','b']
c=[a,b]
print(c)
print(c[0])

print(a.index(1))
a.remove(1)
print(a)
a.reverse()
print(a)
reversed(a)
print(a+[4])

