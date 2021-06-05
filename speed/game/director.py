from time import sleep
from typing import Text
from game import constants
from game.word import Word
from game.wordmanager import WordsLocation
from game.score import Score

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
        self._words = Word()
        self._words_location = WordsLocation()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
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
        self._letter = self._input_service.get_letter()
        _text = self.actor.get_text()
        
    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a typed word, checking for all screen 
        words typed, update words locations and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self._check_typed_word()
        self._check_all_typed()
        self._input_service.move_location(self.wordmanager.move_words())
        
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means displaying the letters typed in Buffer, display
        the current words locations and displaying the current score.

        Args:
            self (Director): An instance of Director.
        """
        
        self._output_service.clear_screen()
        self._output_service.draw_words(self._words_location())
        self._output_service.draw_actors(self._snake.get_all())
        self._output_service.draw_actor(self._score)
        # self._output_service.flush_buffer() "Need to think where buffer will be housed"

    def _check_typed_word(self, _letter):
        """checks for typed words and if so, updating the score 1.

        Args:
            self (Director): An instance of Director.
        """
        self.word.word_typed(_letter)
        self.compare.compare_words(_letter)
        if self.score.set_score(self.compare()):
            self._points += 1

    def _check_all_typed(self):
        """Checks to see if all words on screen have been typed. If True,
        then new words need to be selected and set in random positions.

        Args:
            self (Director): An instance of Director.
        """
        if self.wordmanager.all_typed == True:
            self.wordmanager.reset()