#Dictionaries:-{'key1':"value','key2':'value2'}
#It is unordered and can no be dorted
#object can retrieved by key name
#Dictionaries cannot retain order and not in sequence
#Dictionaries are mutable

# my_dict={'key1':'value1','key2':'value2'}
# print(my_dict)
# print(my_dict['key1'])

# prices_lookup={'apple':80,'oranges':40,'milk':60}
# print(prices_lookup['apple'])

# d={'k1':123,'k2':[0,1,2],'k3':{'insidekey':100}}
# print(d['k2'])
# print(d['k3'])

# d1={'key1':['a','b','c']}
# mylist=d1['key1']
# print(mylist)
# letter=mylist[2]
# print(letter)
# print(letter.upper())
# print(d1['key1'][1].upper())

d={'k1':100,'k2':200,'k3':300}
d['k4']=400
print(d)
d['k1']='New Value'
print(d)
print(d.keys())
print(d.values())
print(d.items())
d['k5']=500
print(d)
del d['k1']
print(d)
d.pop('k2')
print(d)

d2={"name":"Rohan","age":22,"city":"pune"}
d2.pop("name")
print(d2)
del d2["name"]
print(d2)
d2.popitem()
print(d2)
d2={k: v for k, v in d2.items() if k not in ["age","city"]}
print(d2)



























