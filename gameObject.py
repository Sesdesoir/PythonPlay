import pygame

class GameObject:
    def __init__(self , x, y, width, height, image_path):
        #creates a local variable not accessible outside of here
        image = pygame.image.load(image_path)
        #Reassigns the scaled image into the same variable 
        # --scale does have blurring issues. Ideally use the size you are going to use.
        #This self.image is available anywhere as an object property
        self.image = pygame.transform.scale(image, (width, height))

        self.x = x
        self.y = y
        self.width = width
        self.height = height