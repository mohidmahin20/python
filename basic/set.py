#set=unique items collection
#list []
#tupple ()
#set {}
#set er element alada vabe access hoyna
#set er elemnt chnge kora jayna
#set er nirdisto sthane add remove kora jayna

numbers= [12,23,34,45,12]
print(numbers)
numbers_set=set(numbers)
print(numbers_set)
numbers_set.add(55)
numbers_set.add(98)
print(numbers_set)
numbers_set.remove(12)
print(numbers_set)

#item check kora jay
if 9 in numbers_set:
    print('9 exists')
elif 45 in numbers_set:
    print('45 exist')

#union intersection
a={1,3,5}
b={2,3,4,5}
print(a& b)
print(a | b)