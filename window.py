import pygame

from map import Map
from sprites import load_sprites

tile_size = 16
screen = pygame.display.set_mode([640, 640]) # 640x640 is the window size. we can adjust as necessary
pygame.display.set_caption("CRIMELORDS")
clock = pygame.time.Clock()

# pick map here for now we can incorporate this later
map = Map("./maps/emptymap.txt")

sprites = load_sprites()

going = True
# GAME LOOP
while going:
	for event in pygame.event.get():
		if event == pygame.QUIT:
			going = False

	screen.fill((0, 0, 0))
	for row, row_ in enumerate(map):
		for col, cell in row_:
			if cell == "--":
				pygame.draw.rect(screen, (0, 0, 0), [16*col, 16*row, 16, 16])
				screen.blit(sprites["grass"], (col, row))

	clock.tick(5)
	pygame.display.flip()
	break

# title screen can go here i am just going to get straight into the game
