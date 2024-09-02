
dictDemo1 = {"QA":"Aparajeeta","Dev":"Magain", "Devops":"John"}
print(dictDemo1)

print(dictDemo1.get("QA"))
print(type(dictDemo1))
print(dictDemo1.keys())
print(dictDemo1.get("sbs"))
print(dictDemo1["Devops"])
# print(dictDemo1["Devopssss"])
#print(dictDemo1.pop())

#Diconaries can conatian lists or dictonaries

# Dictonating containing  list
dictDemo2 = {"Students":["Aiden","shanvi","Arkit"],"Teachers":{"Play":"Aasha","Nursery":"Mohini"}}
print(dictDemo2["Students"][0])
print(dictDemo2["Teachers"]["Nursery"])
dictDemo2["Director"]="Rajesh Kumar"
print(dictDemo2)
dictDemo2["Director"]="New Rajesh Kumar"
print(dictDemo2)

# Pop will ask for specific key to delete
print(dictDemo2.pop("Students"))

# Popitem() will delete in first in last out fashion
print(dictDemo2.popitem())
print(dictDemo2)
