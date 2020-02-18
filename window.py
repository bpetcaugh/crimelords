import copy
import pygame
import sys

from map import Map
from sprites import load_sprites, sprite_codes
from objects import *
from points import calc_points

framerate = 5

def get_objects(map):
	objects = []
	for row, row_ in enumerate(map.map):
		for col, cell in enumerate(row_):
			if cell == "--":
				continue
			else:
				try:
					objects += [{
						"RR": Base([col, row], "R"),
						"RB": Base([col, row], "B"),
						"MR": Mafioso([col, row], "R"),
						"MB": Mafioso([col, row], "B"),
						"P1": Ext("Police", [col, row], "N", "P1"),
						"P2": PoliceStation([col, row]),
						"P3": Ext("Police", [col, row], "N", "P3"),
						"P4": Ext("Police", [col, row], "N", "P4"),
						"P5": Ext("Police", [col, row], "N", "P5"),
						"P6": Ext("Police", [col, row], "N", "P6")
					}[cell]]
				except KeyError:
					pass
	return objects

def render_map(old_map, objects):
	nmap = Map(old_map.src, array=[["--" for cols in range(40)] for rows in range(40)], background=old_map.bg)
	for object in objects:
		nmap.map[object.location[1]][object.location[0]] = object.icon
	return nmap

def main(teams, game_map=Map("./maps/realmap.txt", background=""), grid=False):
	tile_size = 18
	screen = pygame.display.set_mode([720, 720]) # 720x720 is the window size. we can adjust as necessary
	pygame.display.set_caption("CRIMELORDS")
	clock = pygame.time.Clock()
	if grid:
		tile_size += 1

	going = True
	# GAME LOOP

	objects = get_objects(game_map)
	sprites = load_sprites()
	print("loaded!")

	influence = [0, 0]
	money = [0, 0]

	while going:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill((0, 0, 0))
		for row, row_ in enumerate(game_map.map):
			for col, cell in enumerate(row_):
				pygame.draw.rect(screen, (0, 0, 0), [tile_size*col, tile_size*row, tile_size, tile_size])
				screen.blit(sprites[sprite_codes["--"]], (tile_size*col, tile_size*row))
				if cell != "--":
					screen.blit(sprites[sprite_codes[cell]], (tile_size*col, tile_size*row))

		p1 = Player(influence[0], money[0], "R", "RED TEAM")
		p2 = Player(influence[0], money[0], "B", "BLUE TEAM")

		obj_copy = copy.copy(objects)
		objects = []
		for obj in obj_copy:
			objects += [teams[0](p1, obj, obj_copy)]
			
		dri, drm = calc_points(objects, "R")
		p1.influence += dri
		p1.money += drm

		game_map = render_map(game_map, objects)
		clock.tick(framerate)
		pygame.display.flip()

		obj_copy = copy.copy(objects)
		for obj in obj_copy:
			objects += [teams[1](p1, obj, obj_copy)]

		dbi, dbm = calc_points(objects, "B")
		p2.influence += dbi
		p2.money += dbm

		game_map = render_map(game_map, objects)
		clock.tick(framerate)
		pygame.display.flip()

	pygame.quit()
