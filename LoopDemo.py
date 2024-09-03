# we can loop through - String, Set, List, Tuple, Dictionary

# Iterate through a String

name = "Aparajeeta"

for s in name:
    print(s)


print("============================================")
evenCount = 0
oddCount = 0
# Iterate through a list
list1 =[90,100,90,60,80]
for l in [90,100,33,55,87]:
    print(l)
    if(l%2==0):
        evenCount=evenCount+1
        print("Number is even")
    else:
        oddCount = oddCount+1
        print("Number is odd")

print("List printed")
print("Even numbers are",evenCount)
print("Odd numbers are ",oddCount)

print("============================================")
# Duplicate values will not be printed as sets does not ontain duplicate values
# Iterate through a set
set1 ={10,20,30,10,"Aparajeeta","Dimple",10.0,True,False,True}
for s in set1:
    print(s)