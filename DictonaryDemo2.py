# Fetch and print dictonary values
emp={"QA":{"Aparajeeta", "Hanendra", "Nandish"}, "Manager":["Himadhri","Krishna", "Srinadh"]}

# Print keys and type
print(emp.keys())
print(type(emp.keys()))


# print values and type of values
print(emp.values())
print(type(emp.values()))

# print emp key value pair
# It returns the values in the form of tuples
print(emp.items())
print(type(emp.items()))

# how to delete dictonary values
emp.pop("QA")
print(emp)

# Syntax 2 to initialize dictionaries
emp1=dict(QA="Appu",Team = "Crusing Power", Manager="Ganesh")
print(emp1)

# Syntax 3 to initialize dictionaries using list of tuples
emp2 = dict([(1,"Appu"),(2,"Java"),(3,"Python")])
print(emp2)



