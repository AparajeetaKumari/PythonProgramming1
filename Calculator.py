num1 = float(input("Enter first numeber"))
num2 = float(input("enter second number"))
operation = input("Enter operation")


if(operation == '+'):
    print("Addition is", num1+num2)
elif(operation=='-'):
    print("Substarction is", num1-num2)
elif(operation=='*'):
    print("Multiplication is", num1*num2)
elif(operation=='//'):
    print("Division is", num1//num2)
elif(operation=='%'):
    print("Reminder is", num1%num2)
else:
    print("Invalid operation")