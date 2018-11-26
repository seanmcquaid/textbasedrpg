# from random import randint
from Character import Character

# this is a sub clsss of character
class Vampire(Character):
    def __init__(self):
        # import super class with parameters
        super(Vampire, self).__init__("Vampire", 15 , 4)