n=int(input("how many elemets you want to enter into a list:"))
a=[]
for i in range(n):
    ele=int(input("enter elements:"))
    a.append(ele)
b=[]
for i in a:
    if i not in b:
        b.append(i)
c=[]
for i in b:
    c.append(a.count(i))
print("highest repeated element:",b[c.index(max(c))])
