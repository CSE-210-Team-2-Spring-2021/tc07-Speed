import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):
    """Subclass of Actor, is a word that moves across the screen

    Stereotype:
        Information Holder

    Attributes:
    _points - int tracking score earned for getting the word right
        
    """

    def __init__(self):
        """The class Constructor

        Args:
            self - An instance of Word
        
        """
        super().__init__()
        self._points = 0
        self._typed = False

    def set_word(self, word, point, velocity, score):
        """Sets all of the actor variables to the values needed
        
        Args:
            self - An instance of Word
            word - String, the word displayed
            point - Point object, words starting position
            velocity - Point object, word's direction
            score - value earned when word is typed
        """
        self.set_text(word)
        self.set_position(point)
        self.set_velocity(velocity)
        self._points = score
        self._typed = False

    def get_points(self):
        """Returns points

        Args:
            self - An instance of Word

        Returns:
            _points - score earned from word
        
        """
        return self._points

    def word_typed(self):
        """Runs when a word is typed, sets text to '-' and _typed to True

        Args:
            self - An instance of Word
        """
        self.set_text('-')
        self._typed = True
    
    def get_typed(self):
        """Returns bool, True if the value was typed
        
        Args:
            self - An instance of word
            
        Returns:
        _typed - Boolean stating if word was typed
        """
        return self._typed