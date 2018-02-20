import logging
from random import randint
logging.basicConfig(filename="err.log", level=logging.DEBUG)
import math

class Random:
    """This is the class for the number generator
    with assigned probabilities"""

    def __init__(self, assign=None):
        self.assign = assign

    """gen handles the objects"""
    def gen(self):
        if self.assign == None:
            self.message = "You didn't enter in any dict as a param!"
            self._log()
        elif (type(self.assign) != dict):
            self.message = "That's not the right data type! :("
            self._log()
        else:
            self._a = self.assign
            self._random()

    """play is a playback of past values in an iterator"""
    def play(self):
        with open('past.txt', 'r') as f:
            lines = f.readlines()
            return lines

    """_random is the internal engine for making suitable 
    card decks given the input probabilties and delivering
    the pick"""
    def _random(self):
        self.big_boy = []
        for key, value in self._a.items():
            self.big_boy += [key] * math.ceil((value*len(self._a.items())))
        length = len(self.big_boy)
        self.choice = self.big_boy[randint(0,length-1)]
        self._log(True)
        return print(self.choice)

    """_log is the internal logging engine for both the past.txt file and
    the err.log file"""
    def _log(self, play=False):
        if play:
            with open('past.txt', 'a+') as f:
                f.write(str(self.choice) + "\n")
            exit
        else:
            print("Error: " + self.message +
                "\n[ + ] logged in `.../NumProb/err.log`!")
            logging.debug(f"{self} : " + self.message)
            exit
