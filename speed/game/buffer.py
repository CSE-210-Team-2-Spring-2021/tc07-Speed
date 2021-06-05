from game.actor import Actor
from game.point import Point
from game import constants

class Buffer(Actor):
    """The responsibility of the buffer is to keep track of the player's writing.

    Stereotype:
        Information Holder

    Attributes: 
        _word (string): The word that the player is writing .
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (Score): an instance of Score.
        """
        super().__init__()
        self._word = ""
        position = Point(1, constants.MAX_Y)
        self.set_position(position)
        self.set_text(f"Buffer: {self._word}")
    

    def add_letter(self, letter):
        """Adds the given letters to the current word and updates the buffer.
        
        Args:
            self (Buffer): An instance of Buffer.
            letter (string): The letter to add.
        """
        if letter != "*":
            self._word += letter               
        else:
            self._word = ""
        self.set_text(f"Buffer: {self._word}")

    def get_word(self):
        """Gets the Buffer's textual representation.
        
        Args:
            self (Buffer): an instance of Buffer.

        Returns:
            string: The Buffer's textual representation.
        """
        return self._word
