class Map: # always 40x40 i am not going to have size changeable this is too difficult
	def __init__(self, src_file, background="", array=[]):
		self.src = src_file
		self.bg = ""
		self.array = []
		if len(array) == 0:
			self.bg = background
			self.map = [["--" for col in range(40)] for row in range(40)] # empty map in case of errors
			with open(src_file) as f:
				fc = f.read()
				print(fc)
				# if len(fc.split("\n")) > 40:
				# 	print("the map in the file '{}' is not 40x40 (too many rows)".format(src_file))
				# elif len(fc.split("\n")) < 40:
				# 	print("the map in the file '{}' is not 40x40 (too few rows)".format(src_file))
				# else:
				# 	for n, unsplit_row in enumerate(fc.split("\n")):
				# 		row = unsplit_row.rstrip().split(" ")
				# 		if len(row) > 40:
				# 			print("the map in the file '{}' is not 40x40 (row {} is too long)".format(src_file, n))
				# 		elif len(row) < 40:
				# 			print("the map in the file '{}' is not 40x40 (row {} is too short)".format(src_file, n))
				# 		if len(row) != 40:
				# 			return

				for row_idx, row in enumerate(fc.split("\n")):
					for col, tile in enumerate(row.rstrip().split(" ")):
						self.map[row_idx][col] = tile
		else:
			self.map = array

	def draw(self, obj, x, y): # (0, 0) is the top left corner. sorry
		self.map[y][x] = obj
		return True

	def move(self, x1, y1, x2, y2): # src, dest
		if self.mal[y2][x2] != "--":
			return False
		else:
			self.map[y2][x2] = self.map[y1][x1]
			self.map[y1][x1] = "--" # hopefully robots cannot visibly inhabit anything but empty spaces. lmk if this is not the case
		return True

	def tile_at(self, x, y):
		try:
			return self.map[y][x]
		except IndexError:
			return False

	def __repr__(self):
		out = ""
		for row in self.map:
			for tile in row:
				out += "{} ".format(tile)
			out += "\n"
		return out
