a=list(map(int,input().split()))
print("you entred list a=",a)
swap=True
while swap:
    swap=False
    for i in range(len(a)-1):
        
        if a[i]>a[i+1]:
            swap=True
            a[i],a[i+1]=a[i+1],a[i]
          
print("after sorting list a=",a)
