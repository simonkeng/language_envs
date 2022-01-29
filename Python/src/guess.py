import random
from re import I, U

def rand():
    return random.randint(0, 100)

def get_user_input():
    guess = input('User guess: ')
    try:
        guess = int(guess)
    except ValueError:
        raise ValueError('Must provide integer.')
    return guess

def game():
    print('Starting guessing game. Guess a number between 0 and 100')
    number = rand()

    while True:
        guess = get_user_input()

        if guess == number:
            print('You win!')
            print('The machine lost to you....')
            print('...congratulations human :]')
            break

        if guess + 1 == number or guess + 2 == number or guess + 3 == number:
            print('Your super close! Just a little too high.')
            continue
        if guess - 1 == number or guess - 2 == number or guess - 3 == number:
            print('Super close! But too low.')
            continue
        if guess + 10 == number or guess + 8 == number or guess + 6 == number:
            print('Your very close, but too high.')
            continue
        if guess - 10 == number or guess - 8 == number or guess - 6 == number:
            print('Very close, but too low.')
            continue
        if guess > number:
            print('Nope! Your guess is too high.')
            continue
        if guess < number:
            print('No, sorry. Your guess is too low.')
            continue

if __name__ == "__main__":
    game()