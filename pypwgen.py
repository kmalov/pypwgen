import os
import random
import argparse

numbers = range(10)
vowels = ["a", "e", "i", "o", "u", "y"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
special = ["!", "@", "#", "$", "%", "&", "*"]

def dice():
    return random.choice([False, True])

def gen_alpha(first_capitalize=False):
    result = list()
    vowels_first = dice() 
    for i in range(4):
        if i % 2 == 0:
            c = random.choice(vowels) if vowels_first else random.choice(consonants)
        else:
            c = random.choice(vowels) if not vowels_first else random.choice(consonants)
        result.append(c)
    if first_capitalize:
        result[0] = result[0].upper()        
    return result

def gen_number(special_char=False):
    result = list()
    for i in range(4):
        if special_char:
            if i < 3:
                if dice():
                    c = random.choice(special)
                    special_char = False   
                else:
                    c = random.choice(numbers)
            else:
                c = random.choice(special)
        else: 
            c = random.choice(numbers)
        result.append("%s" % c)
    return result

def parse_args():
    parser = argparse.ArgumentParser(description='MS Style password generator')
    parser.add_argument("-s", "--simple", dest="simple", default=True, help="Make simple 8 chars password", action='store_true')
    parser.add_argument("-S", "--strong", dest="strong", default=False, help="Make strong 16 chars password", action='store_true')
    parser.add_argument("-c", "--special", dest="special", default=False, help="Add some special char to password", action='store_true')
    return parser.parse_args()

def init():
    random.seed(os.urandom(64))


if __name__ == "__main__":
    args = parse_args()
    init()

    result = list()
    result.extend(gen_alpha(True))
    result.extend(gen_number(args.special))
    if args.strong:
        result.extend(gen_alpha())
        result.extend(gen_number(args.special))
    print "".join(result)       
