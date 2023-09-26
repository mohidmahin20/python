def fibonaccii(n):
    sequence=[0,1]
    while len(sequence)<n:
        next_num=sequence[-1]+sequence[-2]
        sequence.append(next_num)
    return sequence[:n]

n=int(input())
result=fibonaccii(n)
for num in result:
    print(num,end=" ")