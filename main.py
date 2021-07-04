import pygame
pygame.init()
#Game code goes between pygame init and quit

#Creates a window in pixels -- will need to see if something like rem, em, vh works
#We diplay constantly but we only create the window once!
width = 800
height = 600
game_window = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()

def run_game_loop():
#Programs *Handle Events *Execute logic *update display
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return
        #The fill take a tuple of r,g,b values (255,255,255) is white
        game_window.fill((255,255,255))
        #Call update everytime you add draw or color the window
        pygame.display.update()
        #Runs 60 times per second --akin to 60fps Higher number =more demanding lower number = less demanding
        clock.tick(60)

run_game_loop()
pygame.quit()
quit()