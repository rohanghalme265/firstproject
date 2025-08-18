# if, elif and else:-

#syntax for an statement-
'''

if some_condition
        execute some code
elif some_other_condition:
         do something different
else:
        do something else

'''

hungry=True
if hungry:
    print('Feed Me')    #Feed Me
else:
    print('I am not hungry')


hungry1=False
if hungry1:
    print('Feed Me')   #we don't get back any output
else:
    print('I am not hungry')

loc='Bank'
if loc=='Auto shop':
    print('Cars are cool')
elif loc=='Bank':
    print('Money is cool!')
elif loc=='Store':
    print('Welcome to the Store')   #with help of elif statement we can get many condition
else:
    print('I do not know much')

name='sammy'
if name=='Frankie':
    print("Hello Frankie!")
elif name=='sammy':
    print('Hello sammy!')
else:
    print("what is your name")

# age = int(input())
# if(age>=18):
#     print("Eligible for Driving License")
# else:
#     print("Not Eligible for driving License")

# age = int(input())
# if (age>=18):
#     test = input()
#     if test=="PASS":
#         print("Eligible for Driving License")
#
#     else:
#         print("not Eligible for Driving License")
#
# else:
#     print("Not Eligible for Driving License")

#

# marks = int(input())
# >=90 Excellent
# 70-90 Good
# 40-70 Fair
# <40 Bad

# if marks>=90:
#     print('Excellent')
# elif marks>=70:
#     print('Good')
# elif marks>=40:
#     print('Fair')
# else:
#     print('Bad')

#for join two statement

# temp = int(input())
# 25-50->  Hot
# 10-24->  Cold
# <10 -> Extremely Cold

# if temp>=50 and temp>=25:
#     print("Hot")
# elif temp<=24 and temp>=10:
#     print("Cold")
# else:
#     print("Extremely Cold")


#Ternary Operator

# age = int(input())
# result = "ELigible" if age>=18 else "not Eligible"
# print(result)


# PRACTICE PROBLEMS

# class Solution:
#     def fizzbuzz(self, n: int):
#         ans = []
#         for i in range(1,n+1):
#             if i%3==0 and i%5==0:
#                 ans.append("FizzBuzz")
#             elif i%3==0:
#                 ans.append("Fizz")
#             elif i%5==0:
#                 ans.append("Buzz")
#             else:
#                 ans.append(str(i))
#         return ans
#
# sol = Solution()
# result = sol.fizzbuzz(15)
# print(result)

#2.how many odd numbers between intervels

# class Solution:
#     def countOdds(self,low,high):
#         return (high+1)//2 - (low//2)
#
# sol = Solution()
# result = sol.countOdds(10,100)
# print(result)


# BASED ON NESTED LOOP

# class Solution:
#     def smallerNumberThanCurrent(self,nums):
#         ans = []
#         for i in nums:
#             c=0
#             for j in nums:
#                 if j<i:
#                     c+=1
#             ans.append(c)
#         return ans
# sol = Solution()
# result = sol.smallerNumberThanCurrent([57,86,7,9,54,90,78])
# print(result)


#COUNT THE DIGITS THAT DIVIDE A NUMBER
'''
Given an integer num,return the number of digits in num that divide num,An integer val divides nums if nums % val == 0
'''

# class Solution:
#     def countDigit(self,num:int):
#         temp = num
#         ans = 0
#         while temp>0:
#             r = temp%10
#             if num%r==0:
#                 ans+=1
#             temp//= 10
#
#         return ans
# obj = Solution()
# print(obj.countDigit(121))


#GIVEN AN INTEGER X,RETURN TRUE IF X IS A PALINDROME,AND FALSE OTHERWISE.

# class Solution:
#     def isPalindrome(self,x:int):
#         temp = x
#         rev = 0
#
#         while temp>0:
#             r = temp%10
#             temp//=10
#             rev = rev*10 + r
#
#         return rev==x
#
# obj = Solution()
# print(obj.isPalindrome(121))
# print(obj.isPalindrome(123))
# print(obj.isPalindrome(1221))


# SUBTRACT THE PRODUCT AND SUM OF DIGITS OF AN INTEGER

class Solution:
    def isPalindrom(self,n:int):
        temp = n
        sum_ = 0
        product = 1

        while temp>0:
            r = temp%10
            temp//=10
            sum_+=r
            product*=r

        return product-sum_

sol = Solution()
num = 123
result = sol.isPalindrom(num)

print(f"Input: {num}")
print(f"Product - Sum of digits = {result}")

#KIDS WITH THE GREATEST NUMBEROF CANDIES

class Solution:
    def kidsWithCandies(self,candies:list[int],extraCandies: int):
        maxCandies = max(candies)
        ans = []

        for i in candies:
            if (i+extraCandies)>=maxCandies:
                ans.append(True)
            else:
                ans.append(False)

        return ans









