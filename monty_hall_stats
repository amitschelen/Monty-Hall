import numpy as np

doors = None

while doors not in range(3, 101):
    doors = int(input('How many doors would you like to try? Enter an integer from 3 to 100.'))
    
print('For', doors, 'doors, the probability of winning without switching is', str(round(1/doors*100,2))+'%.')
print('We\'ll play the game 100,000 times and switch every time to estimate the probability of winning by switching.')
print('\nPrediction:', str(round((doors-1)/(doors*(doors-2))*100, 2))+"%")

correct_count = []

count = 100000
steps = list(range(1,count+1))

#Always switch
for step in steps:
    prize = np.random.randint(1, doors+1)
    guess = np.random.randint(1, doors+1)
    revealed = np.random.choice([i for i in range(1,doors+1) if i not in {guess, prize}])
    guess = np.random.choice([i for i in range(1,doors+1) if i not in {guess, revealed}])
    if guess == prize:
        correct_count.append(1)
    else:
        correct_count.append(0)

avg_correct = sum(correct_count)/len(correct_count)
print('Observed percent correct:', str(round(avg_correct*100, 2))+'%')
print('\nFor', doors, 'doors, the probability of winning by switching appears to be',  str((doors-1))+'/'+str((doors*(doors-2)))+'.')
print('\nFor n doors, the probability of winning by switching appears to be (n-1)/(n(n-2)).')
