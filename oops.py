#OOP:-oop is a way to structure your code
'''
*OOP allows users to create their own objects
*Data and function (called methods) are bundled together into units called objects
*Objects are created from classes,which are like blueprint

**Main principles of oop:-
1].Encapsulation - Bundling data + methods into one unit (class).
2].Abstraction - Hiding complex details and showing only the necessary parts.
3].Inheritance - A class can inherit properties and methods from another class.
4].Polymorphism - One interface, many forms (like same method name doing different tasks).

SYNTAX:--
class NameOfclass():

      def _init_(self,param1,param2):
          self.param1=param1
          self.param2=param2

      def some_method(self):
           #perform some action
           print(self.param1)

'''

mylist=[1,2,3]
myset=set()
print(type(myset))         #<class 'set'>
print(type(set(mylist)))   #<class 'set'>
print(type(mylist))        #<class 'list'>

#
class Sample():     #class is keyword in python used to define a class
                    #A class is like blueprint for creating objects. class names in python start with an uppercase letter
    pass

my_sample=Sample()
print(type(my_sample))     #<class '__main__.Sample'>

#
class  Dog():

    def __init__(self,breed):

        #Attributes
        #we take in the argument
        #Assign it using self.attributes_name
        self.breed=breed

my_dog = Dog(breed='Lab')
print(type(my_dog))          #<class '__main__.Dog'>
print(my_dog.breed)          #Lab

#
class Dog():
    def __init__(self,mybreed):
        self.mybreed=mybreed
my_dog = Dog(mybreed='Huskie')
print(type(my_dog))            #<class '__main__.Dog'>
print(my_dog.mybreed)          #Huskie

#
class Dog():
    def __init__(self,mybreed):
        self.my_attribute= mybreed
my_dog = Dog(mybreed='Huskie')
print(type(my_dog))              #<class '__main__.Dog'>
print(my_dog.my_attribute)       #Huskie

#
class Dog():

    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name

        #Experts boolean True/False
        self.spots = spots

my_dog = Dog(breed='lab',name='Sammy',spots = False)
print(type(my_dog))    #<class '__main__.Dog'>
print(my_dog.breed)    #lab
print(my_dog.name)     #Sammy
print(my_dog.spots)    #False

#
class Dog():

    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species='mammal'

    def __init__(self,breed,name,spots):
        self.breed=breed
        self.name=name
        self.spots=spots

my_dog=Dog(breed='Lab',name='Sam',spots='False')
print(type(my_dog))     #<class '__main__.Dog'>
print(my_dog.breed)     #Lab
print(my_dog.name)      #Sam
print(my_dog.species)   #mammal


























































































































































































































































