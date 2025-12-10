from random import randint
from IPython.display import clear_output


# the_board = [' ']*10

# board = the_board

def display_board(board):
    
    
    
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    
#print(display_board(board))



def player_input():
    
    marker = ''
    
    while marker not in ['X','O']:
        marker = input('Please choose your marker (X or O):').upper()
    if marker == "X":
        return ('X','O')
    else:
        return ('O','X')

    
# player_1_marker,player_2_marker = player_input()

# print(player_2_marker)


# print(player_input())


def place_marker(board,marker,position):
    
    board[position]  = marker

#check all possibilities
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  
            (board[4] == mark and board[5] == mark and board[6] == mark) or  
            (board[1] == mark and board[2] == mark and board[3] == mark) or  
            (board[7] == mark and board[4] == mark and board[1] == mark) or  
            (board[8] == mark and board[5] == mark and board[2] == mark) or  
            (board[9] == mark and board[6] == mark and board[3] == mark) or  
            (board[7] == mark and board[5] == mark and board[3] == mark) or  
            (board[9] == mark and board[5] == mark and board[1] == mark))    

def choose_first():
    
    flip = randint(0,1)
    
    if flip == 0:
        
        return 'player_1'
    else:
        return 'player_2'
    
def space_check(board,position):
    
    return board[position] ==' '

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    
    choice = 0
    
    while choice not in range(1,10) or not space_check(board,choice):
        
        choice = int(input('Please choose your position:'))
        
    return choice


def replay():
    
    choice = input('Keep wanna play again y or no:')

    if choice == 'y':
        return True
    else:
        return False
            
            
print('welcome to Game world!')

while True:
    
    the_board = [' ']*10

    board = the_board
    
    
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    
    print(turn+'will go first')
    
    play_game = input('Are you ready to play game (yes or no)')
    
    if play_game=='yes':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        
        if turn == 'player_1':        
            display_board(board)
            
            position = player_choice(board)
            
            place_marker(board,player1_marker,position)
            
            if win_check(board,player1_marker):
                
                display_board(board)
                print('congratulations!')
                game_on = False
                
            else:
                
                if full_board_check(board):
                    display_board(board)
                    print('Tie')
                    game_on = False
                else:
                    turn = 'player_2'
                
        else:
            
            display_board(board)
            
            position = player_choice(board)
            
            place_marker(board,player2_marker,position)
            
            if win_check(board,player2_marker):
                
                display_board(board)
                print('congratulations!')
                game_on = False
                
            else:
                
                if full_board_check(board):
                    display_board(board)
                    print('Tie')
                    game_on = False
                else:
                    turn = 'player_1'
    
    if not replay():
        break
            
    