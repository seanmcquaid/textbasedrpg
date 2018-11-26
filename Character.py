# this is our super (parent) class. All other characters will be subclasses of this class
class Character(object):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def is_alive(self):
        
    def take_damage(self, ammount_of_damage):
        self.health -= ammount_of_damage