import decimal
num1 = float(input("Enter the number "))
num2 = float(input("Enter the number "))
num3 = float(input("Enter the number "))
num4 = float(input("Enter the number "))

if(num1>num2 and num1>num3 and num1>num4 ):
    print("Largest number is ", num1)
elif(num2>num3 and num2>num4):
    print("Largest number is ", num2)
elif(num3>num4):
    print("Largest number is ", num3)
else:
    print("Largest number is ", num4)


num5 = decimal.Decimal('2.2')
num6 = decimal.Decimal('1.2')
res = num5+num6
print(res)

# nsxn