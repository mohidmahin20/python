def sum_of_odd(x,y):
    odd_sum=0
    if x<y :
       
       for num in range(x+1,y):
           if num%2==1:
               odd_sum +=num
    else :
       for num in range(y+1,x):
           if num%2==1:
               odd_sum +=num

    return odd_sum

t=int(input())

for i in range(t):
    x, y = input().split()
    x=int(x)
    y=int(y)
    result=sum_of_odd(x,y)
    print(result)