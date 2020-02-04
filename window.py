import pygame
import sys

from map import Map
from sprites import load_sprites, sprite_for

tile_size = 16
screen = pygame.display.set_mode([640, 640]) # 640x640 is the window size. we can adjust as necessary
pygame.display.set_caption("CRIMELORDS")
clock = pygame.time.Clock()

# pick map here for now we can incorporate this later
game_map = Map("./maps/emptymap.txt")

sprites = load_sprites()

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
			screen.blit(sprite_for(cell), (tile_size*col, tile_size*row))

	clock.tick(5)
	pygame.display.flip()

pygame.quit()
# title screen can go here i am just going to get straight into the game
