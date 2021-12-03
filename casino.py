# GLOBAL VARIABLES: 
stock_game = False
blackjack = False
casino_loop = True
player_action_loop = True
deposit_loop = True

from os import system
from math import floor
from time import sleep
from random import randint
from random import shuffle

# GENERATE NUMBER OF DAY TO PLAY


def day_generator(n):
    yield from range(1, n+1)


#BALANCE & MONEY


class Stock():
    def __init__(self, name) -> None:
        self.owned = 0
        self.price = 0
        self.name = name

    def __str__(self) -> str:
        return self.name

    def penny_stock(self):
        self.price = randint(1, 10)

    def normal_stock(self):
        self.price = randint(5, 100)

    def high_ticket(self):
        self.price = randint(70, 1000)

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
        return shuffle(self.deck)

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

# MODULES


def buy_action(balance, stock):
    max_stock = int(floor(balance.total/stock.price))
    while True:
        try:
            amount = int(input(
                f'\n🎫 How many {stock.name} stocks do you want to buy? (max: {max_stock:,}): '))
        except ValueError:
            print('⛔ Sorry, that is not a valid amount')
        else:
            if amount > max_stock or amount < 0:
                print('⛔ Sorry, that is not a valid amount')
            else:
                break
    # BUY BALANCE ADJUST
    balance.total -= amount * stock.price
    stock.owned += amount
    print(f'You bought {amount} of {stock.name} stocks')
    print(f'💳 Your current Balance: ${balance.total:,}')


def sell_action(balance, stock):
    while True:
        try:
            amount = int(input(
                f'\n🎫 How many {stock.name} stocks do you want to sell? (max: {stock.owned:,}): '))
        except ValueError:
            print('⛔ Sorry, that is not a valid amount')
        else:
            if amount > stock.owned or amount < 0:
                print('⛔ Sorry, that is not a valid amount')
            else:
                break
    # SELL BALANCE ADJUST
    balance.total += amount * stock.price
    stock.owned -= amount
    print(f'You sold {amount} of your {stock.name} stocks')
    print(f'💳 Your current Balance: ${balance.total:,}')


def buy_action_input(day, current_day, balance, stock1, stock2, stock3, stock_selection=None):
    while True:
        try:
            show_ui(day, current_day, balance, stock1, stock2, stock3)
            print('\nWhich stock do you want to buy?')
            stock_selection = int(
                input(f'(1) {stock1} (2) {stock2} or (3) {stock3}: '))
        except ValueError:
            print('⛔ That is not a valid selection!')
        else:
            if stock_selection == 1:
                stock_selection = stock1
            elif stock_selection == 2:
                stock_selection = stock2
            elif stock_selection == 3:
                stock_selection = stock3
            else:
                print('⛔ That is not a valid selection!')
                continue
            show_ui(day, current_day, balance, stock1, stock2, stock3)
            buy_action(balance, stock_selection)
            break


def sell_action_input(day, current_day, balance, stock1, stock2, stock3, stock_selection=None):
    while True:
        try:
            show_ui(day, current_day, balance, stock1, stock2, stock3)
            print('\nWhich stock do you want to sell?')
            stock_selection = int(
                input(f'(1) {stock1} (2) {stock2} or (3) {stock3}: '))
        except ValueError:
            print('⛔ That is not a valid selection!')
        else:
            if stock_selection == 1:
                stock_selection = stock1
            elif stock_selection == 2:
                stock_selection = stock2
            elif stock_selection == 3:
                stock_selection = stock3
            else:
                print('⛔ That is not a valid selection!')
                continue
            show_ui(day, current_day, balance, stock1, stock2, stock3)
            sell_action(balance, stock_selection)
            break

# SHOW UI/UX


