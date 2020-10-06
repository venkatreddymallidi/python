dict={}#declaring a empty dictionary
n1=int(input("enter no of keys:"))
n2=int(input("enter no of ele in values:"))
for i in range(n1):
    key=input("enter key name:")
    l=[]
    for j in range(n2):
        ele=int(input("enter element in value:"))
        l.append(ele)
    dict[key]=l
print(dict)
