#key value pair
#{key:value,key: value}
#dictionary
#object
#hash table
#overlap with set
person ={'name':' mahin','address':'gafargaon','age':21,'job':'student'}
print(person['job'])
person['language']='python'
person['name']='mohid'
del person['age']
print(person)

#special dictionary looping
for key,value in person.items():
    print(f"{key}: {value}")
    #print(key,value)