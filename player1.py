import crimelords
import random

def turn(unit, objects):
	dirs = random.choice([(0, 1), (1, 0), (-1, 0), (0, -1)])
	unit.move(dirs[0], dirs[1])
