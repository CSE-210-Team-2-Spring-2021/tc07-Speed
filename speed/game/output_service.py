import sys
from game import constants
from asciimatics.widgets import Frame


class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (OutputService): An instance of OutputService.
            screen (Screen): An Asciimatics Screen.
        """
        self._screen = screen
        
    def clear_screen(self):
        """Clears the Asciimatics buffer in preparation for the next rendering.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * constants.MAX_X, 0, 0, 7)
        self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, 7)
        
    def draw_actor(self, actor):
        """Renders the given actor on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actor (actor): The actor to render.
        """ 
        
        text = actor.get_text()
        position = actor.get_position()
        x = position.get_x()                         
        y = position.get_y()
        wordLenght = len(text)
        if wordLenght >=constants.MAX_X:                                     # Not sure if this conditional should be here
                x = constants.MAX_X-wordLenght                               
        self._screen.print_at(text, x, y, 7)  

    def draw_words(self, words):
        """Renders the given list of words on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            words (list): The words to render.
        """ 
        for word in words:
            self.draw_actor(word)
    
    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self._screen.refresh()    
