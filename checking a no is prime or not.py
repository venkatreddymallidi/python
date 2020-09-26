n=int(input("enter a number to check whether it is a prime or not"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print(n,"prime number")
else:
    print(n,"not a prime number")
