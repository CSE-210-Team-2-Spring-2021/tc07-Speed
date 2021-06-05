class Compare:
    """ Service Provider - Compares what is typed in Buffer with word list from words.py
    """

    def comparison(self, words, buffer):
        """ Determines if the input (Buffer) matches the words (Word) on screen

            Args:
              self (Compare): an instance of Compare.

            Returns - index of matched word
        """
        for i, word in enumerate(words):

            if word == buffer:
                return i
            else:
                return 9999999
