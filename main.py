#Programs in a nutshell *Handle Events *Execute logic *update display
import pygame
from game import Game

#Game code goes between pygame init and quit
pygame.init()
#Save a game object in this case the window as a var and run the window loop
game = Game()
game.run_game_loop()

pygame.quit()
quit()