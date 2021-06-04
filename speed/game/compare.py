from word.py import Word
from buffer.py import Buffer


class Compare:
    """ Service Provider - Compares what is typed in Buffer with word list from words.py

        Attributes:

    """

    def __init__(self):
        super().__init__()

    def compare(self, words, buffer):
        """ compare_words(Param - words, bufferthing) - Returns index if there is a match otherwise return 9999999

            Args:
              self (Compare): an instance of Compare.
              words (Word): an instance of Word.
              buffer (Buffer): an instance of Buffer.

            Returns - index of matched word
        """
