import os
import pygame

def load_sprites():
	s = {}
	for filename in os.listdir("sprites"):
		if filename.endswith(".png"):
			img = pygame.image.load(os.path.join("sprites", filename))
			s[filename.split(".png")[0]] = pygame.transform.scale(img, (18, 18))
	return s

def sprite_for(text):
	# define tiles here
	return load_sprites()[{
		"--": "grass",
		"P1": "policestationtopleft",
		"P2": "policestationtopright",
		"P3": "policestationbottomleft",
		"P4": "policestationbottomright"
	}[text]]
