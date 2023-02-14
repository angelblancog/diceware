import random

from diceware.passwords import reseed

def roll_dice(times: int = 1) -> str:
    
    numbers = [str(random.randint(1, 6)) for i in range(times)]
    return "".join(numbers)
