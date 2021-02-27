import numpy as np
import myfunctions as mf

#introduction
print('Welcome to the Monty Hall show! \nWaiting behind one of these doors is a BRAND. NEW. CAR!!!!', 
      '\nUnfurtunately, the other doors only contain goats. And you don\'t want a goat.',
      '\n\nFirst, you\'ll pick a door. Then I\'ll open a door revealing a goat. Then, you\'ll have the opportunity to switch doors if you want.',
      '\n\nTraditionally the game is played with 3 doors, but you can play with up to 100 doors.')

# how many doors to play with?
doors = mf.input_in_range(3, 101, '\nHow many doors do you want to play with? Enter an integer from 3 to 100.')

# set prize door
prize = np.random.randint(1, doors+1)

# user selects initial guess
guess = mf.input_in_range(1, doors+1, '\nFor your initial guess at the car, please select a door from 1 to '+str(doors)+'.')

# host/game reveals a goat behind a door that isn't the guess or the prize
revealed = int(np.random.choice([i for i in range(1,doors+1) if i not in {guess, prize}]))
print('\nI reveal a goat behind door', str(revealed)+'.\n')

# define list of doors that the user can switch to later. Available doors are doors that are unoppened and not the current guess.
valid_doors = list(range(1, doors+1))
available_doors = list(set(valid_doors)-{guess, revealed}) 

# ask the user if they want to switch.
# if they're playing with 3 doors, just switch to the only available door
# if they're playing with more than 3 doors, ask which door they want to swich to. 
switch = None   #switch or not

# ask the user if they want to switch
switch = mf.input_yes_no('\nWould you like to switch doors? Enter yes or no: ')


# if they want to switch and playing with 3 doors, switch to only available door
# if they want to switch and playing with more than 3, ask which door they want to swich to
# otherwise keep guess the same
if switch == 'yes':   
    if doors == 3: 
        new_guess = available_doors[0]
        print('\nOk. Switching to door', str(new_guess)+".")
    else:
        new_guess = None
        while new_guess not in (available_doors): 
            print('\nPlease select a valid new door. Enter an integer from 1 to',  doors, 'that isn\'t door', revealed, 'or', str(guess)+'.')
            new_guess = int(input())
        print('\nOk. Switching to door', str(new_guess)+'.')
else: 
    new_guess = guess
    print('\nOk. Staying with door', str(guess)+'.')

    
# display results. did they win?
if new_guess == prize:  
    print('\nThe prize was behind door', prize, 'and that\'s the one you picked! Nice Job!!')
else:
    print('\nThe prize was behind door', prize, 'but you picked door', str(new_guess) +'.', 'Better luck next time...')
