#First off, make sure you understand the project scope
#what needs to happen?
'''
1].We need to print a board
2].Take in player input
3].place their input on the board
4].check if the game is won,tied,lost,or ongoing
5].Repeat c and d until the game has been won or tied
6].Ask if players want to play again
'''


#Step1-write a function that can print out a board.Set up your board as a list where each index 1-9 corresponds with a number pad so you get a board representation

def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
test_board=['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

#Step2- Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while
#loops to continually ask until you get a correct answer

def player_input():
    marker=''
    #Keep asking player 1 to choose X or O
    while marker !='X' and marker!='O':
        marker=input('player 1: choose X or O:').upper()

    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

player1_marker , player2_marker=player_input()

#la
#Step3-Write a function that makes in the board list object, a marker('X' or 'O'),and a desired position(number 1-9) and
# assign it to the board

def place_marker(board, marker,position):
    board[position]=marker

place_marker(test_board,'$',8)
display_board(test_board)


#Q4.Write a function that takes in a board and a mark(X or O) and then checks to see if that mark has won

def win_check(board,mark):


    return (
        (board[7] == board[8] == board[9] == mark) or     #across the
        (board[4] == board[5] == board[6] == mark) or     #across the middle
        (board[1] == board[2] == board[3] == mark) or     #across the bottom
        (board[7] == board[4] == board[1] == mark) or     #down the middle
        (board[8] == board[5] == board[2] == mark) or     #down the middle
        (board[9] == board[6] == board[3] == mark) or     #down the right side
        (board[7] == board[5] == board[3] == mark) or     #diagonal
        (board[9] == board[5] == board[1] == mark)        #diagonal

    )

display_board(test_board)
print(win_check(test_board,'X'))

#Q5.write a function that uses the random module to randomly decide which player goes first.You may want to lookup
#random.randint() Return a string of which player went first

import random

def choose_first():

    flip=random.randint(0,1)

    if flip==0:
        return 'player 1 '
    else:
        return 'player 2 '
first_player=choose_first()
print(first_player + "will go first")

#Step6.write a function that returns a boolean indicating whether a space on the board is freely available

def space_check(board,position):
    return board[position]==' '
test_board=['#','X','O',' ','X',' ','O','X',' ','O']

def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
display_board(test_board)

#Check a few spaces
print(space_check(test_board,3))
print(space_check(test_board,1))

#step7.write a function that checks if the board is full and returns a boolean value.True if full ,False otherwise


def full_board_check(board):
    for i in range(1,10):
        if board[i]==' ':
            return False
    return True

def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

test_board_full=['#','X','O','X','O','X','O','X','O','X']
display_board(test_board_full)
print(full_board_check(test_board_full))

test_board_not_full=['#','X','O',' ','O','X','O','X','','X']
display_board(test_board_not_full)
print(full_board_check(test_board_not_full))

#step8.write a function that asks for a player's next position(as a number 1-9) and then uses the function from step 6 to check
#if it's a free position.if it is then return the position for later use

def player_choice(board):
    position = 0  # Initial invalid position to enter the loop

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Choose your next position (1-9): "))  # Ask for input

    return position

# Helper function from Step 6 to check if a position is free
def space_check(board, position):
    return board[position] == ' '

# Example: partially filled board
test_board = ['#', 'X', 'O', 'X', ' ', ' ', 'O', 'X', ' ', 'O']

# Display the board for reference
def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

# Show the current board
display_board(test_board)

# Ask the user to choose a valid position
chosen_pos = player_choice(test_board)
print("You chose position:", chosen_pos)

#step9.Write a function that asks the player if they want to play again and returns a boolean True if they want do want to play again

def replay():
    choice = input("Do you want to play again? Enter Yes or No: ").lower()
    return choice.startswith('y')

print(replay())
#step10.Here it comes the hard part! Use while loops and the function you've made to run the game

print('Welcome to Tic Tac Toe!')

while True:
    # Set up the board
    the_board = [' '] * 10  # Index 0 is ignored
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Ready to play? Enter Yes or No: ').lower()
    if play_game.startswith('y'):
        game_on = True
    else:
        game_on = False

    while game_on:
        # Player 1's turn
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Congratulations! Player 1 has won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 2'

        # Player 2's turn
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


































































































































































































































































