#1.Reverse string

text = 'hello'
reversed_text=text[::-1]
print(reversed_text)

text1='Rohan'
reversed_str=text1[::-1]
print(reversed_str)

#2.find second largest number un a array

arr=[12,35,1,10,34,1]
unique=list(set(arr))
unique.sort()
second=unique[-2]
print(second)

arr1=[38,43,33,20,11,30]
unique1=list(set(arr1))
unique1.sort()
second1=unique1[-2]
print(second1)

#3.check if a number is prime
num=7
if num<2:
    print('not prime')
else:
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            print('not prime')
            break
        else:
            print('prime')

num=10
if num < 2:
    print('not prime')

else:
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            print('not prime')
            break
        else:
            print('prime')


if num<2:
    print('not prime')
elif num%2==0:
    print('not prime')
else:
    print('prime')

#4.count vowels in a string

text = 'hello world'
vowels='aeiouAEIOU'
count=0
for char in text:
    if char in vowels:
        count+=1
print(count)

text="Rohan Ghalme"
vowels='aeiouAEIOU'
count=0
for char in text:
    if char in vowels:
        count+=1
print(count)

#5.print a right-angle traingle star pattern
n=4
for i in range(1,n+1):
    print('*'*i)

n=5
for i in range(1,n+1):
    print('*'*i)


#6.find the GCD (Greatest Common Divisor)

a=48
b=18

while b !=0:
    a,b=b, a%b
print(a)

c=100
d=150
while d!=0:
    c,d=d,c%d
print(c)

#7.Check if a string is palindrome
text='madam'
if text==text[::-1]:
    print('YES')
else:
    print("NO")

text_1='radar'
if text_1==text_1[::-1]:
    print('YES')
else:
    print('NO')


#8.rotate an array left by k positions, k=2
arr=[1,2,3,4,5]
k=2
rotated=arr[k:]+arr[:k]
print(rotated)

arr_1=[11,12,13,14,15]
k1=2
rotated_1=arr_1[k1:]+arr_1[:k1]
print(rotated_1)


#9.count the frequency of each character

text='aabbc'
freq={}
for char in text:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)

text_1='aaabbbccddde'
freq={}
for char in text_1:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)

#10.find the sum of digits of a number

num=1234
sum_digits=0
while num > 0:
    sum_digits+=num%10
    num=num//10
print(sum_digits)

num_1=11121314
sumdigits=0
while num_1>0:
    sumdigits+=num_1%10
    num_1=num_1//10
print(sumdigits)

#11.Factorial of a number

num=5
factorial=1
for i in range(1,num+1):
    factorial*=i
print(factorial)

num=8
factorial=1
for i in range(1,num+1):
    factorial*=i
print(factorial)

#12.Fibonacci series up to N terms
n=6
a,b=0,1
for i in range(n):
    print(a,end=' ')
    a,b=b, a+b

n=8
c,d=0,1
for i in range(n):
    print(c,end=' ')
    c,d=d,c+d

#13.print all even numbers in range

start = 1
end = 10
for i in range(start,end+1):
    if i % 2 == 0:
        print(i)

start=10
end=100
for i in range(start,end+1):
    if i%2==0:
        print(i,end=' ')

#14.find largest element in array
arr=[3,9,1,7]
largest=max(arr)
print(largest)

arr=[49,24,58,19]
largest=max(arr)
print(largest)


#15.Count words in a sentence
sentence='TCS NQT coding test'
words=sentence.split()
print(len(words))

sentence='My Name is Rohan Ghalme'
count=sentence.split()
print(len(count))

#16.swap two number
a=3
b=5
a,b=b,a
print('a=',a,'b=',b)

c=49
d=20
c,d=d,c
print('c=',c,'d=',d)

#17.sum of first n natural numbers
n=5
sum=n*(n+1)//2
print(sum)

n=20
sum=n*(n+1)//2
print(sum)

#18.find common elements in two arrays
arr1=[1,2,3]
arr2=[2,3,4]
common=list(set(arr1) & set(arr2))
print(common)

arr3=[5,6,7,8]
arr4=[7,8,9,10]
common=list(set(arr3) & set(arr4))
print(common)

#19.find number of digits
num=12345
digits=len(str(num))
print(digits)

num=1914398374237857
digits=len(str(num))
print(digits)


def matrix(a, b):
    row= len(a)
    col = len(a[0])
    result = []

    for i in range(row):
        row = []
        for j in range(col):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result


a = ([2, 3], [4, 5])
b = ([1, 2], [8, 9])
print('add matrix')
for row in matrix(a, b):
    print(row)

def add_matrix(a,b):
    row = len(a)
    col = len(a[0])
    result = []

    for i in range (row):
        row=[]
        for j in range (col):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result

a=([2,56],[54,12])
b=([1,2],[4,5])
print("addition")
for row in add_matrix(a,b):
    print(row)

def mat(c,d):
    row=len(c)
    col=len(c[0])
    result=[]

    for i in range(row):
        row=[]
        for j in range(col):
            row.append(c[i][j] + d[i][j])
        result.append(row)
    return result
c=([28,39,38],[29,26,39])
d=([82,73,16],[28,37,81])
print("aadd matrix")
for row in mat(c,d):
    print(row)

arr=[38,29,48,29,38,46]
unique=list(set(arr))
unique.sort()
second=unique[-2]
third=unique[-3]
total=second-third
print(total)

