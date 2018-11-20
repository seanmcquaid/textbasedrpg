import os 
from Hero import Hero
from Goblin import Goblin
from Vampire import Vampire
from random import randint

hero_name = raw_input("What is your name, brave one?  ")
theHero = Hero(hero_name, 5)
theHero.cheer_hero()

while (theHero.isAlive()):
    randMonster = randint(1,2)
    if randMonster == 1:
        monster = Goblin()
    else: 
        monster = Vampire()

    print "You have encountered the terrifying %s" % monster.name

    while (theHero.isAlive() and monster.isAlive()):

            message = """
            You have %d health and %d power. 
            The %s has %d health and %d power.
            What do you want to do?
            1. fight the %s
            2. get jiggy with it
            3. flee
            """ 

            print message % (theHero.health, theHero.power, monster.name, monster.health, monster.power, monster.name)

            user_input = raw_input("> ")

            if (user_input == "1"):
                monster.take_damage(theHero.power)
                print "You have done %d damage to the goblin!" % theHero.power
            elif (user_input == "2"):
                theHero.health += 5
                print """The goblin stares at you in disbelief of your stupidity! His jaw drops as your wounds heal."""
                print "Your health is now %d." % theHero.health
            elif (user_input == "3"):
                print "ALRIGHT %s, SEE YA NERDDDDDDDD" % hero_name.upper()
                break
            else:
                theHero.health -= monster.power
                print "YOU FOOL! You have stumbledith (invalid input)"
                print "The goblin attacked you for %d" % monster.power
                print "Your health is now %d" % theHero.health

            if (monster.isAlive):
                theHero.take_damage(monster.power)
                print "The goblin attacked you for %d" % monster.power
            elif (not theHero.isAlive()):
                    print "Thou hast been slain!"
            else:
                print "You have killed the %s" %monster.name


            if (theHero.health < 5):
                theHero.power += 3
                print "You become enraged in your weakened state! Your power is now %d" % theHero.power
            
            raw_input("Press enter to continue")
            os.system("clear")

    fightAgainMsg = "Fight another fiend, brave %s? " %theHero.name
    fightAgain = raw_input(fightAgainMsg)
    if fightAgain == "N":
        break