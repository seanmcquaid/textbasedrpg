from random import randint

class Vampire(object):
    def __init__(self):
        randomPower = randint(4,7)
        self.name = "Vampire"
        self.health = 15
        self.power = randomPower
    def take_damage(self, amountOfDmg):
        self.health -= amountOfDmg
    def isAlive(self):
        return self.health > 0 