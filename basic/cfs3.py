def equationn(x,n):
    summ=0
    p=0
    while p<=n:
     summ+=x**p 
     p+=2
    return summ

x, n = map(int, input().split())
result=equationn(x,n)
print(result-1)