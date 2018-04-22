import random

print('-' * 32)
print('    Guess a number game')
print('-' * 32)
print()

the_number = random.randint(0, 100)
guess: int = -1


while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Your guess is too low')
    elif guess > the_number:
        print('Your guess is too high')
    else:
        print('Well done! You guessed correctly')

print('Done!')
