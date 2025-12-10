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
        
        self.aces=0
        
    def add_cards(self,card):
        
        self.cards.append(card)
        
        self.value += values[Card.rank]
        
        if Card.rank == 'Ace':
            
            self.aces = 1
            
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
            
        elif x[0].lower() == 's':
            
            print('Player Stands,Dealer is playing')
            
            playing= False
        else:
            print('Sorry I did not understand')
            
            continue
        

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




                