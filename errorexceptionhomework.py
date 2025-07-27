#Q1].Handle the excetion thrown by the code below by using try and except blocks

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Type Error! Watch out!")

#Q2].Handle the exception thrown by the code below by using try and except blocks.then use a finally block to print "ALl Done".

try:
    x=5
    y=0
    z=x/y
except:
    print("Error!!")
finally:
    print("All done")

#Q3].write a function asks for an integer and prints the square of it.Use a while loop with a try,except.else block to account
#for incorrect inputs

def ask():

    while True:
       try:
           n = int(input("Enter a number: "))
       except:
           print("please try again! \n")
           continue
       else:
           break
    print("Your number squared is: ")
    print(n**2)
ask()

#OR

def ask():

    # Waiting for correct response
    waiting = True
    while waiting:
        try:
            n = int(input("Enter a number: "))
        except:
            print("Please try again! \n")
            continue
        else:
            waiting = False
        print("Your number squared is: ")
        print(n**2)
ask()











































































































































































