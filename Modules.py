#Modules:- Pythn has several built-in modules that we haven't fully explored yet!
'''
#* Modules Covered:-
      1].Collections
      2].Os module and Datetime
      3].Math and Random
      4].Python Debugger
      5].Timeit
      6].Regular Expressions
      7].Unzipping and Zipping Modules

'''

from collections import Counter

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3]
print(Counter(mylist))    #Counter({3: 7, 1: 5, 2: 4})

mylist = ['a','a',10,10,10]
print(Counter(mylist))    #Counter({10: 3, 'a': 2})

print(Counter('aaaaabbbbccccsssjdjdjdjd'))
#Counter({'a': 5, 'b': 4, 'c': 4, 'j': 4, 'd': 4, 's': 3})

sentence = "How many times does each word show uo in tis sentence with a word"
print(Counter(sentence.lower().split()))
#Counter({'word': 2, 'how': 1, 'many': 1, 'times': 1, 'does': 1, 'each': 1, 'show': 1, 'uo': 1, 'in': 1, 'tis': 1, 'sentence': 1, 'with': 1, 'a': 1})

letter = 'aaabbbccccddddddd'
c = Counter(letter)
print(c)     #Counter({'d': 7, 'c': 4, 'a': 3, 'b': 3})

print(c.most_common())  #[('d', 7), ('c', 4), ('a', 3), ('b', 3)]
print(c.most_common(2))  #[('d', 7), ('c', 4)]

print(c)
print(list(c))   #['a', 'b', 'c', 'd']


#
from collections import defaultdict
d = {'a':10}
print(d)
print(d['a'])  #10

d = defaultdict(lambda:0)
d['correct'] = 100
print(d['correct'])    #100
print(d['Wrong KEY!']) #0
print(d)    #defaultdict(<function <lambda> at 0x000002422A8B3B00>, {'correct': 100, 'Wrong KEY!': 0})

mytuple = (10,20,30)
print(mytuple[0])  #10

from collections import namedtuple
Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(age=5,breed='Husky',name='Sam')
print(sammy)    #Dog(age=5, breed='Husky', name='Sam')
print(type(sammy))    #<class '__main__.Dog'>
print(sammy.age)
print(sammy.breed)
print(sammy.name)
print(sammy[1])


#Opening and reading files and Folders(Shutil and OS Modules)
'''
*Python OS module and shutil allow us to easily navigate files and directries on the 
computer and them perform actions on them, such as movinng them or delecting them
'''

#
   #C:\Users\ROHAN\PyCharmMiscProject

f = open('practice.txt','w+')
f.write('This is a test string')
print(f.close())


import os

print(os.getcwd())

# print(os.listdir('C:\Users'))

#
# import shutil
#
# print(shutil.move('type.py',r'C:\Users\ROHAN'))
#
# print(os.listdir(r'C:\Users\ROHAN'))

print(os.listdir())




#*Datetime Modul:-

import datetime

mytime = datetime.time(13,20,1,20)
print(mytime.minute)
print(mytime.hour)
print(mytime)
print(mytime.microsecond)
print(type(mytime))     #<class 'datetime.time'>

today = datetime.date.today()
print(today)         #2025-07-24
print(today.year)    #2025
print(today.day)     #24
print(today.ctime())  #hu Jul 24 00:00:00 2025

#
from datetime import datetime

mydatetime = datetime(2021,10,3,14,20,1)
print(mydatetime)   #2021-10-03 14:20:01

mydatetime = mydatetime.replace(year=2020)
print(mydatetime)     #2020-10-03 14:20:01

#DATE


from datetime import date

date1 = date(2021,11,3)
date2 = date(2020,11,3)

result = date1 - date2
print(type(result))     #<class 'datetime.timedelta'>
print(result.days)      #365


datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)
print(datetime1-datetime2)    #365 days, 10:00:00
mydiff = datetime1-datetime2
print(mydiff.total_seconds()) #31572000.0


# Math and Random Module:-

import math

# help(math)

value = 4.35
print(math.floor(value))  #4 (it returns the largest integer less than or equal to give number)-it rounds down a number to the nearest whole number
print(math.ceil(value))   #5 (ceil stands for ceiling and it returns the smallest integer greater than or equal to a given number,it rounds up)
print(round(4.35))        #4
print(round(4.5))         #4
print(round(5.5))         #5
print(math.pi)            #3.141592653589793

from math import pi
print(pi)                #3.141592653589793

from math import e
print(e)

print(math.inf)
print(math.nan)

#Numpy

print(math.e)
print(math.log(math.e))    #1.0
print(math.log(100,10))  #2.0
print(10**2)
print(math.sin(10))
print(math.degrees(pi/2))
print(math.radians(180))

#
import random
print(random.randint(0,100))

(random.seed(101))
print(random.randint(0,100))

print(random.randint(0,77))

random.seed(0,101)
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))

#
mylist = list(range(0,20))
print(mylist)

print(random.choice(mylist))
print(mylist)

#SAMPLE WITH REPLACEMENT

print(random.choices(population=mylist,k=10))

#SAMPLE WITHOUT REPLACEMENT

print(random.sample(population=mylist,k=10))  #[8, 17, 4, 9, 3, 11, 1, 10, 5, 7]

print(mylist)         #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
random.shuffle(mylist)
print(mylist)         #[12, 1, 2, 5, 6, 14, 0, 4, 19, 16, 7, 8, 18, 15, 9, 10, 13, 11, 3, 17]

print(random.uniform(a=0,b=10)) #it pick any number in between 0 to 10

print(random.gauss(mu=0,sigma=1))





















































































































































































































































