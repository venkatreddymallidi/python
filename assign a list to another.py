a=[1,5,6,7,9,2,3,4,10]
b=a
print("list a",a)
print("list b",b)
a.pop()#removes lastelement(i.e,list[-1])
a.pop(0)#removes element based on index,here the element in 0th position deleted
del a[3]#this same as above method
a.remove(3)#removes given value from the list
print("after performing delete operations on list a=",a)
print("delete operations on a is reflected into list b=",b) 
