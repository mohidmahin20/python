def reverse_p(n):
    num =str(n)
    for digit in reversed(num):
        print(digit,end=" ")

t=int(input())
for _ in range(t):
        n=int(input())

        reverse_p(n)
        print()
