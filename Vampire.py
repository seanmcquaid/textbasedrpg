from random import randint

class Vampire(object):
    def __init__(self):
        randomPower = randint(3,6)
        self.name = "Vampire"
        self.health = 10
        self.power = randomPower
    def take_damage(self, amountOfDmg):
        self.health -= amountOfDmg
    def isAlive(self):
        return self.health > 0 