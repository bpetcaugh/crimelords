import math
import pygame
import random
'''To Do:
-Engineer Explosion Function
-Create function that gives influence/money
-Create capture function/action
'''

def distance(p1, p2):
	return math.sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))

class Background(pygame.sprite.Sprite):
	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location

# game objects below

class Player():
	def __init__(self, i, m, color, name):
		self.influence = i
		self.money = m
		self.color = color
		self.team_name = name

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
		self.hp=100
		self.ap=25
		self.alive=True
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
				if o.get_location() == loc:
					if o.get_type() in ["Demo", "Mafioso", "Hitman"]:
						o.modify_hp(-self.ap)
						canStrike = True
		return canStrike

	def take_action(self, list, objects, color, player):
		if self.alive:
			if 'move' in list[0]:
				self.move(list[0]['move'], objects)
			elif 'strike' in list[0]:
				self.strike(list[0]['strike'], objects)

# class Demo(Unit):
# 	def __init__(self, loc, color):
# 		self.hp=750
# 		self.charge=1
# 		self.ap=0
# 		self.alive=True
# 		super(Demo, self).__init__("Demo", loc, color, "D"+color, 3)
#
# 	def move(self, loc, objects):
# 	#Checks if various conditions are met
# 	#Returns True if the move was successful, otherwise returns False
# 		canMove = True
# 		for o in objects:
# 			if o.get_location() == loc:
# 				canMove = False
#
# 		if canMove:
# 			if (0 <= loc[0] < 40) and (0 <= loc[1] < 40):
# 				if (int(loc[0]) == loc[0]) and (int(loc[1]) == loc[1]):
# 					if (abs(loc[0] - self.location[0]) <= self.move_max) and (abs(loc[1] - self.location[1]) <= self.move_max):
# 						self.location = loc
# 						return True
# 		return False
#
# 	def take_action(self, list, objects, color, player):
# 		if self.alive:
# 			if 'move' in list[0]:
# 				self.move(list[0]['move'], objects)
# 			elif 'strike' in list[0]:
# 				self.strike(list[0]['strike'], objects)
#
# class Hitman(Unit):
# 	def __init__(self, loc, color):
# 		self.hp=50
# 		self.ap=50
# 		self.attack_max=5
# 		self.alive=True
# 		super(Hitman, self).__init__("Hitman", loc, color, "H"+color, 10)
#
# 	def strike(self, loc, objects):
# 		#Checks for valid location
# 		validLoc = False
# 		if (0 <= loc[0] < 40) and (0 <= loc[1] < 40):
# 			if (int(loc[0]) == loc[0]) and (int(loc[1]) == loc[1]):
# 				if (abs(loc[0] - self.location[0]) <= self.attack_max) and (abs(loc[1] - self.location[1]) <= self.attack_max):
# 					validLoc = True
#
# 		#Checks if object can be attacked
# 		canStrike = False
# 		if validLoc:
# 			for o in objects:
# 				if o.get_location() == loc:
# 					if o.get_type() in ["Demo", "Mafioso", "Hitman"]:
# 						o.modify_hp(-self.ap)
# 						canStrike = True
# 		return canStrike
#
# 	def take_action(self, list, objects, color, player):
# 		if self.alive:
# 			if 'move' in list[0]:
# 				self.move(list[0]['move'], objects)
# 			elif 'strike' in list[0]:
# 				self.strike(list[0]['strike'], objects)
#
#
# class Base(Unit):
# 	def __init__(self, loc, color):
# 		self.hp = 2
# 		self.ap = 0
# 		self.mp = 0
# 		self.build_max = 1
# 		self.alive = True
# 		self.destructable = True
# 		super(Base, self).__init__("Base", loc, color, "R"+color, 0)
#
# 	def build(self, type, color, loc, objects, player):
# 		canBuild = True
# 		for o in objects:
# 			if o.get_location() == loc:
# 				canBuild = False
#
# 		if type == "Mafioso" and player.money < 10:
# 			canBuild = False
# 		if type == "Demo" and player.money < 500:
# 			canBuild = False
# 		if type == "Hitman" and player.money < 20:
# 			canBuild = False
#
# 		if canBuild:
# 			if (0 <= int(loc[0]) < 40) and (0 <= int(loc[1]) < 40):
# 				if (int(loc[0]) == loc[0]) and (int(loc[1]) == loc[1]):
# 					if (abs(loc[0] - self.location[0]) <= self.build_max) and (abs(loc[1] - self.location[1]) <= self.build_max):
# 						if type == "Mafioso" and color == "B":
# 							objects.append(Mafioso("Mafioso",loc,color,"BM"))
# 							player.mod_resources(-10)
# 						elif type == "Mafioso" and color == "R":
# 							objects.append(Mafioso("Mafioso",loc,color,"RM"))
# 							player.mod_resources(-10)
# 						elif type == "Demo" and color == "B":
# 							objects.append(Demo("Demo",loc,color,"BD"))
# 							player.mod_resources(-500)
# 						elif type == "Demo" and color == "R":
# 							objects.append(Demo("Demo",loc,color,"RD"))
# 							player.mod_resources(-500)
# 						elif type == "Hitman" and color == "B":
# 							objects.append(Hitman("Hitman",loc,color,"BH"))
# 							player.mod_resources(-20)
# 						elif type == "Hitman" and color == "R":
# 							objects.append(Hitman("Hitman",loc,color,"RH"))
# 							player.mod_resources(-20)
#
# 						return objects
#
# 	def take_action(self, list, objects, color, player):
# 		if self.alive:
# 			if 'build' in list[0]:
# 				self.build(list[0]['build'][0], color ,list[0]['build'][1] ,objects, player)
#
# class Bank(Unit):
# 	def __init__(self, loc, color):
# 		self.hp = 2
# 		self.ap = 0
# 		self.mp = 0
# 		self.alive = True
# 		self.destructable = False
# 		super(Bank, self).__init__("Bank", loc, color, "B"+color, 0)
#
# class Neighborhood(Unit):
# 	def __init__(self, loc, color):
# 		self.hp = 2
# 		self.ap = 0
# 		self.mp = 0
# 		self.alive = True
# 		self.destructable = True
# 		super(Neighborhood, self).__init__("Neighborhood", loc, color, "N"+color, 0)
#
# 	def strike(self, loc, objects):
# 		#Checks for valid location
# 		validLoc = False
# 		if (0 <= loc[0] < 40) and (0 <= loc[1] < 40):
# 			if (int(loc[0]) == loc[0]) and (int(loc[1]) == loc[1]):
# 				if (abs(loc[0] - self.location[0]) <= self.attack_max) and (abs(loc[1] - self.location[1]) <= self.attack_max):
# 					validLoc = True
#
# 		#Checks if object can be attacked
# 		canStrike = False
# 		if validLoc:
# 			for o in objects:
# 				if o.location == loc:
# 					if o.type in ["Demo", "Mafioso", "Hitman"]:
# 						o.modify_hp(-self.ap)
# 						canStrike = True
# 		return canStrike