def show_ui(day, current_day, balance, stock1, stock2, stock3):
    system('cls||clear')

    # DAY COUNT/ROUND COUNT
    print('📈 SIMPLE STOCK GAMES 📈 - made by: InfrNL 🔥')
    print(f'\n📆 Total Day     : {day}')
    print(f'📅 Current Day   : {current_day}')
    print(f'💳 Balance       : ${balance.total:,}')
    print(
        f'📈 Owned Stock   : {(stock1.owned + stock2.owned + stock3.owned):,}')
    print(f'{stock1.name:^11} | {stock2.name:^13} | {stock3.name:^10}')
    print(f'{stock1.owned:^11,} | {stock2.owned:^14,} | {stock3.owned:^12,}')

    # STOCK PRICE SHOW
    print('\n🎫 Stock Price by Type:')
    print(f'{stock1.name:^11} | {stock2.name:^13} | {stock3.name:^12}')
    print(f'{stock1.price:^11,} | {stock2.price:^14,} | {stock3.price:^16,}')


def day_end(day, current_date, balance, stock1, stock2, stock3):
    show_ui(day, current_date, balance, stock1, stock2, stock3)
    day_end_announce()
    print('                    ▓▓▓▓▒▒▒▒▒▒▒▒\n')
    sleep(0.7)
    show_ui(day, current_date, balance, stock1, stock2, stock3)
    day_end_announce()
    print('                    ▓▓▓▓▓▓▓▓▒▒▒▒\n')
    sleep(0.7)
    show_ui(day, current_date, balance, stock1, stock2, stock3)
    day_end_announce()
    print('                    ▓▓▓▓▓▓▓▓▓▓▓▓\n')
    sleep(0.7)


def day_end_announce():
    print('\n-----------------------------------------------------')
    print('|| The day have ended! Progressing to the next day ||')
    print('-----------------------------------------------------')

# USER ACTIONS


def user_actions(day, current_day, balance, stock1, stock2, stock3):
    global player_action_loop
    while True:
        action = input('\n🏦 Would you like to Buy, Sell or Wait?: ')
        if action.lower().startswith('b'):
            if (
                balance.total < stock1.price
                and balance.total < stock2.price
                and balance.total < stock3.price
            ):
                print("⛔ Sorry, you can not afford any stocks at the moment!")
                continue
            else:
                buy_action_input(day, current_day, balance,
                                 stock1, stock2, stock3)

        elif action.lower().startswith('s'):
            if stock1.owned < 1 and stock2.owned < 1 and stock3.owned < 1:
                print("⛔ Sorry, you do not have any stock to sell!")
                continue
            else:
                sell_action_input(day, current_day, balance,
                                  stock1, stock2, stock3)

        elif action.lower().startswith('w'):
            show_ui(day, current_day, balance, stock1, stock2, stock3)
            player_action_loop = False
            day_end(day, current_day, balance, stock1, stock2, stock3)
            break
        else:
            print('🚫 Sorry, not a valid action, please try again.')
            continue

        more_action = input(
            '\nWould you like to perform anymore action? (y or n): ')

        if more_action.lower().startswith('y'):
            show_ui(day, current_day, balance, stock1, stock2, stock3)
            continue
        else:
            player_action_loop = False
            day_end(day, current_day, balance, stock1, stock2, stock3)
            break

#CARDS ELEMENTS
suits = ('Hearts ♥','Diamonds ♦','Spades ♠','Clubs ♣')

ranks = ('Two','Three','Four','Five','Six','Seven','Eight',
         'Nine','Ten', 'Jack','Queen','King','Ace')

values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,
          'Seven':7,'Eight':8,'Nine':9,'Ten':10, 'Jack':10,
          'Queen':10,'King':10,'Ace':11}

playing = True

def player_bet(amount):
    while True:
        try:
            amount.bet = int(input('How much do you want to bet?: '))
        except:
            print('🚫 That is not a valid bet! Please try again 🚫\n')
        else:
            if amount.bet > amount.total:
                print(f'🚫 your bet can not exceed 💲{amount.total:,}\n')
            elif amount.bet <= 0:
                print(f'🚫 your bet must be at least 💲1\n')
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
    
