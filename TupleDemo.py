tup = (1, "test", "Python", "Java",1,1,1,3,3,4,4,True)
print(tup)
print(tup.count(1))
print(tup.count(2))
print(tup.count(True))

# index
print(tup[2])
print(tup[-2])
# print(tup[100])

# index of an item
print(tup.index(3))
# print(tup.index(100))

#Slicing
print(tup[:5])
print(tup[5:])

# reverse tuple
print(tup[::-1])

# 'tuple' object does not support item assignment
# tup[0]="Aparajeeta"
# print(tup)


# <class 'tuple'>
print(type(tup))
