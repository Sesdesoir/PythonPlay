import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy

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
                                      #   x , y,width,height, img path
        self.treasure_image = GameObject(375, 30, 50, 50, 'assets/treasure.png')
        

        self.level = 1.0

        self.clock = pygame.time.Clock()

        self.reset_map()

    def reset_map(self):
        #The 10 speed is 10 pixles per tick
        self.player = Player(375, 500 , 50 , 50, 'assets/player.png', 10)
        speed = 5 + (self.level *5)
        if self.level >= 4.0:
            self.enemies =[
            Enemy(50, 425, 50, 50, 'assets/enemy.png', speed),
            Enemy(750, 300, 50, 50, 'assets/enemy.png', speed),
            Enemy(75, 175, 50, 50, 'assets/enemy.png', speed),
            ]
        elif self.level >= 2.0:
            self.enemies =[
            Enemy(50, 400, 50, 50, 'assets/enemy.png', speed),
            Enemy(75, 225, 50, 50, 'assets/enemy.png', speed),
            ]
        else:
            self.enemies =[
            Enemy(50, 400, 50, 50, 'assets/enemy.png', speed),
            ]

        

    def draw_objects(self):
        #The fill takes a tuple of r,g,b values (255,255,255) is white
        self.game_window.fill((255,255,255))
        #blit for images. Blit takes 2 arguments the image var and a position tuple
        self.game_window.blit(self.background.image , (self.background.x,self.background.y))
        self.game_window.blit(self.treasure_image.image , (self.treasure_image.x, self.treasure_image.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
        #Call update everytime you add draw or color the window
        pygame.display.update()

    def detect_collision (self, object_1, object_2):
        #Collision occurs when there is an overlap in sides or top in essence share (x,y) coordinate(s)
        #This is written to state where collisions DON'T exist and then anything that passes these checks is therefore a collision.
        # I did the +15 and -15. The blit picture has empty space around the image to be a square.
        #I did the 15px so that the actual visual image is the vertical hitbox rather than the blit box.
        if (object_1.y+15) > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height-15) < object_2.y:
            return False

        if object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False 
        return True

    def check_if_collided(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                self.level = 1.0
                return True
        if self.detect_collision(self.player, self.treasure_image):
            self.level += 0.5
            return True
        return False

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
                    #I couldn't use or after the equals (==) for up and down it produced... interesting results
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        #Move player up
                        player_direction= -1
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        #Move Player down
                        player_direction = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or pygame.K_DOWN or pygame.K_w or pygame.K_s:
                        player_direction=0
            #Draws our images
            self.draw_objects()

            #Detect Collisions...Calling before movement so you can't hypothetically dodge a collision due to loaging
            # Closes the game window if a collision occurs in its current state.
            if self.check_if_collided():
                self.reset_map()
            #Calls the player class move function of object player created above.
            self.player.move(player_direction, self.height)
            #Calls enemy motion
            for enemy in self.enemies:
                enemy.move(self.width)
            #Runs 60 times per second --akin to, but not the same as, 60fps. 
            # Higher number =more demanding lower number = less demanding
            self.clock.tick(60)