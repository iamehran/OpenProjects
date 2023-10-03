
'''
the numbers correspond with caves which th user has to input,demons live in  prime numbere caves
print()
l=9
k=90
while(k>l*2):
'''
from distutils.dep_util import newer_pairwise


print("(1) Easy\n(2) Tough\n")
difflvl=int(input("What difficulty level will you choose?"))
if(difflvl==1):
    print("It's a trap!\nNightmare mode unleashed")
    k=1001
elif(difflvl==2):
    k=51
else:
    k = 21


print("Here are ",k-1," caves ,they  appear sequentially,for caves numbered below 50 the numbers donot appear,press # to dodge in the caves you find Eldrich in prime numbered caves,and * to explore to collect artefacts in the composite numbered caves")
for i in range(1,k): #for caves 1 to k
  if(i<=20): #i is the cave number
    print("Cave",i)
  if(i>20):
    print("Cave",i)
  
  #until j becomes a factor of cave number or greater
  #until value of p exceeds cave number or equals
  j=2 
  while(j<i and i%j!=0):
     #if the number's odd and all prime numbers except 2 is odd
      j=j+1 
  
  p=input('Press\n(#) to dodge\n(*) to explore')
  if(j==i and p=='#' or j!=i and p=="*"):
    print("Your kinetic vision allows you to swiftly evade an incoming unknown disaster.")
  else:
    print("*******************************")
    print("Boss encountered!")
    import random
    if random.random() < 0.3:
      import dark_eldrich
      break
    elif random.random() > 0.7:
      import demon_orc
      break
    else:
      import retricus
      break
    
'''
print(j,i)
  if(p=="*" and i!=j):
      print("You got some elixir")
      print(" You got a wand")
'''
