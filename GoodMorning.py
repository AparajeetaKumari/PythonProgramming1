
import time

currentTime = int(time.strftime('%H'))
print(currentTime)
print(type(currentTime))

if(currentTime>=0 and currentTime<13 ):
    print("Good Morning Sir")
elif(currentTime>=12 and currentTime<17):
    print("Good afternoon sir")
else:
    print("good night sir")
