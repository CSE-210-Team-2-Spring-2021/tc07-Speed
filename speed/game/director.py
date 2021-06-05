from time import sleep
from typing import Text
from game import constants
from game.wordmanager import WordManager
from game.score import Score
from game.compare import Compare
from game.buffer import Buffer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        words (Words): The words to display to screen.
        words_manager(WordsLocation): The location of each word to display to screen.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """

        self._word_manager = WordManager()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer_text = Buffer()
        self._compare = Compare()
        
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word_manager.reset()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the next letter by user.

        Args:
            self (Director): An instance of Director.
        """
        letter = self._input_service.get_letter()
        print(letter)
        self._buffer_text.add_letter(letter)
                
    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a typed word, checking for all screen 
        words typed, update words locations and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self._check_typed_word()
        self._check_all_typed()
        self._words_location = self._word_manager.move_words()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means displaying the letters typed in Buffer, display
        the current words locations and displaying the current score.

        Args:
            self (Director): An instance of Director.
        """
        
        self._output_service.clear_screen()
        words = self._word_manager.get_words()
        self._output_service.draw_words(words)
        self._output_service.draw_actor(self._score)
        self._output_service.draw_actor(self._buffer_text)
        self._output_service.flush_buffer()

    def _check_typed_word(self):
        """checks for typed words and if so, updating the score 1.

        Args:
            self (Director): An instance of Director.
        """
        word_strings = self._word_manager.get_word_strings()
        buffer = self._buffer_text.get_word()
        index = self._compare.comparison(word_strings, buffer)
        if index < (constants.MAX_WORDS - 1):
            self._word_manager.update_words(index)
            point = self._word_manager.get_points(index)
            self._score.add_points(point)
            self._buffer_text.reset()

    def _check_all_typed(self):
        """Checks to see if all words on screen have been typed. If True,
        then new words need to be selected and set in random positions.

        Args:
            self (Director): An instance of Director.
        """
        if self._word_manager.all_typed == True:
            self._word_manager.reset()