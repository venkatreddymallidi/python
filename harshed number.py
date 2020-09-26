def harshednumber(n):
    sum=0
    num=n
    while n>0:
        rem=n%10
        sum=sum+rem
        n=n//10
    if num%sum==0:
        print("harshed number")
    else :
        print("not a harshed number")

harshednumber(n=int(input()))

        
