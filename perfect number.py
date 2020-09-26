def perfectnumber(no):
    
    sum=0
    for i in range(1,no):
        
        if no%i==0:
            
            sum=sum+i
    if sum==no:
        
        print(no,"is a perfect number")
    else :
        
        print(no,"not a perfect number")
no=int(input("enter a no:"))
perfectnumber(no)
