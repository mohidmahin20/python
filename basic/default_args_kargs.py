def sum(num1,num2,num3):
    result =num1+num2+num3
    return result

total=sum(44,39,30)
print(total)
#arg
def all_sum(*numbers):
    print(numbers)
total=all_sum(45,46,43,32)
print('all sum: ',total )