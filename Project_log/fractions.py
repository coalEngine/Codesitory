import re
import operator
from fraction import Fraction

# setting the operation kinds for the calculation
ops = {'+': operator.add,
       '-': operator.sub,
       '/': operator.truediv,
       ':': operator.truediv,
       '*': operator.mul}

# the regex to get the fractions and operator from the input
regex = r"([0-9]*\/[0-9*])(\+|\-|\*|\:|\/)([0-9]*\/[0-9*])"

breuk = False
while breuk is False:                                   # keep looping until we have a valid fraction calculation
    try:
        frac = input("Fraction calculation : ")         # function allows user input.
        frac = frac.replace(" ",'')                     # replace space with nothin
        m = re.match(regex, frac, flags=0)              # search for regex parts
        if m.group(1) and m.group(2) and m.group(3):    # check if parts are existing
            break                                       # when all there, break and continue
    except:                                             # when all goes wrong, keep asking!
        continue

# do the calculation and print on screen
print(ops[m.group(2)](Fraction(m.group(1)), Fraction(m.group(3))))