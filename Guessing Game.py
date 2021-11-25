
  # Interaction Intro

print('LADY AND GENTLEMEN, WELCOME TO GUESS THE NUMBER!')
print('The rule is simple, I will think of a number from 1 to 100 and you have to guess what it is!')
print("If your guess is within 10 of my number, I will say: 'It is WARM!'" )
print("If your guess is further than 10 away from my number, I will say: 'It is COLD!'")
print("If your guess is closer to the number than your previous guess, I will say:'It is WARMER!'")
print("If your guess is farther from the number than your previous guess, I will say:'It is COLDER!'")
print("I wish you the best of luck and see how many guesses it will take for you to found my number!!!!")
print("At anytime, If the game is too hard for you, to stop the game, all you have to do is just to summon the devil, muhahahaha!")
print("LET'S GO!!!!!")

  # Random Answer Mechanism

import random

num = random.randint(1,100)

 # Number of Guesses storage list

Guesses = [0]

while True:

     # Inputting system
    Guess = int(input("I am thinking of a number between 1 to 100.\n Do you know what number it is?:"))
    
     #Stop Game Mechanism
    if Guess == 666:
        print('You have summonned the Devil to Stop the Game!')
        break
        
     # Out of range answer
    if Guess < 1 or Guess > 100:
        print("Your Guess is OUT OF BOUND, please input a different answer")
        continue

     # Correct Answer
    if Guess == num:
        print(f"CONGRATULATION!!! IT ONLY TOOK YOU {len(Guesses)} TRIES TO FIND MY NUMBER!" )
        break
    
     # wrong answer add to counting list mechanism
    Guesses.append(Guess)

     # Lose function:
    if len(Guesses) == 100:
        print(f'It is already been {len(Guesses)} tries and you have not found my number?? Shame on you!')
        print(f'The answer is: {num}, you IDIOT!')
        print('THANKS FOR PLAYING ANYWAY!')
        print('GOODBYE! DUMBASS!')
        break

     #WARMER AND COLDER Mechanism
    if Guesses[-2]:
        if abs(num-Guess) < abs(num-Guesses[-2]):
            print(f'{Guesses[-1]} is WARMER!')
        
        else:
            print(f'{Guesses[-1]} is COLDER!')
    
    else:
        if abs(num-Guess) <= 10:
            print(f'{Guesses[-1]} is WARM!')
        
        else:
            print(f'{Guesses[-1]} is COLD!')