class Demo(Unit):
	def __init__(self, loc, color):
		self.hp = 750
		self.charge = 1
		self.ap = 0
		self.alive = True
		super(Demo, self).__init__("Demo", loc, color, "D"+color, 3)

class Hitman(Unit):
	def __init__(self, loc, color):
		self.hp = 50
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
		super(Base, self).__init__("Base", loc, color, "R"+color)

	def build(self, type, loc, objects, player):
		canBuild = True
		for o in objects:
			if o.location == loc:
				canBuild = False

		if type == "Mafioso" and player.money < 10:
			canBuild = False
		if type == "Demo" and player.money < 500:
			canBuild = False
		if type == "Hitman" and player.money < 20:
			canBuild = False

		if canBuild:
			if (0 <= int(loc[0]) < 40) and (0 <= int(loc[1]) < 40):
				if (int(loc[0]) == loc[0]) and (int(loc[1]) == loc[1]):
					if (abs(loc[0] - self.location[0]) <= self.build_max) and (abs(loc[1] - self.location[1]) <= self.build_max):
						if type == "Mafioso":
							objects.append(Mafioso(loc, self.color))
							player.money -= 10
						elif type == "Demo":
							objects.append(Demo(loc, self.color))
							player.money -= 150
						elif type == "Hitman":
							objects.append(Hitman(loc, self.color))
							player.money -= 20

						return objects

	def take_action(self, list, objects, color, player):
		if self.alive:
			if 'build' in list[0]:
				self.build(list[0]['build'][0], color ,list[0]['build'][1] ,objects, player)

class Bank(GameObject):
	def __init__(self, loc):
		self.hp = 2
		self.ap = 0
		self.mp = 0
		self.move_max = 0
		self.alive = True
		self.destructable = False
		super(Bank, self).__init__("Bank", loc, "N", "B2")

class PoliceStation(GameObject):
	def __init__(self, loc):
		self.hp = 2
		self.ap = 0
		self.mp = 0
		self.move_max = 0
		self.alive = True
		self.destructable = False
		super(PoliceStation, self).__init__("Police", loc, "N", "P2")

class TownHall(GameObject):
	def __init__(self, loc):
		self.hp = 2
		self.ap = 0
		self.mp = 0
		self.move_max = 0
		self.alive = True
		self.destructable = False
		super(TownHall, self).__init__("Town Hall", loc, "N", "T1")

# this is how i'm going to extend buildings over multiple tiles (horrible idea but whatever). their type changes every round and for all intents and purposes does not exist. please dont think too hard about this, this was just the first solution i came up with and i dont want users trying to interfere with it in some way
class Ext(GameObject):
	def __init__(self, t, loc, color, icon, destructable=False):
		super(Ext, self).__init__("ext"+str(id(self))+"_"+t, loc, color, icon)
		self.destructable = destructable

# centers of builidngs:
# police station: P2
