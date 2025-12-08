def display_game(game_list):   
    print('Here is the Game list:')
    print(game_list)
    
def user_choice():
        
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice = input('Please select your choice (0,1,2):')
        if choice not in ['0','1','2']:
            print('please choose a valid choice:')
    return int(choice)

def replacement_choice(game_list,position):
    
    user_new_choice = input('Enter your New replacemenrt value:')    
    game_list[position] = user_new_choice
    return game_list


def gameon_choice():
    
    Choice = 'wrong'
    
    while Choice not in ['Y','N','YES','yes','Yes','NO','no','No']:        
        Choice = input('do you want keep playing (Y or N)')
        if Choice not in ['Y','N','YES','yes','Yes','NO','no','No']:
            print('wrong choice select Y or N')
            
    if Choice == 'Y':
        return True
    else:
        return False
    
        
game_list = [1,2,3] 
game_on = True

while game_on:
    
    display_game(game_list)
    
    position =user_choice()
    
    game_list = replacement_choice(game_list,position)
    
    display_game(game_list)
    
    game_on = gameon_choice()
    
           


    
