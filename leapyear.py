#program to find leap year or not
year=int(input("enter a year"))
if year%400==0 or (year%4==0 and year%100!=0):#1996 and 2004 is divisible by 4 and divisible by 100 so leap years  2100 not a leap year but divisible by 4 divisible by 100 so leap year divisible by 4 not divisible by 100
    print("leap year")
else:
    print("non leap year")
