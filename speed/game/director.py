from time import sleep
from game import constants
from game.word import Words
from game.words_manager import WordsLocation
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
        self._words = Words()
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
        _letter = self._input_service.get_letter()
        
    def _do_updates(self, _letter):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a typed word and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self.compare.compare_words(_letter)
        self._handle_body_collision()
        self._handle_food_collision()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._food)
        self._output_service.draw_actors(self._snake.get_all())
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

    def _handle_body_collision(self):
        """Handles collisions between the snake's head and body. Stops the game 
        if there is one.

        Args:
            self (Director): An instance of Director.
        """
        head = self._snake.get_head()
        body = self._snake.get_body()
        for segment in body:
            if head.get_position().equals(segment.get_position()):
                self._keep_playing = False
                break

    def _handle_food_collision(self):
        """Handles collisions between the snake's head and the food. Grows the 
        snake, updates the score and moves the food if there is one.

        Args:
            self (Director): An instance of Director.
        """
        head = self._snake.get_head()
        if head.get_position().equals(self._food.get_position()):
            points = self._food.get_points()
            for n in range(points):
                self._snake.grow_tail()
            self._score.add_points(points)
            self._food.reset() 