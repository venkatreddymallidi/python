def is_palindrome(n):
    rev=0
    num=n
    while n!=0:
        lastno=n%10
        rev=rev*10+lastno
        n=n//10
    if num==rev:
        return True
    else :
        return False
n=int(input('enter a no:'))
print(is_palindrome(n))
