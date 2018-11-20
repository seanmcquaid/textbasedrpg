from random import randint

class Goblin(object):
    def __init__(self):
        randomPower = randint(2,5)
        self.name = "Goblin"
        self.health = 8
        self.power = randomPower
    def take_damage(self, amountOfDmg):
        self.health -= amountOfDmg
    def isAlive(self):
        return self.health > 0 