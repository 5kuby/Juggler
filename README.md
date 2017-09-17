# Juggler
A new word based password generator.

DESCRIPTION:

Juggler generate wordlist from words obtained with social engineering such as name of the victim, name of his parents and other words that can be related with him. Juggler apply to this word some common characters substituions or symbols adds in order to obtain a list of possible passwords.


usage: juggler.py [-h] [-p] [-y] [-s] words filename

positional arguments:
  words            Comma separated words
  filename         Name of the output file

optional arguments:
  -h, --help       show this help message and exit
  
  -p, --password   Do only character substitution
  
  -y, --years      Do character substitution and year append
  
  -s, --separator  Do character substitution, years append and insert a separator between years and words
