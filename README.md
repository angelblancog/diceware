# Diceware

<p float="left">
    <img src="img/password_strength.png" width="50%">
    <img src="img/dices.png" width="40%">
</p>

This is a CLI implementation of diceware to build passphrases.
This method generates random 5-digit numbers to build passphrases.
We can use as many words as desired.

The utility will

1. Genereate N random numbers.
2. Use those numbers to look up for words on the [EEF wordlist](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt) file
3. Return the resulting passphrase


## Installation

You can install this on your favorite virtual environment thing with

```
pip install git+https://github.com/TheGBG/diceware.git
```

or

```
git clone https://github.com/TheGBG/diceware.git && pip install diceware
```

## Usage

You can view how to use this package with `python3 -m diceware -h`, but the use
is fairly simple.

Call

```
python3 -m diceware
```

to generate a 4-word based passphrase (the default).

Use the `-n` argument to specify other lengths.

```
python3 -m diceware -n 6
```

Use the `-a` or `--add-symbol` flag to add a random symbol. This will increase
the password complexity

```
python3 -m diceware -n 6
```

## Requirements

No 3rd party library is required. `python3.9` or greater is required.

## References

- [Diceware - Wikipedia](https://en.wikipedia.org/wiki/Diceware)
- [Dicweare & Passwords - Computerphile](https://www.youtube.com/watch?v=Pe_3cFuSw1E&ab_channel=Computerphile)
- [xkdc - password strength](https://xkcd.com/936/)