#guess the output
x=-5
a=1
b=-5
if a>0:   #if condition true then its internal elif executed
    if b>0:     #In elif statement any one condition true,then else not executed
        x=x+5
    elif a>5:
        x=x+4
    else :
        x=x+3
else :       #if condition false then else come into play
    x=x+2
print(x)
