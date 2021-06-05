import os

MAX_X = 60
MAX_Y = 20
FRAME_LENGTH = 0.08
STARTING_WORDS = 5
MAX_WORDS = MAX_Y - 2 #Tracks Max number of words that can be on screen
DIFFICULTY = 5
PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()
