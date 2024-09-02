x = int(input("Enter a number:"))

match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case _ if x!=90:
        print("X is different")
    case _ if x==70:
        print("Hello World")



y = input("enter your name")

for i in y:
    print(i)


colors = ["Red", "Green", "Yellow", "Blue"]
for color in colors:
    print(color)



for k in range(5):
    print(k)


for f in range(1,11):
    print(f)