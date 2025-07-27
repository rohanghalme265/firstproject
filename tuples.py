#Tuples () :- It is similar to the list
#it is immutable
#Once an element is inside a tuple, it can not be reassigned

t=(1,2,3,4)
mylist=[1,2,3]
print(type(t))
print(type(mylist))

t1=('one',2,34,'rohan')
print(t1[2])

t2=('a','a','b','c')
print(t2.count('a'))
print(t2.index('a'))
print(t2.index('b'))
print(t2[2])

info=("Rohan",21,True,3.9)
print(info[0])     #Rohan
print(info[3])     #3.9

empty=()
print(empty)         #()
print(type(empty))   #<class 'tuple'>

#single-element tuple
'''
In this comma is required otherwise it won't consider it as a tuple
'''
t3=(5,)
print(type(t3))  #<class 'tuple'>
t4=(5)
print(type(t4))  #<class 'int'>

t5=(1,1,2,3,4,4,5,6)
print(t5)  #(1, 1, 2, 3, 4, 4, 5, 6) duplicates are not eliminated
print(t5.count(1))    #2
print(t5.count(4))    #2

#Accessing tuple elements
t6=('a','b','c','d','e')
print(t[3])    #d
print(t[-4])   #b

#Slicing tuples
t7=(10,20,30,40,50,60)
print(t7[2:-1:2])    #(30, 50)

#Loop through a tuple
t8=('apple',"banana","cherry")
for item in t8:
    print(item)

t9=[1,(2,3),4,(5,6)]
print(t9[3][1])    #6
print(t9[1][0])    #2

#tuple with list inside
tup=(1,2,[3,4])         #tuple is immutable but list inside tuple is mutable
tup[2][0]=9
print(tup)       #(1, 2, [9, 4])

#Tuple from a string
s=tuple("hello")
print(s)       #('h', 'e', 'l', 'l', 'o')

#Tuple from list
l=[1,2,3,4,5]
print(tuple(l))   #(1, 2, 3, 4, 5)

#Tuple Unpacking
a,b,c=(10,20,30)
print(a)   #10
print(c)   #30
print(a,b,c)    #10 20 30

#Tuple with Repeated elements
repeated=(5,)*4
print(repeated)   #(5, 5, 5, 5)

repeat=("Rohan",)*4
print(repeat)      #('Rohan', 'Rohan', 'Rohan', 'Rohan')

#tuple with range
p=tuple(range(1,6))
print(p)           #(1, 2, 3, 4, 5)




































