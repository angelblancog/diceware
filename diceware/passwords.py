'''
Password related methods
'''
from typing import Optional

import random
import string
from math import log2


def reseed(hash_: Optional[int] = None) -> None:
    """
    Set the random seed using a random number
    """
    
    if not hash_:
        hash_ = random.randint(-1000000, 1000000) * random.randint(-1000000, 1000000)
    
    random.seed(hash_)


def calculate_entropy(
    length: int,
    possible_symbols: int = 7776
    ) -> float:
    """Calculate the entropy of a passphrase.

    Parameters
    ----------
    * length : int
        password length

    * possible_symbols : int, optional
        number of possible words, by default 7776. 7776 is the size
        of the EEF Wordlist. We assume that the attacker
        knows the dictionary and hence our size of possible symbols is the
        mentioned EEF Wordlist size.
        

    Returns
    -------
    float
        bits of entropy
    """
    
    combinations = possible_symbols**length
    bits_of_entropy = log2(combinations)

    return round(bits_of_entropy, 2)


def add_symbol(word: str, symbols: str = string.punctuation) -> str:
    """
    Randomly introduce a symbol in a string.
    """
    reseed()
    index = random.randint(0, len(word))
    symbol = random.choice(symbols)

    return f"{word[0:index]}{symbol}{word[index:]}"


def generate_password(lenght: int = 12) -> str:
    """
    Return a random string of a given length.
    """
    reseed()
    
    characters = string.ascii_letters + string.digits + string.punctuation

    return "".join(random.choice(characters) for i in range(lenght))