#for loop= 1.In this you can "iterate" over the object
          #2.you can iterate over every item in a list
          #3.you can iterate over every key in dictionary
#syntax of a for loop
'''
my_iterable=[1,2,3]
for item_name in my_iterable:
    print(item_name)
'''

mylist=[1,2,3,4,5,6,7,8,9,10]
for num in mylist:              #we can use any variable name instead of num like jelly
    print(num)

mylist=[1,2,3,4,5,6,7,8,9,10]
for num in mylist:              #we can use any variable name instead of num like jelly
    print("Hello")
for num in mylist:
    if num%2==0:
        print(num)
    else:
        print(f'odd number:{num}')


list_sum=0
for  num in mylist:
    list_sum = list_sum + num
    #print(list_sum)
print(list_sum)

mystring="helloworld"
for letter in mystring:
    print(letter)
for letter in "Rohan Ghalme":
    print(letter)


tup=(1,2,3,4,5)
for num in tup:
    print(num)


my_list=[(1,2),(3,4),(5,6),(7,8)]
print(len(my_list))
for item in my_list:
    print(item)
for (a,b) in my_list:
    print(a)          #it is known as tuple unpacking
    print(b)
for (a,b)in my_list:
     print(a)

mylist1=[(1,2,3),(5,6,7),(8,9,10)]
for a,b,c in mylist1:
    print(b)
    print(a)

d={'k1':1,'k2':2,'k3':3}
for item in d:          #used when want only key
    print(item)
for item in d.items():  #it used when we want to both key and value
    print(item)
for key,value in d.items(): #used when we want to one of both
    print(value)
for value in d.values():   #used when we want to only values
    print(value)









