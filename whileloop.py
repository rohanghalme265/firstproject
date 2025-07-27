'''
while loop:-
 syntax of a while loop
           while some_boolean_condition:
              #do something
else:
  #do somethings different
'''
x=0
while x < 5:
    print(f'the current value x is {x}')
    x = x + 1  #(we can write this as well as x+=1)
else:
    print(f'x is not less than 5')

y=50
while y<10:
    print(f'the current value of y is {y}')
    y+=1
else:
    print(f'y is greater than than 10')

'''
we can use break, continue, and pass statements iin our loops to add additional functionality for various cases.
the three statements are defined by:
           break: Breaks out of the current closest enclosing loop
           continue: Goes to the top of of the closest enclosing loop
           pass: Does nothing at all
'''

f=[1,2,3]
for item in f:
    pass
print('end of my script')

mystring='sammy'
for letter in mystring:
    if letter=='a':
        continue
    print(letter)

my_string="Rohan"
for letter in my_string:
    if letter=="a":
        break
    print(letter)

a=0
while a<5:
    if x==2:
        break
    print(a)
    a+=1

'''
#useful operators:-
'''

for num in range(10):
    print(num)


for num in range(3,10):
    print(num)
for num in range(1,11,2):
    print(num)

print(list(range(1,11,2)))

index_count=0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count+=1

index_count=0
word='abcde'
for letter in word:
    print(word[index_count])
    index_count+=1

for index,letter in enumerate(word):    #enumerate is a function in python and it keep track of index
    print(index)
    print(letter)
    print('\n')

mylist1=[1,2,3,4,5]
mylist2=['a','b','c','d','e']
mylist3=[100,200,300,400,500]
for item in zip(mylist1,mylist2,mylist3):       #zip function is used to combine two or more iterables like list, tuples
    print(item)                                 #it arrange element wise, creating pairs of group of items
print(list(zip(mylist1,mylist2,mylist3)))

std=[11,22,33,44,55]
std1=[111,222,333,444,555]
std2=['a','b','c','d','e']
for a,b,c in zip(std,std1,std2):
       print(a,b,c)

mylist4=[1,2,3,4,5,6]
mylist5=['a','b','c']
mylist6=[100,200,300,400]
for item in zip(mylist4,mylist5,mylist6):
    print(item)            #zip function ignore the extra item in the list

print("x" in [1,2,34])   #False
print('x' in {'x','y','z'})  #True
print('mykey' in{'mykey':345})  #True

d={'mykey':345}
print(345 in d.keys()) #False
print(345 in d.values())  #True

mylist=[10,20,30,40,100]
print(min(mylist))   #10
print(max(mylist))   #100

#random function

#shuffle
from random import shuffle          #It not return a new list but rearrange the list
mylist=[1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print("Shuffle List:",mylist)  #[7, 6, 1, 3, 10, 8, 9, 2, 4, 5]

from random import shuffle
original=[10,20,30,40]
copy=original[:]
shuffle(copy)
print("Original:",original)
print("Copy:",copy)


#randint
from random import randint
print(randint(0,100))
print(randint(0,100))

mynum=randint(0, 10)
print(mynum)

from random import randint
for i in range(5):
    print(randint(10,50))

import random
num =random.randint(1, 10)
print("Random number between 1 and 10:", num)
#we can also write it as a
from random import randint
num=randint(1,10)
print("Random number between 1 and 10:",num)


#how to expect user input
print(input('Enter a number here:  '))




















