#Nested statement and scope:-
'''
*L:-Local--Names assigned in any way within a function (def or lambda),and not declared global in that function
*E:-Enclosing function locals --Names iin the local scope of any and all enclosing functions(def or lambda),from inner to outer
*G:Global (module)--names assigned at the top-level of module file,or declares global in a def within the file
*B:Built-in(python)--Names preassigned in the built-in names module:open,range,syntaxError,..
'''

# lambda num:num**2 (num right here is local to the lambda expression)

# GLOBAL
name = 'THIS IS A GLOBAL STRING'


def greet():
    # ENCLOSING
    name = 'sammy'

    def hello():
        # LOCAL
        name = 'IM A LOCAL'
        print('Hello ' + name)

    hello()


greet()


x = 50


def func(x):
    print(f'X is {x}')
    #LOCAL REASSIGNMENT
    x = 200
    print(f'I JUST LOCALLY CHANGED X TO {x}')


func(x)


x=100

def func(x):
    print(f'X is {x}')

    #local reassignment on a global variable
    x='NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')
    return x
print(x)
x=func(x)
print(x)



































































































