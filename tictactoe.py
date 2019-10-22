
import random

def display_board(board):
    print('\n'*100)
    print("   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")
    print("- - - - - - ")
    print("   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("   |   |   ")
    print("- - - - - - ")
    print("   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("   |   |   ")



def player_input():
    while True:
        marker = input("Player 1: Please pick either 'X' or 'O': ")
        if marker.upper() == 'O':
            return ('O','X')
        elif marker.upper() == 'X':
            return ('X', 'O')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[7] == mark and board[4] == mark and board[1] == mark:
        return True
    elif board[7] == mark and board[5] == mark and board[3] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[8] == mark and board[5] == mark and board[2] == mark:
        return True
    elif board[9] == mark and board[6] == mark and board[3] == mark:
        return True
    else:
        return False


def choose_first():
    player = random.randint(1,2)
    if player == 1:
        return "Player 1"
    else:
        return "Player 2"



def space_check(board, position):
    return board[position] != 'O' and board[position] != 'X'



def full_board_check(board):
    return len(list(filter(lambda letter: letter != 'O' and letter != 'X',board[1:]))) == 0



def player_choice(board):
    while True:
        position = int(input("What position would you like to play?: "))
        if position in range(1,10):
            if space_check(board, position):
                return position
            else:
                print(f"Position {position} is not avaiable. Please Try Again!")
        else:
            print(f"Position {position} is not avaiable. Please Try Again!")



def replay():
    while True:
        replay = input("Do you want to play again? Y or N: ")
        if replay.lower() == 'y' or replay.lower() == 'n':
            return replay.lower() == 'y'
        else:
            print("Please enter either Y or N")



print('Welcome to Tic Tac Toe!')
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
playerChoice = player_input()
playerOneLetter = playerChoice[0]
playerTwoLetter = playerChoice[1]
firstMove = choose_first()
playerOneMove = True
print("\n" + firstMove + ' will go first!\n\n')
if firstMove == 'Player 2':
    playerOneMove = False

while True:
    gameOver = False
    display_board(board)
    if playerOneMove:
        position = player_choice(board)
        place_marker(board,playerOneLetter,position)
        if win_check(board, playerOneLetter):
            display_board(board)
            print("Congrats Player 1! You are the winner!")
            gameOver = True
        if full_board_check(board):
            display_board(board)
            print("Board is full. Nobody wins. You both are losers!")
            gameOver = True
        playerOneMove = False
    else:
        position = player_choice(board)
        place_marker(board,playerTwoLetter,position)
        if win_check(board, playerTwoLetter):
            display_board(board)
            print("Congrats Player 2! You are the winner!")
            gameOver = True
        if full_board_check(board):
            display_board(board)
            print("Board is full. Nobody wins. You both are losers!")
            gameOver = True
        playerOneMove = True
        
    if gameOver:
        if replay():
            gameOver = False
            board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            firstMove = choose_first()
            print("\n" + firstMove + ' will go first!\n\n')
            if firstMove == 'Player 2':
                playerOneMove = False
            else:
                playerOneMove = True
            continue
        else:
            break


