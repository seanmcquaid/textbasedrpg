class Hero(object):
    def __init__(self, name, power):
        self.name = name
        self.health = 12
        self.power = power
    def cheer_hero(self):
        print "Welcome brave, %s" % self.name
    def take_damage(self, amountofDmg):
        self.health -= amountofDmg
    def isAlive(self):
        return self.health > 0 