import cProfile
import sys

from window import *
import player1
import player2

try:
	if sys.argv[1] in ["-d", "--debug"]:
		cProfile.runctx("main([player1.turn, player2.turn])", {}, {"main": main, "player1": player1, "player2": player2})
		sys.exit()
except IndexError:
	pass

main([player1.turn, player2.turn])