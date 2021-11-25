import os
import random
from math import floor

#GLOBAL PLAYER ACTION LOOP
player_action = True

#GENERATE NUMBER OF DAY TO PLAY
def day_generator(n):
    for i in range(1,n+1):
        yield i

#BALANCE & MONEY
class Cash():
    def __init__(self,amount) -> None:
        self.balance = amount

class Stock():
    def __init__(self) -> None:
        self.owned = 0
        self.price = 0
    
    def stock_price(self):
        self.price = random.randint(1,1000)
        
#USER ACTIONS
def user_actions(balance,stock):
    global player_action
    while True:
        action = input('\n🏦 Would you like to Buy, Sell or Wait?: ')
        if action.lower().startswith('b'):
            if balance.balance/stock.price >= 1:
                while True:
                    try:
                        amount = int(input(f'🎫 How many stocks do you want to buy? (max: {int(floor(balance.balance/stock.price)):,}): '))
                    except ValueError:
                        print('⛔ That is not a number')
                    else:
                        balance.balance -= amount * stock.price
                        stock.owned += amount
                        player_action = False
                        break
            else:
                print("⛔ Sorry, you do not have enough money to buy any stock at the current price!")
                continue
        elif action.lower().startswith('s'):
            if stock.owned >= 1:
                while True:
                    try:
                        amount = int(input(f'🎫 How many stocks do you want to sell? (max: {stock.owned:,}): '))
                    except ValueError:
                        print('⛔ That is not a number')
                    else:    
                        stock.owned -= amount
                        balance.balance += amount * stock.price
                        player_action = False
                        break
            else:
                print("⛔ Sorry, you do not have any stock to sell!")
                continue
        elif action.lower().startswith('w'):
            player_action = False
        else:
            print('🚫 Sorry, no valid action, please try again. 🚫')
            continue
        break

##################
#      MAIN      #
##################

while True:
    
    #GREETINGS
    os.system('cls||clear')
    print('💹💸 Hello and welcome to Stock Game 💹💸')

    #USER INPUT FOR HOW MANY DAY TO PLAY
    while True:
        try:
            day = int(input('\n📆 How many day do you want to play?: '))
        except ValueError:
            print('⛔ Sorry that is not a valid number of days. Please try again ⛔.')
        else:
            break

    #GAME RESET
    day_count = day_generator(day)
    player_balance = Cash(1000)
    stock = Stock()
    playing = True

    #GAMEPLAY:
    while playing:
        player_action = True
        current_day = next(day_count)
        #CLEAR CONSOLE FOR VIEWS
        os.system('cls||clear')
        
        #DAY COUNT/ROUND COUNT
        print('📆 Total Day     :',day)
        print('📅 Current Day   :',current_day)
        print(f'💳 Balance       : ${player_balance.balance:,}')
        print(f'📈 Owned Stock   : {stock.owned:,}')
        
        #STOCK PRICE GENERATE AND SHOW
        stock.stock_price()
        print(f'\n🎫 Stock Price    : ${stock.price:,}')
        
        #USER ACTION LOOP
        while player_action:
            user_actions(player_balance,stock)
        
        #CHECK END GAME CONDITION
        end_date = current_day
        if end_date == day:
            playing = False
            break
        continue
    
    os.system('cls||clear')
    print('\n⏱️ THE GAME HAVE ENDED!')
    print(f'\n📈 You started with $1,000 and ended with ${player_balance.balance:,} in {day} days 📅.')
    
    new_game = input('\nWould you like to play again?: ')

    if new_game.lower().startswith('y'):
        playing = True
        continue
    else:
        print('\nTHANKS FOR PLAYING\nHave a nice day!')
        break