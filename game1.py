from random import shuffle

def shuffle_list(mylist):
    
    shuffle(mylist)
    
    return mylist

def player_choice():
    
    guess= ''
    
    while guess not in ['0','1','2']:
        
        guess = input('Please pick a number 0,1 or 2:')

    return int(guess)

def check_guess(mylist,guess):
    
    if mylist[guess] == 'O':
        
        print('Correct!')
        
    else:
        
        print('Wrong Gueess!')
        
        print(mylist) 
        
        
mylist = [' ','O',' ']

myshuffle_list = shuffle_list(mylist) 

guess = player_choice()

check_guess(myshuffle_list,guess) 

