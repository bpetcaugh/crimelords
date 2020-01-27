import os

class Map: # always 40x40 i am not going to have size changeable shh
	def __init__(self, src_file):
		self.map = [["--" for col in range(40)] for row in range(40)] # empty map in case of errors
		with open(src_file, "w+") as f:
			fc = f.read()
			for row, _ in enumerate(fc.split(os.linesep)): # \n bad need os-specific line ending
				for col, tile in enumerate(row.split(" ")):
					self.map[row][col] = tile
		if len(self.map) > 40:
			print("the map in the file '{}' is not 40x40 (too many rows)".format(src_file))
		elif len(self.map) < 40:
			print("the map in the file '{}' is not 40x40 (too few rows)".format(src_file))
		for n, row in enumerate(self.map):
			if len(row) > 40:
				print("the map written in the file '{}' is not 40x40 (row {} is too long)".format(src_file, n))
			elif len(row) < 40:
				print("the map written in the file '{}' is not 40x40 (row {} is too short)".format(src_file, n))

	def draw(self, obj, x, y): # (0, 0) is the top left corner. sorry
		self.map[y][x] = obj

	def move(self, x1, y1, x2, y2): # src, dest
		self.map[y2][x2] = self.map[y1][x1]
		self.map[y1][x1] = "--" # hopefully robots cannot inhabit anything but empty spaces. lmk if this is not the case