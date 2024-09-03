# Convert tuple to list or set
tup = (1,2,3,"test",False,99.0,1,1,2,3)

print(type(tup))
print(tup)

list1=list(tup)
print(type(list1))
print(list1)

s1=set(tup)
print(type(s1))
print(s1)

# tuple with length as 1
tup1=("Aparajeeta")
print(len(tup1))

tup2=("Aparajeeta",)
print(len(tup2))

# list of tuples
l1=[(1,3,4,5),(4,5,6,7),(10,20,30)]
print(type(l1))
print(l1)
print(l1[0])
print(l1[0][1])


# create tuple using Tuple constructor
t1=tuple([100,200,200,300])
print(type(t1))
print(t1)