import pygame

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
        background = pygame.image.load('assets/background.png')
        #Reassigns the scaled image into the same variable 
        # --scale does have blurring issues. Ideally use the size you are going to use.
        self.background = pygame.transform.scale(background, (self.width , self.height))

        treasure_image = pygame.image.load('assets/treasure.png')
        self.treasure_image = pygame.transform.scale(treasure_image, (50 , 50))

        self.clock = pygame.time.Clock()

    def draw_objects(self):
        #The fill takes a tuple of r,g,b values (255,255,255) is white
        self.game_window.fill((255,255,255))
        #blit for images. Blit takes 2 arguments the image var and a position tuple
        self.game_window.blit(self.background , (0,0))
        self.game_window.blit(self.treasure_image , (375,30))
        #Call update everytime you add draw or color the window
        pygame.display.update()

    def run_game_loop(self):
        # while condition...this is set up to be true until you kill the loop with a break/return 
        #in this case our while loop is broken on a pygame event of type QUIT.
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
            self.draw_objects()
            #Runs 60 times per second --akin to 60fps Higher number =more demanding lower number = less demanding
            self.clock.tick(60)