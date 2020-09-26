def armstrong(num):
    
    armst=0
    no=num
    while num>0:
        
       rem=num%10
       armst=armst+rem*rem*rem
       num=num//10
    if no==armst:
        
        print(no,"is a armstrong number")
    else :
        
        print(no,"is not a armstrong number")
    
n=int(input("enter a no:"))
armstrong(n)


    
    
