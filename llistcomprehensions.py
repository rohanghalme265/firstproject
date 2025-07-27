#List coprehensions:- List comprehensions are a unique way of quickly creatinig a list with python
#It allows you to  create a new list by applying an expression to each item in an existing iterable

mystring='hello'
mylist=[]
for letter in mystring:
    mylist.append(letter)
    print(mylist)

my="rohan"
my1=[letter for letter in my]
print(my1)            #['r', 'o', 'h', 'a', 'n']

mylist1=[x for x in 'omkar' ]
print(mylist1)   #['o', 'm', 'k', 'a', 'r']

mylist2=[num for num in range(1,10)]
print(mylist2)   #[1, 2, 3, 4, 5, 6, 7, 8, 9]

mylist3=[num**2 for num in range(1,11)]
print(mylist3)     #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

mylist4=[x**2 for x in range(1,20) if x%2==0]
print(mylist4)  #[4, 16, 36, 64, 100, 144, 196, 256, 324]

celcius=[1,10,20,34.5]
fahrenheit=[((9/5)*temp+32) for temp in celcius]
print(fahrenheit)     #[33.8, 50.0, 68.0, 94.1]

celcius=[10,20,30,40,50]
fahrenheit=[]
for temp in celcius:
    fahrenheit.append(temp * (9 / 5) + 32)
    print(fahrenheit)

results=[x if x%2==0 else 'odd' for x in range(0,11)]
print(results)  #[0, 'odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd', 10]

#nested loop
mylist=[]
for x in [1,2,3,4,5]:
    for y in [100,200,300]:
        mylist.append(x + y)  # we can also do multiplication , division and other
        print(mylist)

mylist1=[x*y for x in [1,2,3,4] for y in [1,10,100,1000] ]
print(mylist1)











































