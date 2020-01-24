from gallows import *
import hmGameClass as hm


def game_init():
    game = hm.Game()
    return game

def game_replay():
    try:
        again = int(input('Play again? Enter 1:Yes  0:No  '))
        return again
    except:
        print('Looking for a 1 or a 0 here dude')    

def guess_letter(game):
    accept = False
    while not accept:       
        guess = input('Enter a letter guess: ')
        if game.is_available(guess):
            accept = True
        else:
            print('That letter is not available')
    return guess
        
def game_play(game):
    win, lose = False, False
    while not win and not lose:        
        gallows(game.num_misses())
        print('You have {} misses left'.format(game.misses_remaining()))
        print(game.hidden_word())
        guess = guess_letter(game)
        if game.is_in_word(guess):
            game.good_guess(guess)
        else:
            game.bad_guess(guess)
        if game.state == 'win':
            win = True
            gallows(8)
            print('You win, congratulations!!!')
            print('The word was {}.'.format(game.word))
        elif game.state == 'lose':
            lose = True
            gallows(7)
            print('You lost, to bad, better luck next time.')
            print('The word was {}.'.format(game.word))

replay = True
while replay:
    game = game_init()
    game_play(game)
    replay = game_replay()
    
