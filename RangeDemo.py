# printing values in a range
for x in range(0,50):
    print(x)


# printing values in a range
evenNums = []
oddNums =[]
for x in range(50):
    if(x%2==0):
        print("It is a even number")
        evenNums.append(x)
    else:
        print("It is odd number")
        oddNums.append(x)

print("Even numbers are:", evenNums)
print("Odd numbers are:", oddNums)



t1 = (10,200,19)
t2 = (211,311,422)
t3 = (455,355,655)

t = [t1,t2,t3]

for x,y,z in t:
    print(x)
    print(y)
    print(z)

print("========================")
for x in t:
    print(x[0])
    print(x[1])
    print(x[2])
