# Diceware

Implementation of diceware to build passphrases. This method generates random 5
digits number to build passphrases. We can use as many words as desired.

The script will

1. Genereate N random numbers.
2. Use those numbers to look up for words on the EEF wordlist file
3. Return the resulting passphrase

We can also add a symbol in a random possition of the passphrase. This can
be achieved with the `--add-symbol` parameter.


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

To generate a 4-word based passphrase (the default).

Use the `-n` argument to specify other lengths.

```
python3 -m diceware -n 6
```

Use the `-a` or `--add-symbol` flag to add a random symbol.

```
python3 -m diceware -n 6
```


# TODO:
- provide a way to set random seed
- add entropy calculation