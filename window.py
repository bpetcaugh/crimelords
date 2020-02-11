import pygame
import sys

from map import Map
from rounds import do_round_red, do_round_blue
from sprites import sprite_for

tile_size = 18
screen = pygame.display.set_mode([720, 720]) # 640x640 is the window size. we can adjust as necessary
pygame.display.set_caption("CRIMELORDS")
clock = pygame.time.Clock()

grid = False

if grid:
	tile_size += 1

# pick map here for now we can incorporate this later
game_map = Map("./maps/onepolicestation.txt")

going = True
# GAME LOOP
while going:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	screen.fill((0, 0, 0))
	for row, row_ in enumerate(game_map.map):
		for col, cell in enumerate(row_):
			pygame.draw.rect(screen, (0, 0, 0), [tile_size*col, tile_size*row, tile_size, tile_size])
			screen.blit(sprite_for("--"), (tile_size*col, tile_size*row))
			if cell != "--":
				screen.blit(sprite_for(cell), (tile_size*col, tile_size*row))

	game_map = do_round_red(game_map)
	game_map = do_round_blue(game_map)

	clock.tick(15)
	pygame.display.flip()
	

pygame.quit()
