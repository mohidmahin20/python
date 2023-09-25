#global and local variable
balance=3000
def buy(item,price):
#local scope variable
#you can access global variable without using the global keyword
#but if you want to modify it  you have to use global keyword
    global balance
    print(f'previous balance value: ',balance)
    balance =balance -price

    print('balance after: ',balance)

buy('sunglass',1000)