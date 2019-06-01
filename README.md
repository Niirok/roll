# roll
A tiny python command for dices

How to use it : python roll/roll.py [OPTIONS] [DICE(S) YOU WANT TO ROLL]

Syntax for dice is XdY[(+-)modifier]
available options are :
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -s, --sum             return the sum of all thrown dices
  -S, --separated-values
                        each result is displayed
  -o, --open            reroll open dices (a dice is open when it scores max
                        value)
  -a, --advantage       dices will be rolled twice, picking highest
  -d, --disadvantage    dice will be rolled twice, picking lowest

