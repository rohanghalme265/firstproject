#Q1.write a function that returns the lesser of two given numbers if both numbers are even , but returns the greater if one or both numbers are odd
from operator import truediv

from printing import result


def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        #if both numbers are even
        if a<b:
            return a
        else:
            return b
    else:
        #one or both numbers are odd
        if a>b:
            return a
        else:
            return b
print(lesser_of_two_evens(22,44))

def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)
print(lesser_of_two_evens(63,88))\

#Q2.writw a function takes a two-word string and returns True if both words with same letter

def animal_crackers(text):
    wordlist=text.split()
    print(wordlist)

    first = wordlist[0]
    second= wordlist[1]

    return first[0]==second[0]
print(animal_crackers('levelheaded llama'))
print(animal_crackers('crazy kangaroo'))

def animal_crackers(text):
    wordlist=text.lower().split()
    print(wordlist)

    return wordlist[0][0]==wordlist[1][0]
print(animal_crackers('crazy Cat'))

#Q3.Given two integers,return True if the sum of the integers is 20 or if one of the integers is 20.if not ,return False

def makes_twenty(n1,n2):
    if n1+n2==20:
        return True
    elif n1==20:
        return True
    elif n2==20:
        return True
    else:
        False
print(makes_twenty(10,10))
#OR
def makes_twenty(n1,n2):
    return (n1+n2)==20  or n1==20 or n2==20
print(makes_twenty(2,21))

#level 1
#Q1.write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):

    first_letter=name[0]
    inbetween=name[1:3]
    fourth_letter=name[3]
    rest=name[4:]

    return first_letter.upper() + inbetween + fourth_letter.upper() + rest
print(old_macdonald('macdonald'))
#OR
def old_macdonald(name):

    first_half=name[:3]
    second_half=name[3:]

    return first_half.capitalize()+second_half.capitalize()
print(old_macdonald('macdonald'))

#Q2.Given a sentence,return a sentence with the words reversed

mylist=['a','b','c']
print(' '.join(mylist))

def master_yoda(text):
    wordlist=text.split()
    reverse_word_list=wordlist[::-1]
    return ' '.join(reverse_word_list)
print(master_yoda('My Name is Rohan'))

#Q3.Given an integer n, return True if n is within 10 0f either 100 or 200
#note:-abs(num)returns the absolute value of a number

def almost_there(n):
    return (abs(100-n)<=10 or (200-n)<=10)
print(almost_there(180))
print(almost_there(99))

#level2
#Q1.Given a list of ints,return True if thr array contains a 3 next to 3 somewhere

def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False
print(has_33([1,3,3,4,5,6]))
print(has_33([3,3,4,23,564]))
print(has_33([11,22,33,44,33]))

#Q2.Paper DOll:given a string , return a string where for every character in the original there are three character

def paper_doll(text):
    result=''
    for char in text:
         result+=char+char+char    #we can also write this as a resul+=char*3
    return result
print(paper_doll('Rohan'))
print(paper_doll('babayaga'))

#Q3.Given three integers between 1 and 11 , if their sum is less thsn or equal to 21 , return their sum.if their sum exceeds 21 and there's an eleven, reduce the total sum by 10. finally if the sum (even after adjustment)exceeds 21, return 'BUST'

def black_jack(a,b,c):

    if sum([a,b,c])<=21:
        return sum([a,b,c])
    elif sum([a,b,c])>21 and 11 in (a,b,c):
        return sum([a,b,c])-10
    else:
        return "BUST"
print(black_jack(11,9,8))
print(black_jack(9,8,7))
print(black_jack(7,6,5))

#Q4.Return the sum of the numbers in the array expect ignore section of numbers starting with a 6 and extending
# to the next 9(every 6 will be followed by at least one 9).Return 0 for no numbers.

def summer_69(arr):

    total=0
    add=True

    for num in arr:
        while add:
            if num!=6:
                total+=num
                break
            else:
                add=False
        while not add:
            if num!=9:
                break
            else:
                add=True
                break
    return total
print(summer_69([1,2,3,6,7,9,10]))
print(summer_69([10,3,4,2,6,7,10,9,11]))

#Challanging problem
#Q1.Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):

    code=[0,0,7,'x']

    for num in nums:
        if num ==code[0]:
            code.pop(0)
    return len(code)==1
print(spy_game([1,2,0,3,4,0,8,9,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#Q2.write a function that returns the number of prime numbers that exist up to and including a given number
#By convention we'll treat 0 and 1 as not prime

def count_prime(num):
    #Check for 0 and 1 input
    if num<2:
        return 0

    #Store our prime numbers
    primes=[2]
    #Counter going up to the input num
    x=3

    #x is going through every number up to input num
    while x <=num:
        #checking if x is prime
        for y in range(3,x,2):
            if x%y==0:
                x+=2
                break
        else:
            primes.append(x)
            x+=2
    print(primes)
    return len(primes)
print(count_prime(200))


def std(num):
    if num<2:
        return 0

    primes=[2]
    x=3

    while x<=num:
        for y in range(3,x,2):
            if x%y==0:
                x+=2
                break
        else:
            primes.append(x)
            x+=2

    print(primes)
    return len(primes)
print(std(300))





















































































