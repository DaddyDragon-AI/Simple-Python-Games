# Create Deck Object

suits = ('Diamonds','Spades','Hearts','Clubs')

ranks = ('Two','Three','Four','Five','Six','Seven','Eight',
         'Nine','Ten','Jack','Queen','King','Ace')      

values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,
         'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}   

import random

class Card():
    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit))
    
    def shuffle(self):
        return random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()

class Player():
    def __init__(self,name):
        self.name = name
        self.hand = []
    
    def add_card(self,new_cards):
        if isinstance(new_cards,list):
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)
    
    def remove_card(self):
        return self.hand.pop(0)


###########################
#           MAIN          #
###########################

game_on = True

start_deck = Deck()
start_deck.shuffle()
player_one = Player('One')
player_two = Player('Two')

for i in range(26):
    player_one.add_card(start_deck.deal())
    player_two.add_card(start_deck.deal())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f'Round {round_num}')
    
    if len(player_one.hand) == 0:
        print('Player One have no more card to play \n PLayer Two wins the game')
        game_on = False
        break
    if len(player_two.hand) == 0:
        print('Player Two have no more card to play \n PLayer One wins the game')
        game_on = False
        break
    
    at_war = True
    
    player_one_current = []
    player_one_current.append(player_one.remove_card())
    player_two_current = []
    player_two_current.append(player_two.remove_card())

    while at_war:
        if player_one_current[-1].value < player_two_current[-1].value:
            player_two.add_card(player_one_current)
            player_two.add_card(player_two_current)
            at_war = False
        elif player_one_current[-1].value > player_two_current[-1].value:
            player_one.add_card(player_one_current)
            player_one.add_card(player_two_current)
            at_war = False
        else:
            print('WAR!')
            if len(player_one.hand) < 5:
                print('Player One have no more card to play \n PLayer Two wins the game')
                game_on = False
                at_war = False
                break
            elif len(player_two.hand) < 5:
                print('Player One have no more card to play \n PLayer Two wins the game')
                game_on = False
                at_war = False
                break
            else:
                for i in range(5):
                    player_one_current.append(player_one.remove_card())
                    player_two_current.append(player_two.remove_card())