def show_some(player,dealer,player_balance):
    system('cls||clear')
    print(f'\n💵 Your balance: 💲{player_balance.total-player_balance.bet:,} ')
    print(f'💸 Your Bet: 💲{player_balance.bet:,} ')
    print("\n🎲 Dealer's Hand:")
    print('<Card hidden>')
    print(f'{dealer.cards[1]}')
    print(f"\n🃏 Player's Hand: {player.value}")
    print(*player.cards, sep='\n')

def show_all(player,dealer,player_balance):
    system('cls||clear')
    print(f'\n💸 Your Bet: 💲{player_balance.bet:,} ')
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
    
######################
#        MAIN        #
######################

core = True
while core:
    while casino_loop:
        while deposit_loop:
            system('cls||clear')
            print('     🎰 WELCOME TO THE CASINO 🎰 ')
            try:
                deposit = int(input('\n💵 You seem so not having any chips yet.\n💵 How much do you want to deposit?: '))
            except ValueError:
                print('🚫 That is not a valid amount. Please try again.')
                sleep(1.5)
                continue
            else:
                if deposit > 100000:
                    print('🚫 You are not that rich! Please try again.')
                    sleep(1.5)
                    continue
                elif deposit <= 0:
                    print('🚫 That is not a valid amount! Please try again.')
                    sleep(1.5)
                    continue
                else:
                    player_balance = Chips(deposit)
                    deposit_loop = False
        
        system('cls||clear')        
        print(f'\n 💳 Your current balance: 💲{player_balance.total:,}')        
        print('\n          🎰 GAME LIST 🎰')

        print('\n[1]: BlackJack')
        print('[2]: Stocks Investment')
        game = input('\n🎰 What game do you want to play?: ')

        if not game in ['1','2']:
            print('⛔ Sorry We do not have that game, Please Try again')
            x = input('Do you still want to play casino? (y or n): ')
            if not x == 'y':
                system('cls||clear')
                print('GoodBye, See you again!')
                casino_loop = False
                core = False
                break
            else:
                pass
                
        else:
            if game == '1':
                casino_loop = False
                blackjack = True
                playing = True
                break
            else:
                casino_loop = False
                stock_game = True
                break

    while blackjack:
        system('cls||clear')
        print('\n♠ ♦ ♥ ♣ WELCOME to BlackJack ♠ ♦ ♥ ♣')
        print('Get as close to 21 as you can without going over!\nDealer hits until she reaches 17 or more. Aces count as 1 or 11.')
        main_loop = True
        while main_loop:
            print(f'\n💵 Your balance: 💲{player_balance.total:,}')

            deck = Deck()
            deck.shuffle()

            player = Hand()
            player.add_cards(deck.deal())
            player.add_cards(deck.deal())

            dealer = Hand()
            dealer.add_cards(deck.deal())
            dealer.add_cards(deck.deal())

            player_bet(player_balance)
            show_some(player,dealer,player_balance)

            while playing:
                blackjack = False
                if player.value == 21 and player.aces == 1:
                    print('BLACKJACK!')
                    player_win_bj(player,dealer,player_balance)
                    blackjack = True
                    break
                player_action(deck,player,player_balance)
                show_some(player,dealer,player_balance)
                if player.value > 21:
                    player_bust(player,dealer,player_balance)
                    break

            if player.value <= 21 and not blackjack:
                while dealer.value < 17:
                    hit(deck,dealer)
                show_all(player,dealer,player_balance)
                if dealer.value > 21:
                    dealer_bust(player,dealer,player_balance)
                elif dealer.value > player.value:
                    dealer_win(player,dealer,player_balance)
                elif dealer.value < player.value:
                    player_win(player,dealer,player_balance)
                else:
                    push(player,dealer)

            print(f'Player current balance: 💲{player_balance.total:,}')
            if player_balance.total <= 0:
                print('\nYou have no more chips left to play')
                print('Thanks for Playing')
                main_loop = False
                casino_loop = True
                deposit_loop = True
                print('\nGoing back to the Casino...')
                sleep(2)
                break
            
            new_game = input('\nWould you like to play another hand? y or n: ')

            if new_game.lower().startswith('y'):
                playing = True
                continue
            else:
                print('\nThanks for playing BlackJack')
                main_loop = False
                casino_loop = True
                print('\nGoing back to the Casino...')
                sleep(2)
                break

    while stock_game:

        # GREETINGS
        system('cls||clear')
        print('💸 Hello and welcome to 📈 SIMPLE STOCK GAMES 📈 💸')
        print('   == A game code practice made by: InfrNL 🔥 ==')

        # USER INPUT FOR HOW MANY DAY TO PLAY
        while True:
            try:
                day = int(input('\n    📆 How many day do you want to play?: '))
                if day <= 0:
                    print('⛔ Sorry, that is not a valid amount of days')
                    continue
            except ValueError:
                print('⛔ Sorry that is not a valid number of days. Please try again ⛔.')
            else:
                break

        # GAME RESET
        day_count = day_generator(day)
        penny_stock = Stock('🪙 Penny')
        regular_stock = Stock('💵 Regular')
        high_ticket_stock = Stock('🎫 High Ticket')
        balance_copy = player_balance.total
        playing = True

        # GAMEPLAY:
        while playing:
            current_day = next(day_count)
            end_date = current_day

            # GENERATE STOCK PRICE
            penny_stock.penny_stock()
            regular_stock.normal_stock()
            high_ticket_stock.high_ticket()

            # SHOW UI
            show_ui(day, end_date, player_balance, penny_stock,
                    regular_stock, high_ticket_stock)

            # USER ACTION LOOP
            player_action_loop = True
            while player_action_loop:
                user_actions(day, end_date, player_balance,
                            penny_stock, regular_stock, high_ticket_stock)

            # CHECK END GAME CONDITION
            if end_date == day:
                playing = False
                break

        system('cls||clear')
        print('⏱️ THE GAME HAVE ENDED!')
        penny_stock.penny_stock()
        regular_stock.normal_stock()
        high_ticket_stock.high_ticket()
        print('\n🎫 FINAL STOCK PRICE:')
        print('{0:^10} | {1:^10} | {2:^10}'.format(f'{penny_stock} ($)',
            f'{regular_stock} ($)', f'{high_ticket_stock} ($)'))
        print(f'{penny_stock.price:^11} | {regular_stock.price:^14} | {high_ticket_stock.price:^16}')
        print('\n          📈 ENDGAME STATS 📈')
        b = ' Balance'
        a = 'Assets'
        t = 'Total'
        assets = (penny_stock.price*penny_stock.owned
                + regular_stock.price*regular_stock.owned
                + high_ticket_stock.price*high_ticket_stock.owned)
        total = player_balance.total + assets
        print('=======================================')
        print('|{0:^16} | {1:^16}|'.format(' 💵 Source', '(💲)'))
        print('=======================================')
        print(f'|{b:^17} | {player_balance.total:^17,}|')
        print(f'|{a:^17} | {assets:^17,}|')
        print('=======================================')
        print(f'|{t:^17} | {total:^17,}|')
        print(f'=======================================')
        print(
            f'\n📅 You started with ${balance_copy:,} and end with ${total:,} in {day:,} days')

        new_game = input('\nWould you like to play again? (y or n): ')

        if not new_game.lower().startswith('y'):
            print('\nTHANKS FOR PLAYING\nHave a nice day!')
            print('\nGoing back to the Casino...')
            casino_loop = True
            stock_game = False
            player_balance.total = total
            sleep(2)
            break

        else:
            player_balance.total = total
            playing = True
            continue
    
    continue


