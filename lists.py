#List:-It is ordered sequences that can hold a variety of object types
#support indexing andd slicing
#Objects retrived by location
#Ordered sequence can be indexed or sliced


list1=['STRING',100,32,4.5]
print(len(list1))
list=['one','two','three','four']
print(list[0])
lists=list[1:]
print(lists)
another_list=['five','six','seven','eight']
list2=list + another_list
print(list2)
list2[0]='ONE ALL CAPS'
print(list2)
list2.append('nine')    #Used for adding
print(list2)
list2.pop()
print(list2)
popped_item =list2.pop()
print(popped_item)
print(list2)
list2.pop(3)
print(list2)
list3=list2[3]
print(list3)

new_list=['a','e','x','b','c']
num_list=[4,1,8,3]
new_list.sort()
print(new_list)
my_sorted_list=new_list.sort()
print(my_sorted_list)
my_sorted_list=new_list
print(my_sorted_list)
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
new_list.remove('a')
print(new_list)












