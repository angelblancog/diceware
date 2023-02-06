import argparse
import random

from diceware.core import roll_dice
from diceware.utils import load_words
from diceware.passwords import add_symbol

def main(n_of_words: int, symbol: bool = False):

    numbers = [roll_dice(5) for i in range(n_of_words)]
    words = load_words()
    passphrase = [words[number] for number in numbers]

    if symbol:
        word_to_alter = random.choice(passphrase)
        index = passphrase.index(word_to_alter)
        new_word = add_symbol(word_to_alter)
        
        passphrase[index] = new_word
    
    return passphrase


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        prog="diceware",
        description="Generate random passphrases using the diceware method"
    )
    parser.add_argument(
        "-n",
        "--number_of_words",
        type=int,
        default=4,
        help="Number of words to build the passphrase. By default 4."
    )

    parser.add_argument(
        "-a",
        "--add_symbol",
        type=bool,
        default=False,
        help="Add a random symbol to one of the words. By default False."
    )
    
    args = parser.parse_args()
    
    response = main(
        n_of_words=args.number_of_words,
        symbol=args.add_symbol
    )
    
    words = " ".join(response)
    passphrase = words.replace(" ", "")
    
    print(f"{words=}")
    print(f"{passphrase=}")

