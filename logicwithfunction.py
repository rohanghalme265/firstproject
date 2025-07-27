def even_check(number):
    return number % 2 == 0
print(even_check(30))         #True

def even_check(number):
    print(number%2==0)
even_check(30)           #True

#Return True if any number is even inside a list

def check_even_list(num_list):
    for number in num_list:
        if number % 2 ==0:
           return True
        else:
            pass                   #pass keyword means dot do anything
    return False
print(check_even_list([2,4,6,8]))  #True
print(check_even_list([2,1,3,4,5])) #True    #if the first num is even then condition is True
print(check_even_list([1,4,3,5,7,8])) #True    #if th last num is even then condition is True
print(check_even_list([1,3,9,7])) #None      #if there is no even number in list then the coditionn is False

def even_check_list(num_list):
    for number in num_list:
        if number % 2==0:
            return True
        else:
            return False
print(even_check_list([2,4,6,8,0]))  #True
print(even_check_list([1,3,5,7,9]))   #False
print(even_check_list([2,1,4,3,5,6,7,8]))  #True
print(even_check_list([2,1,3,5,7,9]))     #True
print(even_check_list([1,2,3,4,5,6,7,8,9,2]))   #False
print(even_check_list([1,2,3,4,5,6,7]))  #False

def even_list(list):
    for number in list:
        if number %2==0:
            print("True")
        else:
            print("False")
even_list([2,4,6,8,3])

def list_num(num_list):
    even_number=[]
    for number in num_list:
        if number%2==0:
            even_number.append(number)
        else:
            pass
    return even_number
print(list_num([21,4,5,6,7,8,9,3]))   #[4, 6, 8]
print(list_num([1,2,33,44,56,72,888]))  #[2, 44, 56, 72, 888]
















































































































































