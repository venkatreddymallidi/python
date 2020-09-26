n=int(input("enter a number"))
for i in range(2,n):
    if n%i==0:
        break
        print(n,"not a prime number")
else:
    print(n,"prime number")
