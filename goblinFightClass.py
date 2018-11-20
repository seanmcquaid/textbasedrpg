import os 
from Hero import Hero
from Goblin import Goblin

hero_name = raw_input("What is your name, brave one?  ")
theHero = Hero(hero_name, 8)
theHero.cheer_hero()
theGoblin = Goblin()

while (theHero.health > 0 and theGoblin.health > 0):

        message = """
        You have %d health and %d power. 
        The goblin has %d health and %d power.
        What do you want to do?
        1. fight goblin
        2. get jiggy with it
        3. flee
        """ 

        print message % (theHero.health, theHero.power, theGoblin.health, theGoblin.power)

        user_input = raw_input("> ")

        if (user_input == "1"):
            theGoblin.health -= theHero.power
            print "You have done %d damage to the goblin!" % theHero.power
        elif (user_input == "2"):
            theHero.health += 5
            print """The goblin stares at you in disbelief of your stupidity!
            His jaw drops as your wounds heal."""
            print "Your health is now %d." % theHero.health
        elif (user_input == "3"):
            print "ALRIGHT %s, SEE YA NERDDDDDDDD" % hero_name.upper()
            break
        else:
            theHero.health -= theGoblin.power
            print "YOU FOOL! You have stumbledith (invalid input)"
            print "The goblin attacked you for %d" % theGoblin.power
            print "Your health is now %d" % theHero.health

        if (theGoblin.health >= 0):
            theHero.health -= theGoblin.power
            print "The goblin attacked you for %d" % theGoblin.power
            if (theGoblin.health <= 4 and theGoblin.health >= 0):
                theGoblin.power += 2
                theHero.health -= theGoblin.power
                print "The Goblin becomes enraged and attacks you for %d" % theGoblin.power
            elif (theHero.health <= 0):
                print "Thou hast been slain!"
        else:
            print "You have killed the Goblin!"


        if (theHero.health < 5):
            theHero.power += 3
            print "You become enraged in your weakened state! Your power is now %d" % theHero.power
        
        print "Hero: %s" %theHero
        print "Goblin: %s" %theGoblin
        raw_input("Press enter to continue")