#string formating fo printing:-
#from random import sample

print('This is a string {}'.format('INSERTED'))
print('My name {} {}'.format('is','Rohan'))
print('My {} {} Rohan'.format('name','is'))
print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

result=100/777
print(result)
print('The result was {}'.format(result))
print('the result was {r:1.5f}'.format(r=result))

result=103.12345
print('The result was {r:3.3f}'.format(r=result))

name="Jose"
print(f'Hello,his name is {name}')

name='sam'
age=5
print(f"{name} is {age} years old")

print('{0:1} | {1:5}'.format('Fruit','Quantity'))
print((60 + (10 ** 2) / 4 * 7) - 134.75)
print(type(3+1.5+4))

s="hello"
print(s[::-1])

print([0]*3)
list3=[1,2,[3,4,"hello"]]
print(list3)
list3[2][2]="goodbye"
print(list3)
list4=[5,4,3,2,1]
print(sorted(list4))

d={'simple_key':'hello'}
print(d['simple_key'])
d1={'k1':{'k2':'hello'}}
print(d1['k1']['k2'])
d2={'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d2['k1'][0]['nest_key'][1][0])
d3={'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d3['k1'][2]['k2'][1]['tough'][2][0])
original = {'b': 3, 'a': 2, 'c': 1}
sorted_by_keys = dict(sorted(original.items()))
print(sorted_by_keys)














