#https://en.wikipedia.org/wiki/Blackjack

import os
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,
          'Jack':10,'Queen':10,'King':10,'Ace':1}

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return f'{self.suit} Of {self.rank}:({self.value})'

class Deck():
    
    def __init__(self):
        all_cards = []
        self.all_cards = all_cards
    
        for suit in suits:
            for rank in ranks:
                
                new_card = Card(suit,rank)
                
                self.all_cards.append(new_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)

class Player():
    
    def __init__(self,name,chips):
        self.name = name
        self.chips = chips
        
    def player_bet(self):
        while True:
            try:
                p_bet = int(input('How many chips you wanna bet? '))

            except:
                print('Sorry, that`s not a valid bet.')
            
            else:
                if p_bet > self.chips:
                    print('You have not enough chips.')
                    
                elif p_bet <= 0:
                        print('You need to bet something to continue!')
                        
                else:
                    self.chips -= p_bet
                    return p_bet  
                    
    def add_chips(self,amount):
        self.chips += amount
        
    def hit_stay(self):
        while True: 
            answer = input('Hit another card? Yes/No: ')
            
            if answer in ['Yes','No','yes','no']:
                return answer
            else:
                print('Invalid option!')
                continue
                           
    def __str__(self):
        return f'{self.name} has {self.chips} chips.'

class Table():
    
    def __init__(self):
        dealer_cards = []
        self.dealer_cards = dealer_cards
        
        player_cards = []
        self.player_cards = player_cards
        
    def deal_cards(self):
        self.dealer_cards.append(new_deck.all_cards.pop())
        self.dealer_cards.append(new_deck.all_cards.pop())
        
        print(f'Dealer Cards: {self.dealer_cards[0]} // [HIDDEN CARD]\n')
        
        self.player_cards.append(new_deck.all_cards.pop())
        self.player_cards.append(new_deck.all_cards.pop())
        
        print(f'Your cards: {self.player_cards[0]} // {self.player_cards[1]}')
        
    def show_player_cards(self):
        for card in self.player_cards:
            print(f'PLAYER: {card} //')
            
    def show_dealer_cards(self):
        for card in self.dealer_cards:
            print(f'DEALER CARD: {card} //')
            
    def show_hidden_dealer_cards(self):
        print(f'Dealer Cards: {self.dealer_cards[0]} // [HIDDEN CARD]\n')        
        
    def reset_cards(self):
        self.dealer_cards = []
        self.player_cards = []
    
    def add_card_dealer(self):
        self.dealer_cards.append(new_deck.all_cards.pop()) 
        print(f'DEALER hit a card: {self.dealer_cards[-1]}')        
        
    def add_card_player(self):        
        self.player_cards.append(new_deck.all_cards.pop()) 
        print(f'PLAYER hit a card: {self.player_cards[-1]}')

game_on = True

new_deck = Deck()
new_deck.shuffle()

player_one = Player('Player One',1000)
total_player = 0
total_dealer = 0

new_table = Table()

while game_on:
    print(player_one)
    
    game = True
   
    new_table.deal_cards()
    
    bet_amount = player_one.player_bet()
    
    while True:
        for card in new_table.player_cards:
            total_player += card.value
            
        print(f'\nTotal player points: {total_player}')
            
        if total_player > 21:
            print(f'\nBUST ! you lose {bet_amount} chips.')
           
            new_table.reset_cards()
            game = False
            break
            
        
        hit = player_one.hit_stay()
        

        if hit in ['Yes','yes']:
            os.system('cls')
            new_table.add_card_player()
            
            new_table.show_hidden_dealer_cards()
            new_table.show_player_cards()
            
            total_player=0

        else:
            break
    
    
    if game:        
        for card in new_table.dealer_cards:
            total_dealer += card.value 
        
        os.system('cls')
        new_table.show_player_cards()
        print(f'\nTotal player points: {total_player}')
        
        print('\n')
        print('###############################\n')

        new_table.show_dealer_cards()        

        while total_dealer < 17:
            new_table.add_card_dealer()
            
            total_dealer = 0

            for card in new_table.dealer_cards:
                total_dealer += card.value
                
        print(f'\nTotal dealer points: {total_dealer}')


        if total_player > total_dealer or total_dealer > 21:
            bet_amount = bet_amount*2
            player_one.add_chips(bet_amount)

            print(f'\nPlayer won {bet_amount} chips.')

            total_player = 0
            total_dealer = 0

            new_table.reset_cards()

        elif total_player == total_dealer:
            player_one.add_chips(bet_amount)

            print(f'\nDrawn, player one won {bet_amount} chips.')

            total_player = 0
            total_dealer = 0 

            new_table.reset_cards()
            
        else:
            print(f'\nPlayer lost {bet_amount} chips.') 


    
    if player_one.chips > 0:
        while True:
            gameon = input('\nWanna play another round? Yes/No: ')

            if gameon in ['Yes','yes','no','No']:
                if gameon in ['Yes','yes']:
                    os.system('cls')
                    
                    total_player = 0
                    total_dealer = 0

                    new_table.reset_cards()
                    break
                    
                else:                    
                    print(player_one)
                    game_on = False
                    break

            else:
                print('\nSorry, invalid option!')
        
    else:       
        while True:
            gameon = input('\nYou have 0 chips. Do you wanna restart the game? Yes/No: ')

            if gameon in ['Yes','yes','no','No']:
                if gameon in ['Yes','yes']: 
                    os.system('cls')
                    
                    new_deck = Deck()
                    new_deck.shuffle()

                    player_one = Player('Player One',1000)
                    total_player = 0
                    total_dealer = 0

                    new_table = Table()
                   
                    break
                else:
                    print('\nGame Over!')
                    game_on = False
                    break

            else:
                print('\nSorry, invalid option!')                                        
