#Inheritance:-1]It allows a child class (or subclass) to inherit the attributes and methods from a parent class (or superclass)
'''
#why use inheritance?
*Reuseability: Avoid writing the same code again .
*Extendability: Add or change features in child classes.
*Organized code: Groups related classes in a clean hierarchy.
**Types of Inheritance:-
1].Single Inheritance:- One child,one parent
2].Multiple Inheritance:- One child,multiple parents
3].Multilevel Inheritance:- Child-->Parent--->Grandparent
4].Hierarchical Inheritance:- Multiple children from one parent
5].Hybrid Inheritance:- Combination of types above
'''

#
class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an Animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def eat(self):
        print("I am a Dog and eating")

    def bark(self):
        print("WOOF!")

mydog = Dog()    #ANIMAL CREATED
                 #Dog created
mydog.eat()      #I am a Dog and eating 
mydog.who_am_i() #I am an Animal
mydog.__init__() #ANIMAL CREATED
                 #Dog created

#POLYMORPHISM:-1].Polymorphism means "many forms"
#2].In programming, polymorphism allows the same method name or operator to behave differently based on the object that is using it.

class Dog():

    def __init__(self,name):
        self.name=name

    def speak(self):
        return self.name + " says woof!"

class Cat():

    def __init__(self,name):
        self.name=name

    def speak(self):
        return self.name + " says meow"

niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())     # nikosays woof!
print(felix.speak())    # felixsays meow

for pet in [niko,felix]:

    print(type(pet))    #<class '__main__.Dog'>
                        # <class '__main__.Cat'>
    print(pet.speak())  #nikosays woof!
                        #felixsays meow

def pet_speak(pet):
    print(pet.speak())
pet_speak(niko)    # felix says meow
pet_speak(felix)   # niko says woof!

#
class Animal():

    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError()

class Dog(Animal):

    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):

    def speak(self):
        return self.name + " says meow!"

fido = Dog("Fido")
isis = Cat("Isis")

print(fido.speak())       # Fido says woof!
print(isis.speak())       # Isis says meow!

#OOP- Speical (Magic/Dunder) Methods

class Book():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")

b=Book("Python rocks","Jose",200)
print(len(b))    #200
del b            #A book object has been deleted




































































































































































































































































































