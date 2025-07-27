# Decorators:-Decorators allow you to "decorate" a function, let's discuss what that word means in this context
#python has decorators that allow you to tack on extra functionality to an already existing function.
# They use the @ operator and are then placed on top of the original function.
'''
*Imagine you created a function:

       def simple_func():
            # Do simple stuff
            return something

* Now you want to add some new capablities to the function:

       def simple_func():
           #want to do more stuff!
           # Do simple stuff
           return something

*tou have to two options:
     *Add that extra code(functionality) to your old function.
     *Create a brand new function that contains the old code,and then add new code to that

'''

def func():
    return 1
print(func())    #1
print(func)      #<function func at 0x000001D7A8483240>


#
def hello():
    return "Hello!"
print(hello())      #Hello!
print(hello)        #<function hello at 0x000001D7A84F3B00>
greet = hello
print(greet())      #Hello!

del hello
# print(hello())
print(greet())     #Hello!

def hello(name="jose"):
    print('The hello() function has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'
    def welcome():
        return '\t This is welcome() inside hello'

    print(greet())
    print(welcome())
    print('This is the end of the hello funcyion!')

hello()       #The hello() function has been executed!
	                #This is the greet() func inside hello!
	                #This is welcome() inside hello
              #This is the end of the hello funcyion!

#
def hello(name='jose'):

    print('The hello() function has been executed!')

    def greet():
        return '\t this is the greet() func inside the hello()!'

    def welcome():
        return '\t This is a welcome() inside hello!'

    print(("I am going to return a function!"))

    if name == 'jose':
        return greet
    else:
        return welcome

my_new_func = hello('jose')   #The hello() function has been executed!
                              #I am going to return a function!

print(my_new_func())          #    this is the greet() func inside the hello()!



# #
def cool():

    def super_cool():
        return 'I am very cool!'

    return super_cool

some_func = cool()
print(some_func)      #<function cool.<locals>.super_cool at 0x00000244376ACF40>
print(some_func())    #I am very cool!



#
def hello():
    return 'Hi jose!'
def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())
print(hello)              #<function hello at 0x0000028C59D6CFE0>
print(hello())            #Hi jose!
other(hello)         #Other code runs here!
                     #Hi jose!






#
def new_decorators(original_func):

    def wrap_func():
        print("Some extra code, before the original functiom")

        original_func()

        print('Some extra code, after the function!')

    return wrap_func

def func_needs_decorator():
    print("I want to be decorated!")

func_needs_decorator()     #I want to be decorated!

decorated_func = new_decorators(func_needs_decorator)
decorated_func()      #Some extra code, before the original functiom
                      #I want to be decorated!
                      #Some extra code, after the function!
@new_decorators
def func_needs_decorator():
    print("I want to be decorated!")

func_needs_decorator()      #Some extra code, before the original functiom
                            #I want to be decorated!
                            #Some extra code, after the function!
































































































































































































