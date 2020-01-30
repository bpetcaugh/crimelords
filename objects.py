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

class Base(Unit):
    def __init__(self, hp, move_max, melee_dmg, melee_rng, cost, drop, alive_state):
        self.hp = 100
        self.move_max = 5
        self.melee_dmg = 25
        self.melee_rng = 1
        self.cost = 10 
        self.drop = 5 
        self.color = ""
        self.alive_state= True
        super(Base, self).__init__( hp, move_max, melee_dmg, melee_rng, cost, drop, alive_state)