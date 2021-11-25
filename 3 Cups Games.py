# IMPORT RANDOM
import random

# PLAYER'S GUESS FUNC
def player_guess():
    
    guess = ''
    
    while guess not in ['<','^','>']:
        
        # Recall input() returns a string
        guess = input("Pick a cup left, middle or right using: < , ^ , > : ")
    return guess

# CONVERT PLAYER'S GUESS TO INT
def player_guess_int():

   if guess == '<':
      convert_guess = 0
   elif guess =='^':
      convert_guess = 1
   elif guess == '>':
      convert_guess = 2
   return convert_guess


###################################
#              MAIN               #
###################################

# INITIAL LIST
list =[" "," "," "]

# PLAYER'S GUESS
guess = player_guess()
convert_guess = player_guess_int()

# ANSWER RANDOMIZE SYSTEM
num = random.randint(0,2)

# CHECK PLAYER'S GUESS >< ANSWER
if num == convert_guess:
  print('Correct Guess!')
  list[num] = "0"
  print(list)
else:
    print('Wrong! Better luck next time')
    list[num] = "0"
    print(list)