def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    print(is_prime(n))
 
def before_prime(n):
    for i in range(n-1,1,-1):
        if is_prime(i):
            return i
            
def after_prime(n):
    n=n+1
    while True:
        if is_prime(n):
            return n
        n+=1
def nearest_prime(n):
    if is_prime(n):
        print(n)
    else :
        x=before_prime(n)
        y=after_prime(n)
        if abs(n-x)>abs(n-y):
            print(x)
        elif abs(n-y)>abs(n-x):
            print(y)
        else :
            print(x,y)
n=int(input("enter a no:"))
nearest_prime(n)
        
n=int(input())
is_prime(n)
