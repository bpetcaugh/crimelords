import os

class Map: # always 40x40 i am not going to have size changeable shh
	def __init__(self, src_file):
		self.map = [["--" for col in range(40)] for row in range(40)] # empty map in case of errors
		with open(src_file, "w+") as f:
			fc = f.read()
			for row_idx, row in enumerate(fc.split(os.linesep)): # \n bad need os-specific line ending
				for col, tile in enumerate(row.split(" ")):
					self.map[row_idx][col] = tile
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
		self.map[y1][x1] = "--" # hopefully robots cannot visibly inhabit anything but empty spaces. lmk if this is not the case

	def tile_at(self, x, y):
		return self.map[y][x]

	def __repr__(self):
		out = ""
		for row in self.map:
			for tile in row:
				out += "{} ".format(tile)
			out += "\n"
		return out

# test lines. uncomment and run to view results
# test = Map("./maps/emptymap.txt")
# print(test)
# test.draw("HI", 0, 0)
# print(test)
# test.move(0, 0, 5, 5)
# print(test)