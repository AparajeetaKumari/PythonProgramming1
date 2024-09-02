import datetime

today = datetime.datetime.today()
print(type(today))
print(f"{today:%B %d, %Y}")

print('appu','geekforgeeks', sep='@')
print('appu','geekforgeeks', sep=' ')

# use end function for python print

print("Python", end='@')
print("GeekforGeeks")

str = "this is a string reverse test"
print(str[::-1])
print("".join(reversed(str)))
print(type(reversed(str)))