def reverse(n):
    rev=0
    while n>0:
        lastno=n%10
        rev=rev*10+lastno
        n=n//10
    
    print('reverse of given number:',rev)
n=int(input("enter a no:"))
reverse(n) #func call

        
