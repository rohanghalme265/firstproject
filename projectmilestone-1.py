# Displaying some information

# def display(row1, row2, row3):
#     print(row1)
#     print(row2)
#     print(row3)
#
#
# row1 = [1, 2, 3]
# row2 = [4, 5, 6]
# row3 = [7, 8, 9]
# display(row1, row2, row3)
#
# row1 = [' ', ' ', ' ']
# row2 = [' ', ' ', ' ']
# row3 = [' ', ' ', ' ']
# row2[1] = 'X'
# display(row1, row2, row3)

# Accepting User Input

# input('please enter a value:')
#
# result=input('please enter a value:')
# print(type(result))
#
# result_int=int(result)
# print(type(result))

# position_index=int(input("choose an index position:"))
# print(type(position_index))
#
# print(row2[position_index])

# Validating user input
# for checking user input is number or not we have to use isdigit()

# def user_choice():
#     choice=input("input enter a number (0-10):")
#     return choice
# # print(user_choice())
# some_value='100'
# print(some_value.isdigit())
# print(int(some_value))
#
#
# def user_choice():
#     choice = 'WRONG'
#
#     while choice.isdigit() == False:
#
#         choice = input("Please enter a number (0-10):")
#         if choice.isdigit()==False:
#             print("Sorry that is not a digit")
#
#
#     return int(choice)
# print(user_choice())
#
# result='WRONG VALUE'
# acceptable_value=[0,1,2]
# print(result in acceptable_value)

# def user_choice():
#
#     #variables
#     choice="WRONG"
#     acceptable_range=range(0,10)
#     within_range=False
#
#     #two condition to check
#     #digit or within_range==False
#     while choice.isdigit()==False or within_range==False:
#
#         choice=input('Please enter a number (0-10):')
#
#         #Digit check
#         if choice.isdigit()==False:
#             print("sorry that is not a digit!")
#
#         #Range check
#         if choice.isdigit()==True:
#             if int(choice) in acceptable_range:
#                 within_range=True
#             else:
#                 print('Sorry, you are out of acceptable range (0-10)')
#                 within_range=False
#
#     return int(choice)
#
# print(user_choice())


# Simple user interaction

#we start with display function

game_list=[0,1,2]

def display_game(game_list):
    print("Here is the current list:")
    print(game_list)
display_game(game_list)

def position_choice():
    choice='wrong'

    while choice not in ['0','1','2']:
        choice=input('pick a position (0,1,2):')

        if choice not in ['0','1','2']:
            print("Sorry,invalid choice! ")

    return int(choice)
print(position_choice())

def replacement_choice(game_list,position):
    user_placement=input("Type a string to place at positon:")
    game_list[position]=user_placement
    return game_list
print(replacement_choice(game_list,0))

def gameon_choice():
    choice='wrong'

    while choice not in ['Y','N']:

        choice=input('Keep playing? (Y or N)')

        if choice not in ['Y','N']:
            print("Sorry, I don't understand,please choose Y or N")

    if choice == 'Y':
        return True
    else:
        return False
print(gameon_choice())

game_on=True
game_list=[0,1,2]
while game_on:
     display_game(game_list)
     position=position_choice()
     game_list=replacement_choice(game_list,position)
     display_game(game_list)
     game_on=gameon_choice()
    






















































































