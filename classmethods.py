#

class Dog():

    species='mammal'  #THIS IS CLASS ATTRIBUTES

    def __init__(self,breed,name):
        self.breed=breed
        self.name=name

    #METHOD
    def bark(self,number):
        print("WOOF! My name is {} and the number is {}".format(self.name,number))
my_dog = Dog('Lab','Frankie')
print(type(my_dog))     #<class '__main__.Dog'>
print(my_dog.species)   #mammal
print(my_dog.name)      #Frankie
my_dog.bark(10)         #WOOF! My name is Frankie and the number is 10

#
class Circle():

    #CLASS OBJECT ATTRIBUTES
    pi=3.14

    def __init__(self,radius=1): #radius=1 means its default value if no radius is passed when creating a Circle object
        self.radius = radius
        self.area=radius*radius*Circle.pi

    #METHOD
    def get_circumference(self):
        return self.radius*self.pi*2
my_circle=Circle(30)
print(my_circle.pi)                   #3.14
print(my_circle.radius)               #30
print(my_circle.get_circumference())  #188.4
print(my_circle.area)                 #2826.0








































































































































































































