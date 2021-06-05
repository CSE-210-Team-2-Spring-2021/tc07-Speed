import random
from game import constants
from game.point import Point
from game.word import Word

class WordManager:
    """Selects and tracks the words going across the screen.

    Stereotype:
        Information Holder

    Attributes:
        _words          (list) - Holds the set of word objects
        _words_guessed  (list) - Contains all guessed words
        _word_strings   (list) - holds the strings chosen for the word objedcts
        _points         (list) - Holds the value of points each word is worth
    """

    def __init__(self):
        """The class Constructor

        Args:
            self -  An instance of WordManager 
        
        """
        self._word_strings = ['', '', '', '', '']
        self._words = [Word(), Word(), Word(), Word(), Word()]
        self._points = [1, 1, 1, 1, 1]
        self._words_guessed = []

    def reset(self):
        """Sets the field with new words.
        
        Args:
            self -  An instance of WordManager
        """
        self._choose_words()
        self._set_words()

    def _choose_words(self):
        """Selects 5 words and adds them to the _words lists
        
        Args:
            self -  An instance of WordManager 
        """
        all_words = constants.LIBRARY
        value_range = range(len(all_words))
        positions= random.sample(value_range, constants.STARTING_WORDS)

        for i, position in enumerate(positions):
            self._word_strings[i] = all_words[position]
            self._points[i] = 1
    
    def _set_words(self):
        """Update the values of the _words list
        
        Args:
            self -  An instance of WordManager
        """
        num_words = constants.STARTING_WORDS
        x_range = range(constants.MAX_X)
        y_range = range(constants.MAX_Y)
        x = random.sample(x_range, num_words)
        y = random.sample(y_range, num_words)

        for i, word in enumerate(self._words):
            location = Point(x[i], y[i])
            velocity = Point(-1,0) #Probably changing this later
            word.set_word(self._word_strings[i], location, velocity, self._points[i])
        
    def move_words(self):
        """Updates the position of word based on velocity (look at snake.py)

        Args:
            self -  An instance of WordManager
        """
        for word in self._words:
            word.move_next()

    def update_words(self, i):
        """Move the word at given index from _words to _words_guessed update the word
        
        Args:
            self - An instance of WordManager
            i - index of matching word 
        """
        self._words_guessed.append(self._word_strings[i])
        self._words[i].word_typed()

    def get_word_strings(self):
        """Returns _words_string list
        
        Args:
            self - An instance of WordManager
        """
        return self._word_strings
        
    def get_words(self):
        """Returns _words list
        
        Args:
            self - An instance of WordManager

        Returns:
            self._words - list of Word Objects
        """
        return self._words

    def get_points_list(self):
        """Returns point value list(score)
        
        Args:
            self - An instance of WordManager

        Returns:
            self._points - list containing all five current point values
        """

        return self._points

    def get_points(self, i):
        """Returns point value (score)
        
        Args:
            self - An instance of WordManager

        Returns:
            self._points[i] - singular point value chosen by index
        """

        return self._points[i]

    def all_typed(self):
        """The purpose of this method is to return a bool indicating all _words were typed

        Args:
            self - An instance of WordManager

        Returns:
            typed - True if all words are guessed and reset should be called
        """
        for word in self._words:
            if word.get_typed() == False:
                return False
            
        return True