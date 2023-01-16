from diceware.core import roll_dice
from diceware.utils import load_words

def main():

    N_OF_WORDS = 5

    numbers = [roll_dice(5) for i in range(N_OF_WORDS)]
    words = load_words()
    
    return [words[number] for number in numbers]


if __name__ == "__main__":
     print(main())

