import os
import pygame

def load_sprites():
	s = {}
	for filename in os.listdir("sprites"):
		if filename.endswith(".png"):
			img = pygame.image.load(os.path.join("sprites", filename))
			s[filename.split(".png")[0]] = pygame.transform.scale(img, (18, 18))
	return s

sprite_codes = {
	"--": "grass",
	"P1": "policestationtopleft",
	"P2": "policestationtopmiddle",
	"P3": "policestationtopright",
	"P4": "policestationbottomleft",
	"P5": "policestationbottommiddle",
	"P6": "policestationbottomright",
	"MB": "mafiosoblue",
	"MR": "mafiosored",
	"HB": "hitmanblue",
	"HR": "hitmanred",
	"RB": "restaurantblue",
	"RR": "restaurantred",
	"B1": "banktopleft",
	"B2": "banktopmiddle",
	"B3": "banktopright",
	"B4": "bankbottomleft",
	"B5": "bankbottommiddle",
	"B6": "bankbottomright"
}
