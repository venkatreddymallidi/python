#copying elements using list slicing
a=[1,5,2,3,7,6,9,10,4,8]
b=a[:]#copying elements of a to b
print('list a',a)
print('list b',b)
a.pop()
a.pop(2)
del a[1]
a.remove(9)
print("after some delete operations on list a=",a)
print("no changes in b ",b)
#copying elements using copy method
a=[1,5,2,3,7,6,9,10,4,8]
b=a.copy()#this method help to copy only elemets not memory location
del a[:]#deleting elements from start to end
print("deleting all elemts in list a=",a)
print("no changed in b",b)
