import numpy as np

def input_in_range(lower, upper, prompt):
    var = None
    while var not in range(lower, upper+1):
        try:
            var = int(input(prompt))
            if var < lower or var > upper:
                raise ValueError
        except:
            print('Please enter a number from '+str(lower)+' to '+str(upper)+'.')
    return var

#introduction
print('Welcome to the Monty Hall show! \nWaiting behind one of these doors is a BRAND. NEW. CAR!!!!', 
      '\nUnfurtunately, the other doors only contain goats. And you don\'t want a goat.',
      '\n\nFirst, you\'ll pick a door. Then I\'ll open a door revealing a goat. Then, you\'ll have the opportunity to switch doors if you want.',
      '\n\nTraditionally the game is played with 3 doors, but you can play with up to 100 doors.')

doors = input_in_range(3, 100, '\nHow many doors do you want to play with? Enter an integer from 3 to 100.')  #how many doors to play with

prize = np.random.randint(1, doors+1)   #set prize door

guess = input_in_range(1, doors, '\nFor your initial guess at the car, please select a door from 1 to '+str(doors)+'.')  #select initial guess

revealed = int(np.random.choice([i for i in range(1,doors+1) if i not in {guess, prize}])) #reveal goat
print('\nI reveal a goat behind door', str(revealed)+'.\n')

valid_doors = list(range(1, doors+1))
available_doors = list(set(valid_doors)-{guess, revealed})  #list of unoppened doors

switch = None   #switch or not
while switch not in ("yes", "no"):   
    switch = input("\nWould you like to switch doors? Enter yes or no: ") 
    if switch == "yes":   
        if doors == 3:   # no need to ask which door to switch to if there are only 3 doors
            new_guess = available_doors[0]
            print('\nOk. Switching to door', str(new_guess)+".")
        else:
            new_guess = None
            while new_guess not in (available_doors): 
                print("\nPlease select a valid new door. Enter an integer from 1 to",  doors, 'that isn\'t door', revealed, 'or', str(guess)+".")
                new_guess = int(input())
            print('\nOk. Switching to door', str(new_guess)+".")
    elif switch == "no": 
        new_guess = guess
        print("\nOk. Staying with door", str(guess)+".")
    else: 
        print("Please enter yes or no.")
        
if new_guess == prize:   # results
    print('\nThe prize was behind door', prize, 'and that\'s the one you picked! Nice Job!!')
else:
    print('\nThe prize was behind door', prize, 'but you picked door', str(new_guess) +'.', 'Better luck next time...')
