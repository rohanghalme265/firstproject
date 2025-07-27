#ERRORS:- Errors are bound to happen in your code!
'''
*Especially when someone else ends up using it in an unexpected way.
*We can use error handling to attempt to plan for possible errors

*we use three keywords for this:
   1].try: this is the block of code to be attempted (may lead to an error)
   2].except: Block of code will execute in case there is an error in try block
   3].finally: A final block of code to be executed,regardless of an error
'''


# def add(n1,n2):
#     print(n1+n2)
#
# add(10,20)    #30
#
# number1 = 10
# number2= input("please provide a nuber: ")

# add(number1,number2)

try:
    # WANT TO ATTEMPT THIS CODE
    # MAY HAVE AN ERROR
    result = 10 + 10
except:
    print("Hey it looks like you aren't adding correctlly!")
else:
    print("Add went well!")
    print(result)

#
try:
    f = open('testfile','w')
    f.write("write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS Error")
finally:
    print("I always run")

#OSError- It occurs when a system-related error happens like 1).file not found 2).file permission denied 3).Invalid operation

#
try:
    f = open('testfile','r')
    f.write("write a test line")
except TypeError:
    print("there was a type error!")
except OSError:
    print("Hey you have an OS error")
finally:
    print("I always run")

#
try:
    f = open("testfile",'r')
    f.write("write a test line")
except:
    print("All other exceptions!")
finally:
    print("I always run")

def ask_for_int():
    try:
        result = int(input("please provide a number:"))
    except:
        print("Whoops! that is not a number")
    finally:
        print("End of try/except/finally")
ask_for_int()

#
def ask_for_int():

    while True:
        try:
            result = int(input("Please provide number:"))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes Thank You")
            break
        finally:
            print("I'm going to ask you again! \n")

ask_for_int()

#
def ask_for_int():

    while True:
        try:
            result=int(input("please provide a number"))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes Thank You")
            break
ask_for_int()

















































































































































































