# 1) user input =>low and high bound
# 2) random => [a,b]
# 3) loop => condition=> guess_counts => feedback
import random

try:
    low = int( input('Enter lower bound: \n'))
    high = int( input('Enter high bound: \n'))
except:
    print('please enter a valid number1 ')


r = random.randint(low, high)

guess_count = 5

while guess_count>0:

    try:
         new_guess_str = input(f'remained guess: {guess_count} => Enter your next_guess: \n')
         new_guess = int(new_guess_str)

         if r == new_guess:
            print('Great, your guess is correct!')
            break
         elif r > new_guess:
            print('your guess is lower than your selected number')
         else:
            print('your guess is higher than your selected number')  
    
         guess_count -= 1
    
    except:
           print('please enter a valid number')

