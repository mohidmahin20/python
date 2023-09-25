def full_name(first,last):
    name=f'full name is: {first} {last}'
    return name
name =full_name('Alu','mia')
#name=full_name(last='mia',first='Alu')
print(name)
#def famous(**kargs)


def famous_name(first,last,**addition):
    name=f'{first} {last}'
    # print(addition)
    # print(addition['title'])
    for key, value in addition.items():
     print(key,value)
    return name
name=famous_name(first='taher',last='Ali',title='mister',adj='valo')
print(name)

#return multiple things from an array
def a_lot(n1,n2):
   sum=n1+n2
   mult=n1*n2
   remain=n1-n2
   return sum,mult,remain
everything=a_lot(55,21)
print(everything)