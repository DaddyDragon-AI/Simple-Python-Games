import random
import os

#CARDS ELEMENTS
suits = ('Hearts ♥','Diamonds ♦','Spades ♠','Clubs ♣')

ranks = ('Two','Three','Four','Five','Six','Seven','Eight',
         'Nine','Ten', 'Jack','Queen','King','Ace')

values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,
          'Seven':7,'Eight':8,'Nine':9,'Ten':10, 'Jack':10,
          'Queen':10,'King':10,'Ace':11}

playing = True

class Card():
    def __init__(self,rank,suit) -> None:
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck():
    def __init__(self) -> None:
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit))
    
    def shuffle(self):
        return random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
    
class Hand():
    def __init__(self) -> None:
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_cards(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_ace(self):
        if self.aces and self.value > 21:
            self.aces -= 1
            self.value -= 10

class Chips():
    def __init__(self,total = 100) -> None:
        self.total = total
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def win_bet_bj(self):
        self.total += self.bet*2
    def lose_bet(self):
        self.total -= self.bet
    def double_bet(self):
        self.bet *= 2

def player_bet(amount):
    while True:
        try:
            amount.bet = int(input('How much do you want to bet?: '))
        except:
            print('🚫 That is not a valid bet! Please try again 🚫')
        else:
            if amount.bet > amount.total:
                print(f'🚫 your bet can not exceed {amount.total}💲')
            else:
                break

def hit(deck,hand):
    hand.add_cards(deck.deal())
    hand.adjust_ace()
    
def double_down(deck,hand,chips):
    chips.double_bet()
    hand.add_cards(deck.deal())
    hand.adjust_ace()

def player_action(deck,hand,chips):
    global playing
    while True:
        action = input('\nWould you like to Hit, Stand or Double down?:')

        if action.lower().startswith('h'):
            hit(deck,hand)
        elif action.lower().startswith('s'):
            playing = False
        elif action.lower().startswith('d'):
            if chips.total-chips.bet >= chips.bet:
                double_down(deck,hand,chips)
                playing = False
            else:
                print("You don't have enough money to Double Down! PLease try again")
                continue
        
        else:
            print('🚫 Sorry, no valid action, please try again. 🚫')
            continue
        break
    
def show_some(player,dealer,player_chips):
    os.system('cls||clear')
    print(f'\n💵 Your balance: {player_chips.total-player_chips.bet:,} 💲')
    print(f'💸 Your Bet: {player_chips.bet:,} 💲')
    print("\n🎲 Dealer's Hand:")
    print('<Card hidden>')
    print(f'{dealer.cards[1]}')
    print(f"\n🃏 Player's Hand: {player.value}")
    print(*player.cards, sep='\n')

def show_all(player,dealer):
    os.system('cls||clear')
    print(f'\n💸 Your Bet: {player_chips.bet:,} 💲')
    print(f"🎲 Dealer's Hand: {dealer.value}")
    print(*dealer.cards, sep='\n')
    print(f"\n🃏 Player's Hand: {player.value}")
    print(*player.cards, sep='\n')

def player_win(player,dealer,chips):
    chips.win_bet()
    print('\n🃏 Player Wins!')

def player_win_bj(player,dealer,chips):
    chips.win_bet_bj()
    print('\n🃏 Player Wins!')

def player_bust(player,dealer,chips):
    chips.lose_bet()
    print('\n🃏 Player Bust')

def dealer_win(player,dealer,chips):
    chips.lose_bet()
    print('\n🎲 Dealer Win')

def dealer_bust(player,dealer,chips):
    chips.win_bet()
    print('\n🎲 Dealer Bust')

def push(player,dealer):
    print('\n⚖ PUSH! ⚖')


#####################
#       MAIN        #
#####################

os.system('cls||clear')
print('\n♠ ♦ ♥ ♣ WELCOME to BlackJack ♠ ♦ ♥ ♣')
print('Get as close to 21 as you can without going over!\nDealer hits until she reaches 17 or more. Aces count as 1 or 11.')
deposit_loop = True
main_loop = True
while main_loop:
    while deposit_loop: 
        try:
            deposit = int(input('\n💵 How much do you want to deposit?: '))
        except:
            print('🚫 That is not a valid amount, your amount must be a number 🚫')
        else:
            if deposit > 1000000:
                print('You are not that rich!')
                continue
            else:
                player_chips = Chips(deposit)
                deposit_loop = False
                game_on = True
                break
    while game_on:
        print(f'\n💵 Your balance: {player_chips.total:,} 💲')

        deck = Deck()
        deck.shuffle()

        player = Hand()
        player.add_cards(deck.deal())
        player.add_cards(deck.deal())

        dealer = Hand()
        dealer.add_cards(deck.deal())
        dealer.add_cards(deck.deal())
        
        player_bet(player_chips)
        show_some(player,dealer,player_chips)

        while playing:
            blackjack = False
            if player.value == 21 and player.aces == 1:
                print('BLACKJACK!')
                player_win_bj(player,dealer,player_chips)
                blackjack = True
                break
            player_action(deck,player,player_chips)
            show_some(player,dealer,player_chips)
            if player.value > 21:
                player_bust(player,dealer,player_chips)
                break
        
        if player.value <= 21 and not blackjack:
            while dealer.value < 17:
                hit(deck,dealer)
            show_all(player,dealer)
            if dealer.value > 21:
                dealer_bust(player,dealer,player_chips)
            elif dealer.value > player.value:
                dealer_win(player,dealer,player_chips)
            elif dealer.value < player.value:
                player_win(player,dealer,player_chips)
            else:
                push(player,dealer)
        
        print(f'Player current balance: {player_chips.total:,} 💲')
        if player_chips.total <= 0:
            print('\nYou have no more chips left to play')
            replay = input('Would you like to deposit more? y or n:')
            if replay.lower().startswith('y'):
                deposit_loop = True
                game_on = False
                break
            else:
                print('\nThanks for Playing')
                print('\n')
                game_on = False
                main_loop = False
                break

        new_game = input('\nWould you like to play another hand? y or n: ')

        if new_game.lower().startswith('y'):
            playing = True
            continue
        else:
            print(f'\nYou have withdrew: {player_chips.total:,} 💲')
            print('Thanks for Playing')
            print('\n'*2)
            game_on = False
            main_loop = False
            break