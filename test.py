#Use for, .spli() and if to create a statement that will print out word that starts with 's'

st='Sam print only the words that starts with s in this sentence'
for word in st.split():
    if word[0]=='s' or word[0]=="S":
        print(word)

#Use range () to print all the even numbers from 0 to 10
for num in range(1,11):
    if num%2==0:
        print(num)

#Use a list Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3

mylist=[x for x in range(1,51) if x%3==0 ]
print(mylist)

#GO through the string below and if the length of a word is even print "even"
st1='print every word in this sentence that has an even number of letters'
for word in st1.split():
    if len(word)%2==0:
        print(word+' is even')

#
'''Write a program that prints the integer from 1 to 100 but for multiples of three print "fizz"
instead of the number,and for the multiples of five "Buzz". for numbers which are multiples of both three and five print 'FizzBuzz'''

for num in range(1,101):
    if num%3==0 and num%5==0:
        print('FizzBuzz')
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)

#Use list coprehension to create a list of the  first letters of every word in the string below

st3='Create a list of the first letters of every word in this string'
st4=[word[0] for word in st3.split()]
print(st4)       #['C', 'a', 'l', 'o', 't', 'f', 'l', 'o', 'e', 'w', 'i', 't', 's']






