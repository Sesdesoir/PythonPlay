import pygame
from gameObject import GameObject
from player import Player
    #Self is kinda like this. It references information related to itself/this specific object
class Game:
    # __init__ is a special designation in a python class
    # def is the keyword used to create a custom function the colon : indicates the end of the defining and everything indented after is part of the function
    # Javascript equivalent: function runGameLoop = () => {}
    def __init__(self):
        #Creates a window in pixels -- will need to see if something like rem, em, vh works
        #We diplay constantly but we only create the window once! So All creation happens outside the function
        # and everything we want maintained and displayed happens inside the function
        self.width = 800
        self.height = 600
        self.game_window = pygame.display.set_mode((self.width,self.height))
                        #GameObject is a class we created in file gameObject.py
        self.background = GameObject(0,0, self.width, self.height, 'assets/background.png')

        self.treasure_image = GameObject(375, 30, 50, 50, 'assets/treasure.png')
        #The 10 speed is 10 pixles per tick
        self.player = Player(375, 500 , 50 , 50, 'assets/player.png', 10)
        self.clock = pygame.time.Clock()

    def draw_objects(self):
        #The fill takes a tuple of r,g,b values (255,255,255) is white
        self.game_window.fill((255,255,255))
        #blit for images. Blit takes 2 arguments the image var and a position tuple
        self.game_window.blit(self.background.image , (self.background.x,self.background.y))
        self.game_window.blit(self.treasure_image.image , (self.treasure_image.x, self.treasure_image.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        #Call update everytime you add draw or color the window
        pygame.display.update()

    def run_game_loop(self):
        #function variable
        player_direction=0
        # while condition...this is set up to be true until you kill the loop with a break/return 
        #in this case our while loop is broken on a pygame event of type QUIT.
        while True:
            #pygame event handler
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                #elif is else if
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        #Move player up
                        player_direction= -1
                    elif event.key == pygame.K_DOWN:
                        #Move Player down
                        player_direction = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or pygame.K_DOWN:
                        player_direction=0
                        
            self.draw_objects()
            #Calls the player class move function of object player created above.
            self.player.move(player_direction)
            #Runs 60 times per second --akin to 60fps Higher number =more demanding lower number = less demanding
            self.clock.tick(60)