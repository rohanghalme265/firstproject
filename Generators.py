#Generators:Generator functions allow us to write a function that can send back a value and then later resume to pick up where it left off
'''
*When generator function is complied they become an object that supports an iteration protocol
*That means when they are called in your code they don't actually return a value and then exit

*Generator are useful when
    1].You have large amounts of data
    2].You want to save memory
    3].you want to process data lazily,i.e,one piece at a time

*it uses yield keyword:- i].It pauses the function and remembers where it left off
                         ii].When you call the generator again(using next(),it resumes from the last yield
'''

def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

for x in create_cubes(10):
    print(x)

#
def create_cubes(n):

    for x in range(n):
        yield x**3

for x in create_cubes(10):
    print(x)

#
def create_cubes(n):

    for i in range(n):
        yield i**3

print(list(create_cubes(10)))

#
def gen_fibon(n):

    a = 1
    b = 1
    output=[]
    for i in range(n):
        output.append(a)
        a,b = b,a+b
    return output

for number in gen_fibon(10):
    print(number)

#
def gen_fibon(n):

    a = 1
    b = 1

    for i in range(n):
        yield a
        a,b = b,a+b

for number in gen_fibon(10):
    print(number)


#
def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()
print(g)        #<generator object simple_gen at 0x0000012585E65B40>

print(next(g))
print(next(g))
print(next(g))


#
s = 'hello'
for letter in s:
    print(letter)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

#Homework
#Q1].create a generator that generates the squares of numbers up to some number N

def gensquares(N):
    for i in range(N):
        yield i**2

for x in gensquares(10):
    print(x)

#Q2].Create a generator that yields 'n' random numbers between a low and high number (that are inputs).
#Note: Use the random library.For example
import random    #random is a built-in python module that helps you generate random numbers or make random choices.


print(random.randint(1,10))

def rand_num(low,high,n):

    for i in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)



#Q3].Use the iter() function to convert the string below into an iterator.

s = 'hello'
s = iter(s)    # It is is a Buil-in python function that return an iterator object from a sequence
print(next(s))


#Q4].Explain a use case for a generator using a yeild statement where you would not want to use a normal function with a return statement

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)
#this is a generator comprehension similar to list comprehension,but with**()**instead of[]

for item in gencomp:
    print(item)     
































































































































































