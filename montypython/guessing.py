#!/user/bin/python3
"""This is a number guessing game between 1 and 100.
Written by: Damian Mercado"""

import random

rand = random.randint(1, 100)

count = 0

while count < 5:
    try:
        userGuess =  int( input('Choose a number between 1 and 100') )
        if userGuess == rand:
            print('You got it! Congratulations')
            break
    #elif userGuess != rand:
        #print('You\'re wrong! Try again')
        #count +=1
        elif guess > rand:
            print('You\'re wrong! Too high.')
            count += 1
        else:
            print('You\'re wrong! Too low.')
            count += 1
    except         
        
