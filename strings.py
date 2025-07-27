#string:- string are sequences of characters.it uses syntax of single or double quotes
#ex, "hello" ,'rohan',"my name is rohan"
#indexing allows you to grab a single character from the string.It uses [] notation
#SLicing allows you to subsection of multiple characters
#[start:stop:step]

# print("hello \n world")

# std="my name is rohan"
# print(len(std))

#String indexing and slicing

# mystring="hello World"
# std=mystring[0]
# print(std)
# std1=mystring[-8]
# print(std1)

#slicing:-

# name="rohanghalme"
# name1=name[:8]
# print(name1)
# name2=name[3:10]
# print(name2)
# name3=name[::]
# print(name3)
# name4=name[0:9:2]
# print(name4)
# name5=name[2:8:1]
# print(name5)
# name6=name[::-1]
# print(name6)
# name7=name[3]
# print(name7)

#String Properties and Methods

# name="Sam"
# letter=name[1:]
# print(letter)
# lastlet="p"+letter
# print(lastlet)

# X="hello world"
# X=X + " it is beautiful outside! "
# print(X)
# print(X*3)
# print('2'+'3')

# X='Hello World'
# X1=X.upper()
# print(X1)

# F='Hello World'
# F1=F.lower()
# print(F1)

# A='My name is Rohan'
# A1=A.split()
# print(A1)
# A2=A.split('a')
# print(A2)

# name='Rohan'
# name1=name[0:4:1]
# print(name1)

#multi-line string
poem="""Roses are red,
violets are blue,
Python is fun,
And so are you."""
print(poem)

#string Indexing and Slicing
word='rohan ghalme'
print(word[4])  #n
print(word[-4])  #a
print(word[1:-3:1]) #ohan gha
print(word[0:8])    #rohan gh

#Comman string Methods
name="ROHAN"
print(name.lower())   #rohan
print("Yash".lower()) #yash

name1="rohan"
print(name1.upper())  #ROHAN
print('pratik'.upper()) #PRATIK

name2="python language"
print(name2.capitalize())  #Python language
print('omkar'.capitalize())  #Omkar

name3='my name is rohan'
print(name3.title())    #My Name Is Rohan
print("sinhgad collage of engineering".title())  #Sinhgad Collage Of Engineering

name4="apple"
print(name4.replace('e','c'))  #applc
print('pomogranate'.replace('n','c'))  #pomogracate

name5='a,b,c,d'
print(name5.split())      #['a,b,c,d']
print('k,a,r,t'.split())  #['k,a,r,t']

std=['a','b','c','d']
std1=" ".join(std)
print(std1)  #a b c d
print(" ".join(std))  #a b c d

name6="Rohanghalme"
print(name6.startswith('R'))   #True
print(name6.endswith('e'))     #True
print('pratik'.startswith("P"))  #False
print("pratik".endswith('i'))   #False

name7='aadarsh'
print(name7.count("a"))  #3
print(name7.find("d"))   #2

a="Hello"
b="World"
print(a+" "+b)   #Hello World

#Repetition
c="hi"
print("hi "* 3)  # hi  hi  hi

print("a" in "apple")  #True
print("z" not in "apple") #True





















































