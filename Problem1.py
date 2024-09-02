import sys
import datetime
print("Twinkle, twinkle, little star,\n\t How I wonder what you are! \n \t\tUp above the world so high, \n \t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")


print("Python version")
print(sys.version)

print("Version info")
print(sys.version_info)

now = datetime.datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))
