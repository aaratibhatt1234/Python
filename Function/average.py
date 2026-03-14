def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    avg=sum/len(numbers)
    return avg

c=average(2,4,6,8,10)
print(c)
       