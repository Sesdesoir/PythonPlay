import pygame
pygame.init()
#Game code goes between pygame init and quit

#Creates a window in pixels -- will need to see if something like rem, em, vh works
width = 800
height = 800
game_window = pygame.display.set_mode((width,height))
#The fill take a tuple of r,g,b values (255,255,255) is white
game_window.fill((255,255,255))
#Call update everytime you add draw or color the window
pygame.display.update()


pygame.quit()
quit()