'''
The third Questboss
Eldrich Daaptaash nightingale
The variables ending with 'ED' are the stats of Eldrich
the ones that don't are player stats
Run by importing it on main.py  
'''


#Import stuff
import random
from wep_index import swordskillset
from wep_index import shieldskillset
from wep_index import spellbskillset

DamageED = 0
healthED = 100
BattleED = 1
#Playerstats

Damage = 0
attk = 100
dfns = 100
coins = 500
health = 1000
c = 1

#dialogues
commencement = " 'Someone seems to have called Retricus,who will for the rest of the odessey ushering you to the Heraclitus '"
actcomencement="The maroon mantle of Eldrich causes a stir in the air,that you are almost blinded by the dust,none of you can see each other"
actcommand="Sieze the oppurtunity.."
intro = """This is the doomed planet.The star Sirius would make the day and night happen but until a day came when a powerful demon came and dethroned the god called Heraclitus.The planet was swallowed up by complete darkness,So,the aide of Heraclitus will come to you by order,to get you the right way to Heraclitus"""
supermove = "The kick has more power than Mjölnir"
bossname = "Eldrich Daptaash Nightangle"
smallermove = "You punched on his cheek and ,see Eldrich lose a molar "
victorymsg = "You dampened the dark spirits,You have lighted the the hopes of the dawn"

eldmsg = "" #When you get your turn
def gameover(dead, playdead):
    if dead == 0:
        print("GAME OVER")
    elif playdead == 0:
        print("YOU WON!")
for j in range(1,5):
    for i in range(1,85):
        if(i%2==0 and j%2!=0):
           print("*",end="")
        else:
            print(" ",end="")
        if(j%2==0 and i%2!=0):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print(intro)
print(commencement)
import random
while c > 0:
  if random.random() < 0.5:
      # ELDRICH
      print("========")
      if random.random() < 0.1:
          print(intro)
          print(supermove)
          health -= 1000
          print("Player HP: ", health)
          print(bossname +" HP: ", healthED)
          print("G A M E    O V E R")
          break
      elif random.random() < 1:
          print(smallermove)
          health -= 100
          print("Player HP: ", health)
          print(bossname + " HP: ", healthED)
  else:
      print("========")
      if healthED <= 0:
        print(victorymsg)
        print("Y O U    W O N")
        break
      print(eldmsg)
      #PLAYER
      print("(1)Dodge")
      print("(2)Retreat")
      print("(3)Equipment skill")
      mve = int(input())
      if mve == 3:
          print("Equipment used")
          Equip = 4
          if Equip == 1:
            swordskillset(healthED)
          elif Equip == 2:
            shieldskillset(healthED)
          elif Equip == 4:
            spellbskillset(healthED)
      elif mve == 2:
          print("GAME OVER")
          print("A spell was cast such as to make you fear the very poison for your demise")
          break
      elif mve == 1:
          print("You dodged the attack")
          if random.random() < 0.4:
            print("Eldrich used Mindread!")
            health -= 10
            print("Player HP: ", health)
            print("Eldrich HP: ", healthED)