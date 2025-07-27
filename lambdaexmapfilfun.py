def square(numbers):
    for num in numbers:
        print(num**2,end=' ')
square([1,2,3,4,5])

#map function:-map function is used to apply  a function to every item in an iterable (like a list,tuple,etc) and return
#the result
'''
map(function,iterable)
function: A function like list,tuple or string whose elements will be processed by the function
map() returns a map object (an iterator),so you need to convert it to a list or tuple to see the result

'''

def square(num):
    return num**2
my_nums=[1,2,3,4,5]
for item in map(square,my_nums):
    print(item)
print(list(map(square,my_nums)))



def splicer(mystring):
    if len(mystring)%2==0:
        return 'even'
    else:
        return mystring[0]
names=['Rohan','omkar','om','nikhil']
print(list(map(splicer,names)))       #map function is a built-in python function.2]
#we don't write splicer() instead we write only splicer because we just want to pass the function we don't wanna execute function the map is doing for us

#filter function:-A filter function in python is used to filter elements from an iterable (like a list or tuple) based condition provided by a function
#it returns  only those elements for which the function returns True
'''
filter(function,iterable)
function:-A function that return either True or False for each item
iterable:-The sequence(like a list,tuple,etc) to filter
filter() returns an iterator,so you need to convert it to a list or loop throught it
'''
def check_even(num):
    return num%2==0
mynums=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(check_even,mynums)))
for n in filter(check_even,mynums):
    print(n,end=' ')

#lambda function:- lambda function is a small , anonymous function(i.e.,without a name) used for short-term use,especially
#when the function is simple and only needed temporarily
'''
lambda arguments:expression
lambda:keyword used to define the function
arguments:One or more inputs(just like a normal function)
expression:A single expression whose result is returned automatically

'''

lambda num:num**2
print(square(2))

#we can use map and filter function in lambda
my_nums=[11,12,13,14,15,16,17]
print(list(map(lambda num:num**2,my_nums)))

print(tuple(filter(lambda nums:nums%2==0,my_nums)))


























































































































































