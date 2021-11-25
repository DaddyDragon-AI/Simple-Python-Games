# BOARD DISPLAY
def display_board(board):
    print('\n'*50)
    print(f'Player 1: {player1_marker} - PLayer 2: {player2_marker}')
    print(' ',board[1],'|',board[2],'|',board[3])
    print('-------------')
    print(' ',board[4],'|',board[5],'|',board[6])
    print('-------------')
    print(' ',board[7],'|',board[8],'|',board[9])

# GUIDE
def guide ():
    print("Board Position Guide:")
    print(' ',1,'|',2,'|',3)
    print('-------------')
    print(' ',4,'|',5,'|',6)
    print('-------------')
    print(' ',7,'|',8,'|',9)
    print('In this game 2 players will place X or O marker in to position from 1 to 9 on the board above')
    print('until one of the player form a horizontal, vertical or diagonal line of 3 of their marker, that')
    print('player win the game, if no one form any line of 3, the players tied!')
    print("LET'S GO!")

# PLAYER CHOOSE MARKER
def marker_input():
    marker = 'wrong'
    while marker not in ['X','O']:
        marker = input('Player 1, do you want to be X or O:').upper()
        if marker not in ['X','O']:
            print('That is not a valid marker!')
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

# CHECK FOR BLANK SPACES
def space_check(board, position):
    
    return board[position] == ' '

# CHECK FULL BOARD FOR BLANK SPACES
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# PLAYER'S INPUT
'''def player_input(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        if position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
            print('There are no valid position for that, please pick another position')
    return position'''

def player_input(board):
    position = 0
    
    while True:
        try:
            while (position not in [1,2,3,4,5,6,7,8,9]
                            or not space_check(board, position)):
                position = int(input('Choose your next position: (1-9) '))
                if (position not in [1,2,3,4,5,6,7,8,9]
                             or not space_check(board, position)):
                    print('There are no valid position for that,please pick another position')
        except:
            print('There are no valid position for that, please pick another position')
            continue
        else:
            break
    return position

# AI's INPUT

#PLACE MARKER IN TO THE BOARD
def place_marker(board, marker, position):
    board[position] = marker

# CHECK WIN CONDITION:
def winning_condition(board,mark):
    return ((board[1] == board[2] == board[3] == mark) #first horizontal
    or (board[1] == board[4] == board[7] == mark) #first vertical
    or (board[1] == board[5] == board[9] == mark) #first diagonal
    or (board[2] == board[5] == board[8] == mark) #2nd vertical
    or (board[3] == board[6] == board[9] == mark) #3rd vertical
    or (board[4] == board[5] == board[6] == mark) #row 2 horizontal
    or (board[7] == board[8] == board[9] == mark) #row 3 horizontal
    or (board[3] == board[5] == board[7] == mark)) #3rd diagonal

# RANDOM FOR FIRST PLAYER
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# REPLAY SYSTEM
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

################################
#            MAIN              #
################################

# GREETINGS AND GUIDE
print('HELLO AND WELCOME TO: TIC TAC TOE')
guide()

# MAIN LOOP
while True:
    # RESET BOARD:
    theBoard = [' ']*10

    # SET PLAYER INPUT
    player1_marker, player2_marker = marker_input()

    # RANDOM WHO GO FIRST
    turn = choose_first()
    print(f'{turn} will go first!')
    print(f'Player 1: {player1_marker} - PLayer 2: {player2_marker}')
    
    # GAMEPLAY CONFIRMATION
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    # GAMEPLAY LOOP
    while game_on:
        # PLAYER 1 TURN
        if turn == 'Player 1':
            display_board(theBoard)
            print('Player 1 turn')
            position = player_input(theBoard)
            place_marker(theBoard, player1_marker, position)
            
            # CHECK IF WIN CONDITION MET
            if winning_condition(theBoard,player1_marker):
                display_board(theBoard)
                print('Congratulations! Player 1 have won the game!')
                game_on = False
            
            # CHECK IF THE GAME IS DRAW
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                
                # IF NO CONDITION IS MET, RETURN THE TURN TO PLAYER 2
                else:
                    turn = 'Player 2'

        # PLAYER 2 TURN
        else:
            display_board(theBoard)
            print('Player 2 turn')
            position = player_input(theBoard)
            place_marker(theBoard, player2_marker, position)
            
            # CHECK IF WIN CONDITION MET
            if winning_condition(theBoard,player2_marker):
                display_board(theBoard)
                print('Congratulations! Player 2 have won the game!')
                game_on = False
            
            # CHECK IF THE GAME IS DRAW
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                
                # IF NO CONDITION IS MET, RETURN THE TURN TO PLAYER 1
                else:
                    turn = 'Player 1'   

    # ASK PLAYERS IF THEY WANT TO PLAY AGAIN - IF NOT THEN END MAIN LOOP        
    if not replay():
        print('THANKS FOR PLAYING, GOOD BYE!')
        break