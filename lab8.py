# Partner lab 8 example

import random
damagebymonster = random.randint(1,35)

print "A monster approaches! Prepare to fight!"

playerhealth = 100
monsterhealth = 100
punchDmg = 5
swordDmg = 10
fireballDmg = 30
titanfall = 100
titanpunchdmg = 15
a40mm = 25
rocketsalvodmg = 40
print 'You have 100 health'
print 'The monster has 100 health'
rand = random.randint(0,10)
while(playerhealth>0 and monsterhealth>0):
    if rand == 3:

       print 'TITANFALLL!!'
       playerhealth = playerhealth+titanfall
       print 'What attack do you wish to do?'
       print 'Titan punch=1 ' + '40mm=2 ' + 'Rocket Salvo=3'
       userinput = int(raw_input())
       if userinput == 1:
            monsterhealth = monsterhealth-titanpunchdmg
            print 'Hit the monster with your metal fisr you have'
            print 'The monster has ' + str(monsterhealth) + ' health.'
       elif userinput == 2: 
            monsterhealth = monsterhealth-a40mm
            print 'Hit the monster with a 40mm round you have'
            print 'The monster has ' + str(monsterhealth) + ' health.'
       elif userinput == 3: 
            monsterhealth = monsterhealth-rocketsalvodmg
            print 'Shot rockets every where you have'
            print 'The monster has ' + str(monsterhealth) + ' health.'
       playerhealth = playerhealth - damagebymonster
       print 'Ox the monster did ' + str(damagebymonster) + ' damage.'
       print 'Your health is ' + str(playerhealth)
       damagebymonster = random.randint(1,35)
       if playerhealth<=0:
            print 'Dead you are.' + ' Failure to the order you are.'
       elif monsterhealth<=0:
            print 'Killed Ox you have.' + ' Great job you have done.' + ' Sloppy it was, again you must fight.'
    else:
        rand = random.randint(0,7)
        print 'Which attack do you wish to do?'
        print '1-punch 2-Sword 3-fireball'
        userinput = int(raw_input())
        if userinput == 1:
            monsterhealth = monsterhealth-punchDmg
            print 'Gone ninja you have, hit monster with your fist you have.'
            print 'The monster has ' + str(monsterhealth) + ' health.'
        elif userinput == 2: 
            monsterhealth = monsterhealth-swordDmg
            print 'Swing your sword at the monster you have.' 
            print 'The monster has ' + str(monsterhealth) + ' health.'
        elif userinput == 3: 
            monsterhealth = monsterhealth-fireballDmg
            print 'Conjured up a fireball you have.'
            print 'The monster has ' + str(monsterhealth) + ' health.'
        playerhealth = playerhealth - damagebymonster
        print 'Ox the monster did ' + str(damagebymonster) + ' damage.'
        print 'Your health is ' + str(playerhealth)
        damagebymonster = random.randint(1,35)
        if playerhealth<=0:
            print 'Dead you are.' + ' Failure to the order you are.'
        elif monsterhealth<=0:
            print 'Killed Ox you have.' + ' Great job you have done.' + ' Sloppy it was, again you must fight.'
        
        
# TODO:
# Loop - When should it stop?
# Input - user gets to choose attack
# Calculating the damage done by the user and the monster
# Output - printing damage
# Printing a victory message