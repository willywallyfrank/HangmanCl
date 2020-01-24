#this module defines the hangman game class
import random

WORD_LIST = 'wordListLong.txt'
MAX_MISSES = 7

class Game:
    def __init__(self):
        self.available_letters = [chr(n) for n in range(97, 123)]
        self.correct_letters = []
        self.used_letters = []
        self.misses = 0
        self.num_misses_remaining = MAX_MISSES
        self.state = 'play'
        self.get_word()

    def get_word(self):
        with open('wordListLong.txt','r') as file:       
            file_contents = file.readlines()
            num_words = len(file_contents)
            index = random.randint(0,num_words-1)
            self.word = file_contents[index].strip()
                
    def is_in_word(self,letter):
        if letter in self.word:
            return True
        else:
            return False
        
    def good_guess(self,letter):
#        print('\n'*20)
        print('Yes {} is in the word'.format(letter))
        self.available_letters.remove(letter)
        self.correct_letters.append(letter)
        self.used_letters.append(letter)
        if self.hidden_word() == self.word:
            self.state = 'win'
        
    def bad_guess(self,letter):
#        print('\n'*20)
        print('No {} is not in the word'.format(letter))
        self.available_letters.remove(letter)
        self.used_letters.append(letter)
        self.misses += 1
        self.num_misses_remaining -= 1        
        if self.num_misses_remaining == 0:
            self.state = 'lose'            
        
    def num_misses(self):
        return self.misses
    
    def misses_remaining(self):
        return self.num_misses_remaining
    
    def is_available(self,letter):
        if letter in self.available_letters:
            return True
        else:
            return False
    
    def hidden_word(self):
        hidden = ''
        for letter in self.word:
            if letter in self.correct_letters:
                hidden += letter
            else:
                hidden += '*'
        self.hidden = hidden
        return hidden
            
        
            
        
