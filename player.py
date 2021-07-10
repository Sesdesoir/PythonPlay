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

    def move (self, direction, max_height):
        # the and is important! We don't want to move off the screen, however we want to be allowed to move in other directions.
        if (self.y >= max_height-self.height and direction >0) or (self.y == 0 and direction<0):
            return
    #Up arrow key will be equivalent to -1 down arrow will be equivalent to 1
    #This is because (0.0) is the top left corner. Meaning 0 is the top and max height of 600 is the bottom
        self.y += (direction * self.speed)