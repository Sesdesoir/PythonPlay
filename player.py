from gameObject import GameObject
#Player is going to be a sub class of GameObject. GameObject is like the parent
#We want everything GameObject has PLUS some stuff exclusive to Player.
#This is like when we did the vehicle/car/boat classes
class Player(GameObject):
    #This creates the Player object
    def __init__(self, x, y, width, height, image_path, speed):
        #Super() is creating all the parent information with the parameters we passed in
        super().__init__(x, y, width, height, image_path)

        self.speed = speed
    def move (self, direction):
        #Up arrow key will be equivalent to 1 down arrow will be equivalent to -1
        self.y += (direction * self.speed)