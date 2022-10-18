

import random
import sys

SIZE = (20, 99)
# size of the labyrinth (x, y)

if sys.getrecursionlimit() < SIZE[0] * SIZE[1]:
	sys.setrecursionlimit(SIZE[0] * SIZE[1])
# if max recursion limit is lower than needed, adjust it

N, S, E, W = 1, 2, 4, 8
# directions translated into bitnums to store information on all cleared walls in one variable per cell

GO_DIR = {N: (0, -1), S: (0, 1), E: (1, 0), W: (-1, 0)}

REVERSE = {E: W, W: E, N: S, S: N}

lab = list(list(0 for i in range(SIZE[0])) for j in range(SIZE[1]))
# labyrinth is prepared

def dig(x, y):
	# digs passage from a cell (x, y) in an unvisited cell
	dirs = [N, E, W, S]
	random.shuffle(dirs)
	# shuffles directions each time for more randomness
	for dir in dirs:
		new_x = x + GO_DIR[dir][0]
		new_y = y + GO_DIR[dir][1]
		if (new_y in range(SIZE[1])) and\
		(new_x in range(SIZE[0])) and\
		(lab[new_y][new_x] == 0):
			# checks if the new cell is not visited
			lab[y][x] |= dir
			lab[new_y][new_x] |= REVERSE[dir]
			# if so, apply info on passages to both cells
			dig(new_x, new_y)
			# repeat recursively
	
def check():
	# displays the cells' values for check-up
	for i in range(SIZE[1]):
		for j in range(SIZE[0]):
			print(" "*(1-(lab[i][j]//10))+\
			str(lab[i][j]), end='|')
		print ('')

def draw():
	# displays the labyrinth
	print ("\nLabyrinth of Hogwarts #" + str(seed) + " (" + str(SIZE[0])+"x"+str(SIZE[1])+")")
	# prints the seed (for reference) and the lab size
	print("_" * (SIZE[0] * 2))
	for j in range(SIZE[1]):
		if j!=0:
			print("|", end='')
		else:
			print ("_", end='')
		for i in range(SIZE[0]):
			if (lab[j][i] & S != 0):
				print(" ", end='')
			else:
				print("_", end='')
			if (lab[j][i] & E != 0):
				if ((lab[j][i] | lab[j][i+1]) & S != 0):
					print(" ", end='')
				else:
					print("_", end='')
			elif (j==SIZE[1]-1) & (i==SIZE[0]-1):
				print("_", end='')
			else:
				print("|", end='')
		print("")
	print("Try 'Labyrinth 2.0' for roguelike xp! ;)")

# Let's start!
seed = random.randint(0, 1000)
random.seed(seed)
dig(SIZE[0]//2, SIZE[1]//2)
draw()
# check()
