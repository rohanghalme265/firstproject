#Problem 1:- Fill in the class methods to accept coordiates as a pair of tuples and return the slope and distance of the line

class Line():

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1) / ((x2-x1))


#EXAMPLE OUTPUT

c1 = (3,2)
c2 = (8,10)

myline = Line(c1,c2)
print(myline.distance())     # 9.433981132056603
print(myline.slope())        # 1.6

# Fill in the class

class Cylinder():

    def __init__(self,hieght=1,radius=1):
        self.hieght = hieght
        self.radius = radius

    def volume(self):
        return self.hieght * 3.14 * (self.radius)**2

    def surface_area(self):
        top = 3.14 * (self.radius**2)

        return (2*top) + (2*3.14*self.radius*self.hieght)

mycyl = Cylinder(2,3)
print(mycyl.volume())               # 56.52
print(mycyl.surface_area())         # 94.2


#OOP-challenge

#For this challenge, create a bank account class that has two attributes
'''
*owner
*balance
and two methods
*deposit
*withdraw

As an added requirement,withdrawals may not exceed the available balance

Instantiate your class, make several deposite and withdrawlas,and test to make sure the account can't be overdrawn

'''
class Account():

    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,dep_amt):
        self.balance = self.balance + dep_amt
        print(f'Added {dep_amt} to the balance')

    def withdrawal(self,wd_amt):

        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print("withdrawal accepted")

        else:
            print("sorry not enough funds!")

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"

a = Account("Sam",500)
print(a)        # Owner: Sam
                # Balance: 500
a.deposit(100)  # Added 100 to the balance
print(a)          #Owner: Sam
                  #Balance: 600
a.withdrawal(400)  #a.withdrawal(400)
a.withdrawal(500)  #sorry not enough funds!
print(a)           #Owner: Sam
                   #Balance: 200




















































































































































































































