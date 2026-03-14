def fact(num):
    if (num==0 or num==1):
        return 1
    else:
        return num * fact(num-1)
    
a=fact(3)
b=fact(6)
print(a,b)