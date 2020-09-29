n=int(input("enter a no:"))
f1=0
f2=1
print(f1,f2,end=" ")
f3=f1+f2
i=3
while i<=n:
    
    print(f3,end=" ")
    f1=f2
    f2=f3
    f3=f1+f2
    i+=1       
