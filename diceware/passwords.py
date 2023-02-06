'''
Password related methods
'''

import random
import string
from math import log2


def calculate_entropy(
    length: int,
    possible_symbols: int = 7776
    ) -> float:
    """Calculate the entropy of a passphrase

    Parameters
    ----------
    * length : int
        number of words of the passphrase

    * possible_symbols : int, optional
        number of possible words, by default 7776. 7776 is the size
        of the EEF Wordlist.
        

    Returns
    -------
    float
        bits of entropy
    """
    
    combinations = possible_symbols**length
    bits_of_entropy = log2(combinations)

    return bits_of_entropy


def add_symbol(word: str, symbols: str = string.punctuation) -> str:
    """
    Randomly introduce a symbol in a string.
    """

    index = random.randint(0, len(word))
    symbol = random.choice(symbols)

    return f"{word[0:index]}{symbol}{word[index:]}"


def generate_password(lenght: int = 12) -> str:
    """
    Return a random string of a given length.
    """

    characters = string.ascii_letters + string.digits + string.punctuation

    return "".join(random.choice(characters) for i in range(lenght))