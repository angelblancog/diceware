import argparse
import random
from pathlib import Path

from diceware.core import roll_dice
from diceware.utils import load_words
from diceware.passwords import add_symbol, calculate_entropy

def main(n_of_words: int, symbol: bool = False):

    path =  Path(Path(__file__).parent, "data", "eff_wordlist.txt")
    words = load_words(path)
    
    numbers = [roll_dice(5) for i in range(n_of_words)]
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
        action=argparse.BooleanOptionalAction,
        help="Add a random symbol to one of the words."
    )
    
    args = parser.parse_args()
    
    n_of_words = args.number_of_words
    response = main(
        n_of_words=n_of_words,
        symbol=args.add_symbol
    )
    
    words = " ".join(response)
    passphrase = words.replace(" ", "")
    bits_of_entropy = calculate_entropy(length=n_of_words)
    
    print(f"""
    {words=}
    {passphrase=}

    {bits_of_entropy=}
    """)
