import pygame
import math
import random

class GameObject():
    #Type:Base, Building, 
    #Location: (x,y)
    #Team: "R", "B", or None
    def __init__(self, t, loc, color, i):
        self.id = random.randint(100, 1000)
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
        self.hp=100
        self.charge=1
        self.alive=True
        self.ap=
        super(Soldier, self).__init__(t, loc, color, i)

class Base(Unit):
    def __init__(self, t, loc, color, i):
        self.hp = 300
        self.ap = 0
        self.mp = 0
        self.move_max = 0
        self.build_max = 1
        self.alive = True
        super(Base, self).__init__(t, loc, color, i)