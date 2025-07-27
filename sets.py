#Sets:--Sets are unordered collection of unique elements
#there can only be one representative of the same object

s=set()
s.add(1)
print(s)
s.add(2)
print(s)

s1=[1,1,1,2,2,2,3,3,3,4,4,4]
print(set(s1))
print(s1[2])

#creating a list
my_set={1,2,3,4}
print(my_set)

#Duplicate Values are Removed
numbers={1,1,2,3,3,4,5,6,6,7}
print(numbers)     #{1, 2, 3, 4, 5, 6, 7}

#Add Elements to Set
fruits={"Apple","Banana","graps"}
fruits.add("cherry")        #{'cherry', 'Apple', 'Banana', 'graps'}
print(fruits)

#Remove Elements from a Set
colours={'red','blue','black','white'}
colours.remove("red")
print(colours)          #{'blue', 'black', 'white'}

#Set Union
a={1,2,3}
b={4,5,6}
print(a.union(b))    #{1, 2, 3, 4, 5, 6}
print(b.union(a))    #{1, 2, 3, 4, 5, 6}

#Set Intersection
a1={1,2,3,4,5}
b1={3,4,5,6,7}
print(a1.intersection(b1))    #{3, 4, 5}

#Set Difference
a2={1,2,3,4,5}
b2={4,5,6,7,8}
print(a2.difference(b2))  #{1, 2, 3}
print(b2.difference(a2))  #{8, 6, 7}

#Set Symmetric Difference
a3={1,2,3,4}
b3={4,5,6,7}
print(a3.symmetric_difference(b3))    #{1, 2, 3, 5, 6, 7}
print(b3.symmetric_difference(a3))    #{1, 2, 3, 5, 6, 7}

#check if an item exists
my_set={"apple","banana","cherry"}
print("banana" in my_set)         #True

num={1,2,3,4,5,6,7}
print(8 in num)      #False

#Convert list to set to remove duplicates
nums=[1,2,3,3,4,5,6,6,7,8]
print(set(nums))      #{1, 2, 3, 4, 5, 6, 7, 8}




















