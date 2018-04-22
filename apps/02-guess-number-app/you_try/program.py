import random

print('-' * 32)
print('    Guess a number game')
print('-' * 32)
print()

the_number = random.randint(0, 100)
guess: int = -1

name = input('What is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry {1}, Your guess of {0} is too low'.format(guess, name))
    elif guess > the_number:
        print('Sorry {1}, Your guess of {0} is too high'.format(guess, name))
    else:
        print('Well done {1}! Your guess of {0} is right!'.format(guess, name))

