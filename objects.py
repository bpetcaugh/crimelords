import pygame
import math
import random

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

class Demo(Unit):
    def __init__(self, t, loc, color, i):
        self.hp=300
        self.charge=1
        self.move_max=2
        self.ap=0
        self.alive=True
        super(Soldier, self).__init__(t, loc, color, i)

    def move(self, loc, objects):
    #Checks if various conditions are met
    #Returns True if the move was successful, otherwise returns False
        canMove = True
        for o in objects:
            if o.get_location() == loc:
                canMove = False

        if canMove:
            if (0 <= loc[0] < 20) and (0 <= loc[1] < 20):
                if (int(loc[0]) == loc[0]) and (int(loc[1]) == loc[1]):
                    if (abs(loc[0] - self.location[0]) <= self.move_max) and (abs(loc[1] - self.location[1]) <= self.move_max):
                        self.location = loc
                        return True
        return False

    def strike(self, loc, objects):
    #Checks for valid location
        validLoc = False
        if (0 <= loc[0] < 20) and (0 <= loc[1] < 20):
            if (int(loc[0]) == loc[0]) and (int(loc[1]) == loc[1]):
                if (abs(loc[0] - self.location[0]) <= self.attack_max) and (abs(loc[1] - self.location[1]) <= self.attack_max):
                    validLoc = True

        #Checks if object can be attacked
        canStrike = False
        if validLoc:
            for o in objects:
                if o.get_location() == loc:
                    if o.get_type() in ["Demo"]:
                        o.modify_hp(-self.ap)
                        canStrike = True

        return canStrike

    def take_action(self, list, objects, color, player):
        if self.alive:
            if 'move' in list[0]:
                self.move(list[0]['move'], objects)
            elif 'strike' in list[0]:
                self.strike(list[0]['strike'], objects)
'''
#Depending on if demo is suicide bomber or not.
class Charge(Unit):
    def __init__(self, t, loc, color, i):
        self.turns=3
        super(Unit, self).__init__(t, loc, color, i)
    
    def countdown(self):
        if self.turns>=0:
            self.turns-=1
        if self.turns==0:
            Detonate(self)

    def Detonate(self, t, loc, color, i):
        self.radius=3
'''
class Base(Unit):
    def __init__(self, t, loc, color, i):
        self.hp = 200
        self.ap = 0
        self.mp = 0
        self.move_max = 0
        self.build_max = 1
        self.alive = True
        super(Base, self).__init__(t, loc, color, i)