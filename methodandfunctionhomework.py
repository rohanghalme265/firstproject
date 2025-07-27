#Q1.write a function that computes the volume of asphere given its radius

import math


def sphere_volume(radius):
    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume


print(sphere_volume(4))

#Q2.write a function that checks whether a number is in a given range(inclusive of high and low)

def check_in_range(number,low,high):
    if low<=number<=high:
        return  True
    else:
        return False
number=10
low=5
high=15
print(check_in_range(number,low,high))

def check_range(low,num,high):
    if low<=num<=high:
        return True
    else:
        return False
num=14
low=15
high=30
result=check_range(low,num,high)
print('Is',num, "in the range [",low,",",high,"]?",result)

#Q3.write a python function that accepts a string and calculates the number of upper case letters and lower case letters

def count_letters(s):
    upper_count = 0
    lower_count = 0

    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print("Original string:", s)
    print("number of uppercase letter:", upper_count)
    print("number of lowercase letter:", lower_count)


input_string = "MY Name Is Rohan Madhukar Ghalme"
count_letters(input_string)

#Q4.write a python function that takes a list and returns a new list with unique elements of the first list

def unique_elements(my_list):
    new_list=[]

    for item in my_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

numbers=[1,1,1,3,3,3,4,4,2,2,2,6,6,7,7]
print('Original list:',numbers)
print("unique list:",unique_elements(numbers))

#Q5.write python function to multiply all the numbers in a list

def multiply(number):
    result=1
    for num in number:
        result*=num
    return result
numbers=[1,2,3,4,5]
print(multiply(numbers))

#Q6.write a python functionn that check whether a word  or phrase is palindrom or not

def palindrom(s):
    if s==s[::-1]:
        return 'this word is palindrom'
    else:
        return 'this word is not palidrom'
s="Rohan"
print(palindrom(s))
s1='RADAR'
print(palindrom(s1))

#with replace method

def is_palindrom(text):
    result = text.lower().replace(" ", "")
    if result == result[::-1]:
        return True
    else:
        return False

word1 = "Madam"
word2 = "Nurses Run"
word3 = "Python"

print(f"'{word1}' is palindrom?:", is_palindrom(word1))
print(f"'{word2}' is palindrom?:", is_palindrom(word2))
print(f"'{word2}' is palindrom?:", is_palindrom(word3))

#Q7.write a python function to check whether a string is pangram or not
import string
print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)

import string
def is_pangram(sentence):
    alphabet=set(string.ascii_lowercase)   #set of all 26 lowercase letter
    sentence=sentence.lower()              # convert sentence to lowercase
    sentence_letter=set(sentence)

    return alphabet.issubset(sentence_letter)
s1='The quick brown Fox jumps over the lazy dog'
s2='Hello World'
print(f'"{s1}" is pangram?:',is_pangram(s1))
print(f"'{s2}' is pangram?:", is_pangram(s2))
#OR
def is_pangram(sentence):
    sentence=sentence.lower()
    letters=set()

    for char in sentence:
        if char.isalpha():
            letters.add(char)

    return len(letters)==26
s3='The quick brown Fox jumps over the lazy dog'
print(f'"{s3}" is pangram?:',is_pangram(s1))


































































