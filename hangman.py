import random

# 1) list of names 
# 2) select one name randomly
# 3) get user char
# 4) check => show feedback
# 5) guess > 0 =>win/loss

names = ['hassan','Ali', 'Behnam','Mohammad','Vahid', 'Amin','Maryam', 'Zahra']


selected_name = random.choice(names).lower()

guess_count = len(selected_name)
guessed_list = ['-'] * len(selected_name)
current_guess = " ".join(guessed_list)
print(current_guess)

while guess_count > 0:
    guessed_char = input('Enter a char: \n')

    if guessed_char.isalpha() and len(guessed_char) == 1:
        if guessed_char in selected_name:
            if guessed_char in guessed_list:
                print('You have guessed before, try a new character')
            else:
                for idx, char in enumerate(selected_name):
                    if char == guessed_char:
                        guessed_list[idx] = guessed_char

                current_guess = " ".join(guessed_list)
                print(f'Perfect => {current_guess}')

                if "-" not in guessed_list:
                    print('You won!')
                    break
        else:
            guess_count -= 1  
            print(f'Wrong! => Remaining guesses: {guess_count}')
    
    else:
        print('Please enter a valid character')

if "-" in guessed_list:
    print(f'You lost! The word was: {selected_name}')