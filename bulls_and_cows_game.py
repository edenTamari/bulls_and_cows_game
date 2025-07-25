"""
@Project: Bulls and cows game

@Description : We would like to implement the Cows and Bulls game using
    a positive four-digit integer. We will implement the game using two
    bots that will simulate the game's moves until one of the bots wins.

@Author: Eden Tamari
"""
import random

player = 1

"""
The function parses a number and checks that all its digits are different from each other.
@Returns:
    int: returns a complex positive number of four digits in the range 1000-9999
"""
def generate_number():
    while(True):
        fail = 0
        random_num = random.randint(1000, 9999)
        random_num_list = list(str(random_num))
        for digit in random_num_list:
            if random_num_list.count(digit) != 1:
                fail = 1
                break
        if fail == 0:
            return random_num

'''
The function parses which player will start.
@Returns:
    int: returns the value of the starting player 1 or 2
'''
def which_player_start():
    return random.randint(1, 2)

'''
The function checks if digit exist in number
@param:
    num (int):  The first parameter
    digit (int):  The second parameter
@:returns:
    boolean: True if the digit is in the number. Otherwise it returns False.
'''
def is_digit_exist(num, digit):
    if str(digit) in str(num):
        return True
    return False
'''
The function checks how many digits in a guess number are in the same place as the secret number
@param:
    guess_num (int):  The first parameter
    secret_num (int):  The second parameter
@:returns:
    int: the number of digits in the guess number that are in their place in the drawn number (bulls)
'''
def num_of_bulls(guess_num, secret_num):
    bulls = 0
    for digit_guess,digit_secret in zip(str(guess_num), str(secret_num)):
        if digit_guess == digit_secret:
            bulls += 1
    return bulls

'''
The function checks how many digits in a guess number are in the secret number in a different position
@param:
    guess_num (int):  The first parameter
    secret_num (int):  The second parameter
@:returns:
    int: the number of digits in the guess number that match the drawn number but are not in the correct place (cow)
'''
def num_of_cows(guess_num, secret_num):
    cow = 0
    for digit in str(guess_num):
        if is_digit_exist(secret_num, digit):
            index_of_digit_in_guess = str(guess_num).find(digit)
            index_of_digit_in_secret = str(secret_num).find(digit)
            if (index_of_digit_in_guess != index_of_digit_in_secret
                    and str(secret_num)[index_of_digit_in_secret] != str(guess_num)[index_of_digit_in_secret]
                    and str(secret_num)[index_of_digit_in_guess] != str(guess_num)[index_of_digit_in_guess]):
                cow += 1
    return cow

'''
The function decides which player is playing.
@param:
    turn (int):  The first parameter
@:returns:
    int: the identity of the current player, 1 or 2
'''
def current_player(turn):
    return 2//player

'''
The function implements the game logic
'''
def start_game():
    global player
    win = 0
    secre_num = generate_number()
    print('Secret number = ', secre_num)
    turn = 1
    player = which_player_start()
    #print('player number', player, 'is starting')
    while(win == 0):
        guess_num = generate_number()
        bulls = num_of_bulls(guess_num, secre_num)
        cows = num_of_cows(guess_num, secre_num)
        #print('Player:', player)
        print('Guessed number =', guess_num, 'Bulls =', bulls, 'Cows =', cows)
        if bulls == 4:
            win = 1
            print('Player',player,'wins!')
        player = current_player(turn)
        turn += 1

start_game()


