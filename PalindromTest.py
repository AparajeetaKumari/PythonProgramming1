list1 =[ 1, 2, 1]
list2 =[ 1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()
copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list1==list1):
    print("List is palindrom")
else:
    print("List is not palindrom")


if(copy_list2==list2):
    print("List is palindrom")
else:
    print("List is not palindrom")




