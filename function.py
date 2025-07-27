#function:-functions allows us to create blocks of code that can be easily executed many times ,without needing to constantly rewrite the entire block of code
           #it helps you to avoid repition  and make programs easier to understand and maintain
           #It devides large programs into smaller blocks
#creating a function requires a very specific syntax , including the def keyword, correct indentation, and proper structure
'''
def name_of_function():

Docstring explain function


def=keyword telling python this is a function
name_of_function=you decide on the function name.notice "snake casing"
#snake casing is all lowercase with underscores between words
#A colon indicates an upcoming indented is then "inside" the function
'''

def add_function(num1,num2):
    return num1+num2
result=add_function(1,2)
print(result)
#return allows you to save the result to a variable
#most function will use return.rarely will a function only print()

def say_hello():
    print("hello")
    print("how")
    print('are')
    print("you")
say_hello()   #we have to add start and close paranthesis otherwise it means you not callin the function

def greet(name):
    print(f'Hello {name}')
greet("Rohan")

def say_hello(name='pratik'):
    print(f'hello {name}')
say_hello()

#return
def add_num(num1,num2):
    return num1+num2
result=add_num(12,20)
print(result)   #32

# def return_result(a,b):
#     print(a+b)                  #it not return anything ti be saved
# return_result(10,20)

def return_result(a,b):
    return a+b
std=return_result(10,20)
print(std)

def myfunc(a,b):
    print(a+b)
    return a+b
myfunc(33,65)

def sum_numbers(num1,num2):
    return num1+num2
print(sum_numbers(398,94) )

 

def return_result(a,b):
    print(a+b)                  #it not return anything ti be saved
return_result(10,20)























