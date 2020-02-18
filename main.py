import cProfile

from window import *
import player1
import player2

cProfile.runctx("main([player1.turn, player2.turn])", {}, {"main": main, "player1": player1, "player2": player2})

main([player1.turn, player2.turn])
