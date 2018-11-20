class Hero(object):
    def __init__(self, name, power = 3):
        self.name = name
        self.health = 12
        self.power = power
    def cheer_hero(self):
        print "Welcome brave, %s" % self.name
