'''
The first Questboss
The dark spirit of Eldrich
The variables ending with 'ED' are the stats of Eldrich
the ones that don't are player stats
Run by importing it on main.py  
'''

#protagostat function will store the stats of the player
DamageED = 0
healthED = 100
BattleED = 1
#Playerstats
Equip = 1
Damage = 0
attk = 100
dfns = 100
coins = 500
health = 1000
c = 1
eldmsg = "Eldrich has paralysis! Take your chance NOW!"

for j in range(1,5):
    for i in range(1,85):
        if(i%2==0 and j%2!=0):
           print("~",end="")
        else:
            print(" ",end="")
        if(j%2==0 and i%2!=0):
            print("~",end="")
        else:
            print(" ",end="")
    print()
print("QUEST BOSS FIGHT \n\n YOU VS THE DARK SPIRIT OF ELDRICH NIGHTINGALE")
import random
while c > 0:
  if random.random() < 0.5:
      # ELDRICH
      print("=*=*=*=*=*=*=*=*")
      if random.random() < 0.1:
          print(
              "Eldrich activates his special move!\n[SPECIAL] Night Of The Black Star"
          )
          print(
              "\nComplete darkness envelopes you, the next second you let your guard down,and the whole world goes white. You see a massive star, black and burning with a black flame descend onto the Earth\n you try to run but it's of no use."
          )
          health -= 1000
          print("Player HP: ", health)
          print("Eldrich HP: ", healthED)
          print("G A M E    O V E R")
          break
      elif random.random() < 1:
          print("Eldrich casts Curse Bind!")
          health -= 100
          print("Player HP: ", health)
          print("Eldrich HP: ", healthED)
  else:
      print("=*=*=*=*=*=*=*=*")
      if healthED <= 0:
        print("The spirit of the brave envelops you in a tornado of white flame. \n The next second, you disappear from sight,and with your next appearance, you slash through Eldrich's slender neck, spilling his blood on your weapon. The world goes silent and the angels in heaven sing a beautiful chorus as his soul slowly floats up into the eternity.")
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
          if Equip == 1:
              print("(1)Blade dance")
              print("(2)Side slash")
              print("(3)[SPECIAL] Executioner's rage")
              mvex = int(input())
              if mvex == 1:
                  healthED -= 30
              elif mvex == 2:
                  healthED -= 40
              elif mvex == 3:
                  healthED -= 60
      elif mve == 2:
          print("GAME OVER")
          print("A spell was cast such as to make your fear the very poison for your demise")
          break
      elif mve == 1:
          print("You dodged the attack")
          if random.random() < 0.4:
            print("Eldrich used Mindread!")
            health -= 10
            print("Player HP: ", health)
            print("Eldrich HP: ", healthED)

        
      
