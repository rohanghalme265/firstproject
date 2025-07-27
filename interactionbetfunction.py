example=[1,2,3,4,5,6,7]
from random import shuffle
result=shuffle(example)
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result=shuffle_list(example)
print(result)
print(shuffle_list(example))

mylist=['','0','']
print(shuffle_list(mylist))

def player_guess():
    guess=''

    while guess not in ['0','1','2']:
        guess=input("pick a number:0,1,or 2")

    return int(guess)
myindex=player_guess
print(myindex)

def check_guess(mylist,guess):
    if mylist[guess]=='0':
        print('correct')
    else:
        print('wrong guess!')
        print(mylist)

#intial list
mylist=['','0','']

#shuffle list
mixedup_list=shuffle_list(mylist)

#user guess
guess=player_guess()

#check guess
check_guess(mixedup_list,guess)

































































































































































































