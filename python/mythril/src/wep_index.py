def swordskillset(heel):
    print("(1)Blade dance")
    print("(2)Side slash")
    print("(3)[SPECIAL] Executioner's rage")
    #========================================
    mvex = int(input())
    if mvex == 1:
        heel -= 30
    elif mvex == 2:
        heel -= 40
    elif mvex == 3:
        heel -= 60

def shieldskillset():
    print("(1)Charge and slam")
    print("(2)Shield throw")
    print("(3)[SPECIAL] Eternal Realms Divider ")
    #========================================
    mvex = int(input())
    if mvex == 1:
        heel -= 20
    elif mvex == 2:
        heel -= 30
    elif mvex == 3:
        heel -= 100
      

def spellbskillset(heel):
    print("(1)Fire Arrow")
    print("(2)Lightning Orb")
    print("(3)[SPECIAL] Night Of The Black Star")
    #========================================
    mvex = int(input())
    if mvex == 1:
        heel -= 40
    elif mvex == 2:
        heel -= 60
    elif mvex == 3:
        heel -= 150
       