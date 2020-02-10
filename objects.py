import math
import random

class Player():
    def __init__(self, r, color, name):
        self.resources = r
        self.game_color = color
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
    def __init__(self, t, loc, color, i):
        self.id = id(self)
        self.type = t
        self.location = loc
        self.team = color
        self.icon = i

    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def get_location(self):
        return self.location

    def get_team(self):
        return self.team

    def get_icon(self):
        return self.icon

    def set_icon(self, i):
        self.icon = i

    def get_location_string(self):
        return "(" + str(self.location[0]) + "," + str(self.location[1]) + ")"

class Unit(GameObject):
    def __init__(self, t, loc, color, i):
        super(Unit, self).__init__(t, loc, color, i)

class Mafioso(Unit):
    def __init__(self, t, loc, color, i):
        self.hp=100
        self.move_max=5
        self.ap=25
        self.alive=True
        super(Mafioso, self).__init__(t, loc, color, i)

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
                    if o.get_type() in ["Demo", "Mafioso", "Assassin"]:
                        o.modify_hp(-self.ap)
                        canStrike = True
        return canStrike

    def take_action(self, list, objects, color, player):
        if self.alive:
            if 'move' in list[0]:
                self.move(list[0]['move'], objects)
            elif 'strike' in list[0]:
                self.strike(list[0]['strike'], objects)

class Demo(Unit):
    def __init__(self, t, loc, color, i):
        self.hp=750
        self.charge=1
        self.move_max=3
        self.ap=0
        self.alive=True
        super(Demo, self).__init__(t, loc, color, i)

    def move(self, loc, objects):
    #Checks if various conditions are met
    #Returns True if the move was successful, otherwise returns False
        canMove = True
        for o in objects:
            if o.get_location() == loc:
                canMove = False

        if canMove:
            if (0 <= loc[0] < 40) and (0 <= loc[1] < 40):
                if (int(loc[0]) == loc[0]) and (int(loc[1]) == loc[1]):
                    if (abs(loc[0] - self.location[0]) <= self.move_max) and (abs(loc[1] - self.location[1]) <= self.move_max):
                        self.location = loc
                        return True
        return False

    def take_action(self, list, objects, color, player):
        if self.alive:
            if 'move' in list[0]:
                self.move(list[0]['move'], objects)
            elif 'strike' in list[0]:
                self.strike(list[0]['strike'], objects)

class Assassin(Unit):
    def __init__(self, t, loc, color, i):
        self.hp=50
        self.move_max=10
        self.ap=50
        self.attack_max=5
        self.alive=True
        super(Assassin, self).__init__(t, loc, color, i)

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
                    if o.get_type() in ["Demo", "Mafioso", "Assassin"]:
                        o.modify_hp(-self.ap)
                        canStrike = True
        return canStrike

    def take_action(self, list, objects, color, player):
        if self.alive:
            if 'move' in list[0]:
                self.move(list[0]['move'], objects)
            elif 'strike' in list[0]:
                self.strike(list[0]['strike'], objects)


class Base(Unit):
    def __init__(self, t, loc, color, i):
        self.hp = 2
        self.ap = 0
        self.mp = 0
        self.move_max = 0
        self.build_max = 1
        self.alive = True
        self.destructable = True
        super(Base, self).__init__(t, loc, color, i)

    def build(self, type, color, loc, objects, player):
        canBuild = True
        for o in objects:
            if o.get_location() == loc:
                canBuild = False

        if type == "Mafioso" and player.get_resources() < 10:
            canBuild = False
        if type == "Demo" and player.get_resources() < 500:
            canBuild = False
        if type == "Assassin" and player.get_resources() < 20:
            canBuild = False

        if canBuild:
            if (0 <= int(loc[0]) < 40) and (0 <= int(loc[1]) < 40):
                if (int(loc[0]) == loc[0]) and (int(loc[1]) == loc[1]):
                    if (abs(loc[0] - self.location[0]) <= self.build_max) and (abs(loc[1] - self.location[1]) <= self.build_max):
                        if type == "Mafioso" and color == "B":
                            objects.append(Mafioso("Mafioso",loc,color,"BM"))
                            player.mod_resources(-10)
                        elif type == "Mafioso" and color == "R":
                            objects.append(Mafioso("Mafioso",loc,color,"RM"))
                            player.mod_resources(-10)
                        elif type == "Demo" and color == "B":
                            objects.append(Demo("Demo",loc,color,"BD"))
                            player.mod_resources(-500)
                        elif type == "Demo" and color == "R":
                            objects.append(Demo("Demo",loc,color,"RD"))
                            player.mod_resources(-500)
                        elif type == "Assassin" and color == "B":
                            objects.append(Assassin("Assassin",loc,color,"BA"))
                            player.mod_resources(-20)
                        elif type == "Assassin" and color == "R":
                            objects.append(Assassin("Assassin",loc,color,"RA"))
                            player.mod_resources(-20)

                        return objects

    def take_action(self, list, objects, color, player):
        if self.alive:
            if 'build' in list[0]:
                self.build(list[0]['build'][0], color ,list[0]['build'][1] ,objects, player)

class Bank(Unit):
    def __init__(self, t, loc, color, i):
        self.hp = 2
        self.ap = 0
        self.mp = 0
        self.move_max = 0
        self.alive = True
        self.destructable = False
        super(Bank, self).__init__(t, loc, color, i)

class Neighborhood(Unit):
    def __init__(self, t, loc, color, i):
        self.hp = 2
        self.ap = 0
        self.mp = 0
        self.move_max = 0
        self.alive = True
        self.destructable = True
        super(Neighborhood, self).__init__(t, loc, color, i)
