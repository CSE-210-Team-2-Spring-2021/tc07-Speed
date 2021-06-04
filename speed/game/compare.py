class Compare:
    """ Service Provider - Compares what is typed in Buffer with word list from words.py
    """

    def __init__(self):
        super().__init__()

    def comparison(self, words, buffer):
        """ Determines if the input (Buffer) matches the words (Word) on screen

            Args:
              self (Compare): an instance of Compare.

            Returns - index of matched word
        """
        for word in words:
            if word == buffer:
                return word
            else:
                return "9999999"
