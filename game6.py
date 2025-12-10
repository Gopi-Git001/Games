suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

import random 
class Card:
    
    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return self.rank + ' of '+ self.suit
    

class Deck:
    
    def __init__(self):
        
        self.cards =[]
        
        for suit in suits :
            for rank in ranks:
                self.cards.append(Card(suit,rank))
                
    def shuffle(self):
        return random.shuffle(self.cards)
    
    def deal_one(self):
        
        return self.cards.pop()
    
    
class Hand:
    
    def __init__(self):
        
        self.cards = []
        self.value = 0 
        self.aces=0
        
    def add_cards(self,card):
        
        self.cards.append(card)
        
        self.value += values[card.rank]
        
        if card.rank == 'Ace':
            
            self.aces += 1
            
    def adjust_for_aces(self):
        
        while self.value >21 and self.aces:
            self.value -= 10
            self.aces -=1
            
            
class Chips:
    
    def __init__(self):
        
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        
        self.total+=self.bet
        
    def lose_bet(self):
        
        self.total -= self.bet
        

def take_bet(chips):
    
    while True:
        
        try:
            
            chips.bet = int(input('Please provide your bet amount:'))
        
        except:
            print('You entered wrong setails please enter Integer value')
            
        else:
            
            if chips.bet > chips.total :
                
                print('sorry your bet exceeds the total amount,chips.total')
                
            else:
                
                break
            
def hit(deck,hand):
    
    hand.add_cards(deck.deal_one())
    
    hand.adjust_for_aces()

def hit_or_stand(deck,hand):
    
    global playing
    
    
    while True:
        
        x = input('would you like to Hit or Stand Enter h or s ')
        
        if x[0].lower() == 'h':
            
            hit(deck,hand)
            break
        
        elif x[0].lower() == 's':
            
            print('Player Stands,Dealer is playing')
            
            playing= False
            break
        else:
            print('Sorry I did not understand')
            
            continue
        
        break

def show_some(player,dealer):
    
    print("\n Dealer's Hand:")
    print(dealer.cards[1])
    
    print("\n player's Hand:")
    
    for card in player.cards:
        print(card)
        
def show_all(player,dealer):
    
    print('Players cards:')
    for card in player.cards:
        print(card)
        
    print('Dealer cards:')

    for card in dealer.cards:
        print(card)



def player_busts(player,dealer,chips):
    print('Player Busts')
    chips.lose_bet()
    
def player_win(player,dealer,chips):
    print('Player wins')
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print('Player win ')
    chips.win_bet()
    
def dealer_win(player,dealer,chips):
    print('dealer win')
    chips.lose_bet()
    
def push(player,dealer):
    print("Tie It's a push")



print('Welcome to Black Jack Game!')

while True:
    
    playing = True
    
    
    new_deck = Deck()
    
    new_deck.shuffle()
    
    
    player_hand = Hand()  
    player_hand.add_cards(new_deck.deal_one())
    player_hand.add_cards(new_deck.deal_one())
    
    dealer_hand = Hand()
    dealer_hand.add_cards(new_deck.deal_one())
    dealer_hand.add_cards(new_deck.deal_one())
    
    chips = Chips()
    
    take_bet(chips)
    
    show_some(player_hand,dealer_hand)
    
    while playing:
        
            hit_or_stand(new_deck,player_hand)
            
            if not playing:
                break
            
            show_some(player_hand,dealer_hand)
            
            if player_hand.value >21:
                
                player_busts(player_hand,dealer_hand,chips)
                
                break
            
    
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(new_deck,dealer_hand)
            
        show_all(player_hand,dealer_hand)
        
        if dealer_hand.value >21 :

                dealer_busts(player_hand,dealer_hand,chips)
                
        elif dealer_hand.value > player_hand.value:
            dealer_win(player_hand,dealer_hand,chips)
        elif dealer_hand.value < player_hand.value:
            player_win(player_hand,dealer_hand,chips)

        else:
            
            push(player_hand,dealer_hand)
    
    print(f"\nPlayer's total chips: {chips.total}")
        
    new_game = input('would you like to play again y or n') 
    
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you!')
        playing= False
        break           
        
    
    

                