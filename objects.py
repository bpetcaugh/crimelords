import math
import random

def distance(p1, p2):
	return math.sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))

class Player():
	def __init__(self, r, color, name):
		self.resources = r
		self.color = color
		self.team_name = name

	def player_turn(self, game_stats):
		#In PROGRESS
		pass

	def get_resources(self):
		return self.resources

	def get_color(self):
		return self.game_color

	def get_name(self):
		return self.team_name

	def mod_resources(self, amount):
		self.resources += amount

class GameObject():
	#Type:Base, Building,
	#Location: (x,y)
	#Team: "R", "B", or None
	def __init__(self, _type, _location, _color, _icon):
		self.id = id(self)
		self.type = _type
		self.location = _location
		self.color = _color
		self.icon = _icon

class Unit(GameObject):
	def __init__(self, _type, _location, _color, _icon, _move_max):
		super(Unit, self).__init__(_type, _location, _color, _icon)
		self.move_max = _move_max

	def move(self, dx, dy, objects):
		if distance([0, 0], [dx, dy]) > self.move_max:
			return

		target_occupied = False
		for obj in objects:
			if obj.location[0] == self.location[0]+dx and obj.location[1] == self.location[1]+dy:
				target_occupied = True
				break
		if target_occupied:
			return

		self.location[0] += dx
		self.location[1] += dy
		for i in range(len(self.location)):
			if self.location[i] > 39:
				self.location[i] = 39
			elif self.location[i] < 0:
				self.location[i] = 0

class Mafioso(Unit):
	def __init__(self, loc, color):
		self.hp = 100
		self.ap = 25
		self.alive = True
		super(Mafioso, self).__init__("Mafioso", loc, color, "M"+color, 5)

	def strike(self, loc, objects):
		#Checks for valid location
		validLoc = False
		if (0 <= loc[0] < 40) and (0 <= loc[1] < 40):
			if (int(loc[0]) == loc[0]) and (int(loc[1]) == loc[1]):
				if (abs(loc[0] - self.location[0]) <= self.attack_max) and (abs(loc[1] - self.location[1]) <= self.attack_max):
					validLoc = True

		#Checks if object can be attacked
		canStrike = False
		if validLoc:
			for o in objects:
				if o.location == loc:
					if o.type in ["Demo", "Mafioso", "Hitman"]:
						o.modify_hp(-self.ap)
						canStrike = True
		return canStrike

class Demo(Unit):
	def __init__(self, loc, color, i):
		self.hp = 750
		self.charge = 1
		self.ap = 0
		self.alive = True
		super(Demo, self).__init__("Demo", loc, color, "D"+color, 3)

class Hitman(Unit):
	def __init__(self, loc, color, i):
		self.hp = 50
		self.move_max = 10
		self.ap = 50
		self.attack_max = 5
		self.alive = True
		super(Hitman, self).__init__("Hitman", loc, color, "H"+color, 10)

	def strike(self, loc, objects):
		#Checks for valid location
		validLoc = False
		if (0 <= loc[0] < 40) and (0 <= loc[1] < 40):
			if (int(loc[0]) == loc[0]) and (int(loc[1]) == loc[1]):
				if (abs(loc[0] - self.location[0]) <= self.attack_max) and (abs(loc[1] - self.location[1]) <= self.attack_max):
					validLoc = True

		#Checks if object can be attacked
		canStrike = False
		if validLoc:
			for o in objects:
				if o.location == loc:
					if o.get_type() in ["Demo", "Mafioso", "Hitman"]:
						o.modify_hp(-self.ap)
						canStrike = True
		return canStrike

class Base(GameObject):
	def __init__(self, loc, color):
		self.hp = 2
		self.ap = 0
		self.mp = 0
		self.move_max = 0
		self.build_max = 1
		self.alive = True
		self.destructable = True
		super(Base, self).__init__("Base", loc, color, "B"+color)

	def build(self, type, loc, objects, player):
		canBuild = True
		for o in objects:
			if o.location == loc:
				canBuild = False

		if type == "Mafioso" and player.get_resources() < 10:
			canBuild = False
		if type == "Demo" and player.get_resources() < 500:
			canBuild = False
		if type == "Hitman" and player.get_resources() < 20:
			canBuild = False

		if canBuild:
			if (0 <= int(loc[0]) < 40) and (0 <= int(loc[1]) < 40):
				if (int(loc[0]) == loc[0]) and (int(loc[1]) == loc[1]):
					if (abs(loc[0] - self.location[0]) <= self.build_max) and (abs(loc[1] - self.location[1]) <= self.build_max):
						if type == "Mafioso":
							objects.append(Mafioso(loc, self.color))
							player.mod_resources(-10)
						elif type == "Demo":
							objects.append(Demo(loc, self.color))
							player.mod_resources(-500)
						elif type == "Hitman":
							objects.append(Hitman(loc, self.color))
							player.mod_resources(-20)

						return objects

	def take_action(self, list, objects, color, player):
		if self.alive:
			if 'build' in list[0]:
				self.build(list[0]['build'][0], color ,list[0]['build'][1] ,objects, player)

class Bank(GameObject):
	def __init__(self, loc, color):
		self.hp = 2
		self.ap = 0
		self.mp = 0
		self.move_max = 0
		self.alive = True
		self.destructable = False
		super(Bank, self).__init__("Bank", loc, color, "BA")

class Neighborhood(GameObject):
	def __init__(self, loc, color):
		self.hp = 2
		self.ap = 0
		self.mp = 0
		self.move_max = 0
		self.alive = True
		self.destructable = True
		super(Neighborhood, self).__init__("Neighborhood", loc, color, "NE")
