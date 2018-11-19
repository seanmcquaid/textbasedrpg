import os

hero_name = raw_input("What is thy name, brave adventurer?  ")

def fight():
    print "Welcome %s. Thou art brave! " %hero_name
    hero = {
        "Health" : 12,
        "Power" : 3
    }
    goblin = {
        "Health" : 8,
        "Power" : 3
    }
    print "Fight the Goblin!"
 
    while (hero["Health"] > 0 and goblin["Health"] > 0):
        message = """
        You have %d health and %d power. 
        The goblin has %d health and %d power.
        What do you want to do?
        1. fight goblin
        2. get jiggy with it
        3. flee
        """ 

        print message % (hero["Health"], hero["Power"], goblin["Health"], goblin["Power"])

        user_input = raw_input("> ")

        if (user_input == "1"):
            goblin["Health"] -= hero["Power"]
            print "You have done %d damage to the goblin!" % hero["Power"]
        elif (user_input == "2"):
            hero["Health"] += 5
            print """The goblin stares at you in disbelief of your stupidity!
            His jaw drops as your wounds heal."""
            print "Your health is now %d." % hero["Health"]
        elif (user_input == "3"):
            print "ALRIGHT %s, SEE YA NERDDDDDDDD" % hero_name.upper()
            break
        else:
            hero["Health"] -= goblin["Power"]
            print "YOU FOOL! You have stumbledith (invalid input)"
            print "The goblin attacked you for %d" % goblin["Power"]
            print "Your health is now %d" % hero["Health"]

        if (goblin["Health"] >= 0):
            hero["Health"] -= goblin["Power"]
            print "The goblin attacked you for %d" % goblin["Power"]
            if (goblin["Health"] <= 4 and goblin["Health"] >= 0):
                goblin["Power"] += 2
                hero["Health"] -= goblin["Power"]
                print "The Goblin becomes enraged and attacks you for %d" % goblin["Power"]
            elif (hero["Health"] <= 0):
                print "Thou hast been slain!"
        else:
            print "You have killed the Goblin!"


        if (hero["Health"] < 5):
            hero["Power"] += 3
            print "You become enraged in your weakened state! Your power is now %d" % hero["Power"]
        
        print "Hero: " + str(hero)
        print "Goblin: " + str(goblin)
        raw_input("Press enter to continue")
        os.system("clear")

fight()