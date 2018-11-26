# from random import randint
from Character import Character

# this is a sub clsss of character
class Vampire(object):
    def __init__(self):
        # impoort super class with parameters
        super(Vampire, self).__init__("Vampire", 15 , 4)