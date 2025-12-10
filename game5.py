import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
        
    def __str__(self):
        
        return self.rank + ' of '+self.suit


class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            
            for rank in ranks :
                
                self.all_cards.append(Card(suit,rank))
                
    def __str__(self):
        
        pass
    
    def shuffle(self):
        
        return random.shuffle(self.all_cards)

    def deal_one(self):
        
        return self.all_cards.pop(0)
    


class Player():
    
    def __init__(self,name):
        
        self.name = name 
        self.all_cards = []
        
    def add_cards(self,new_cards):
        
        if type(new_cards) == type([]):
            
            random.shuffle(new_cards)
            
            self.all_cards.extend(new_cards)
        else:
            
            self.all_cards.append(new_cards)
    
    def remove_one(self):
        
        return self.all_cards.pop()
    

print("="*60)
print("🎴 WELCOME TO THE GAME OF WAR! 🎴")
print("="*60)

player_one = Player('One')

player_two = Player('two')


new_deck = Deck()

new_deck.shuffle()

print("\n📋 Dealing cards to both players...")

for i in range(26):
    
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

print(f"✅ Each player has been dealt 26 cards!")
print(f"\n🎮 Let the game begin!\n")
print("="*60)
    
Round_Number = 0

game_on = True

while game_on:
    
    Round_Number +=1
    
    print(f"\n🔄 ROUND {Round_Number}")
    print("-"*60)
    
    if len(player_one.all_cards) ==0:
        
            print('\n❌ Player One has run out of cards!')
            print('🏆 PLAYER TWO WINS THE GAME! 🏆') 
            game_on = False
            break
            
    if len(player_two.all_cards)== 0:
        
        print('\n❌ Player Two has run out of cards!')
        print('🏆 PLAYER ONE WINS THE GAME! 🏆') 
        game_on = False
        break
    
    player_one_cards = []
    
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    
    player_two_cards.append(player_two.remove_one())
    
    print(f"Player One plays: {player_one_cards[0]} (Value: {player_one_cards[0].value})")
    print(f"Player Two plays: {player_two_cards[0]} (Value: {player_two_cards[0].value})")
    
    at_war = True
    
    while at_war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            print(f"✨ Player One wins this round! (+{len(player_one_cards) + len(player_two_cards)} cards)")
            print(f"📊 Card Count - Player One: {len(player_one.all_cards)} | Player Two: {len(player_two.all_cards)}")
            
            at_war = False
            
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            print(f"✨ Player Two wins this round! (+{len(player_one_cards) + len(player_two_cards)} cards)")
            print(f"📊 Card Count - Player One: {len(player_one.all_cards)} | Player Two: {len(player_two.all_cards)}")
            
            at_war = False
            
        else:
            
            print("\n⚔️  WAR! Both players have equal cards! ⚔️")
            
            if len(player_one.all_cards) < 5:
                
                print('\n💥 Player One doesn\'t have enough cards for war!')
                print('🏆 PLAYER TWO WINS THE GAME! 🏆')
                
                game_on = False
                break
            elif len(player_two.all_cards) <5:
                
                print('\n💥 Player Two doesn\'t have enough cards for war!')
                print('🏆 PLAYER ONE WINS THE GAME! 🏆')
                
                game_on = False
                break
            
            else:
                
                print("🃏 Each player puts down 5 cards face down...")
                
                for i in  range(5):
                    
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                
                print(f"🎯 Player One's war card: {player_one_cards[-1]} (Value: {player_one_cards[-1].value})")
                print(f"🎯 Player Two's war card: {player_two_cards[-1]} (Value: {player_two_cards[-1].value})")

print("\n" + "="*60)
print(f"🎮 GAME OVER after {Round_Number} rounds!")
print("="*60)
