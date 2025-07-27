#1
def myfun():
    print('Hello World')
myfun()

def myfun(name):
    print('hello {}'.format(name))
myfun("Rohan")

#2
def print_name(name):
    print(f'hello {name} where is your hometown?and Have you eaten?')
print_name("pratik")

#3
def myfun(x):
    if x==True:
        return 'hello'
    elif x==False:
        return 'Goodby'
print(myfun(False))

#4
def myfun(x,y,z):
    if x:
        return z
    else:
        return y
result=myfun(1,2,True)
print(result)
result1=myfun(1,2,False)
print(result1)

#5
def myfun(a,b):
    print(a+b)
result=myfun(10,53)
result

#6
def is_even(num):
    if num%2==0:
        return True
    else:
        return False
print(is_even(6))

#7
def is_greater(x,y):
    if x>y:
        return 'x is greater than y'
    else:
        return 'y is greater than x'
print(is_greater(734,843))

#8
def myfun(*arg):
    return sum(arg)
print(myfun(23,523,13454))

#9
def myfun(*args):
    out=[]
    for num in args:
        if num%2==0:
            out.append(num)
    return out
print(myfun(38,283,43,88,94))

#10
def myfun(x):
    out=[]
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)
input_string="HelloWorld"
result=myfun(input_string)
print("Original String:",input_string)
print("Modified String:",result)
#we can also write like print(myfun("HelloWorld")) in one line























































































































