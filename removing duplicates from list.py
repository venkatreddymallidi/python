a=[2,4,6,2,1,10,1,2,4,9,3,2,6,5] # declaring a list
b=[]# declaring a empty list
for i in a: #accessing list a and assigning elements to i
    if i not in b:#adding unique elements to b
        b.append(i)#append method in list add value to last position
print(b)
