def helloWorld():
    print("Hello this my function without argument")
    print("Bye")

def sum(x,y):
    c=x+y
    print(c)
    return c

# if function does not return any vale and we print it, it will return none
helloWorld()
print(sum(10,20))


# function with default value
def sumNums(num1,num2=0,num3=1,num4=2):
    num = num1+num2+num3+num4
    return num

print(sumNums(10,20,11,10))



# calling function with key value argument
def hello(fname,lname):
    print("Hello",fname, lname)


# calling function
hello("Aiden", "Kachhap")
hello(fname="Benhur",lname="Kachhap")