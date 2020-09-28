n=int(input('enter any digit no:'))
sum=0
while n!=0:
    lastno=n%10
    sum+=lastno
    n=n//10
print(sum)
