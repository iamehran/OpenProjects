'''
The Second Questboss
The Demon orc
The variables ending with 'ED' are the stats of Eldrich
the ones that don't are player stats
Run by importing it on main.py  
'''

#Import stuff
import random
from wep_index import swordskillset
from wep_index import shieldskillset
from wep_index import spellbskillset

#Boss stats
healthED = 400
BattleED = 1
#Playerstats
attk = 100
dfns = 100
coins = 500
health = 1000
c = 1

#strings
commencement1 = "YOU VS. DEMON ORC"
intro1 = "The orclord moves his hands in a circular motion\na colossal clock descends from the heavens and crashes onto the ground!\n Time has stopped and you feel a tremendous pain in your body as you watch the still orc staring straight towards you while not moving a muscle."
#Supermove text
supermove1 = "Demon Orc uses [SPECIAL] Dimensional Distortion!"
#name of supermove
bossname1 = "Demon Orc"
smallermove1 = "Demon Orc uses Lightning feet!"
victorymsg1 = "A sudden exhaustion hits the enemy. Grabbing the chance, from nowhere, a surprising blow of lightning leaves nothing but ashes of the Orc infront of you."

eldmsg1 = "The Orc seems stunned, you get an extra turn!" #When you get your turn

for j in range(1,5):
    for i in range(1,85):
        if(i%2==0 and j%2!=0):
           print("MYTHX",end="")
        else:
            print(" ",end="")
        if(j%2==0 and i%2!=0):
            print("MYTHX",end="")
        else:
            print(" ",end="")
    print()
print(commencement1)
import random
while c > 0:
  if health <= 0:
    print("G A M E    O V E R")
    break
  if random.random() < 0.5:
      print("=*=*=*=*=*=*=*=*")
      if random.random() < 0.1:
          print(intro1)
          print(supermove1)
          health -= 1000
          print("Player HP: ", health)
          print(bossname1 +" HP: ", healthED)
          print("G A M E    O V E R")
          break
      elif random.random() < 1:
          print(smallermove1)
          health -= 100
          print("Player HP: ", health)
          print(bossname1 + " HP: ", healthED)
  else:
      print("=*=*=*=*=*=*=*=*")
      if healthED <= 0:
        print(victorymsg1)
        print("Y O U    W O N")
        break
      print(eldmsg1)
      print("(1)Dodge")
      print("(2)Retreat")
      print("(3)Equipment skill")
      mve = int(input())
      if mve == 3:
              print("Equipment used")
              wepset = 4
              if wepset == 1:
                swordskillset(healthED)
              elif wepset == 2:
                shieldskillset(healthED)
              elif wepset == 4:
                spellbskillset(healthED)
      elif mve == 2:
          print("GAME OVER")
          print("A spell was cast such as to make your fear the very poison for your demise")
          break
      elif mve == 1:
          print("You dodged the attack")
          if random.random() < 0.4:
            print(bossname1 + " used Mindread!")
            health -= 10
  print("Player HP: ", health)
  print(bossname1 + " HP: ", healthED)
      
      

        
      
