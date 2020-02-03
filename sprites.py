import os
import pygame

def load_sprites():
	s = {}
	for filename in os.listdir("sprites"):
		if filename.endswith(".png"):
			img = pygame.image.load(os.path.join("sprites", filename))
			s[filename.split(".png")[0]] = pygame.transform.scale(img, (16, 16))
	return s
