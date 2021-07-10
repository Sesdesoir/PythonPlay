from gameObject import GameObject

class Enemy(GameObject):
    #This creates the Enemy object
    def __init__(self, x, y, width, height, image_path, speed):
        #Super() is creating all the parent information with the parameters we passed in
        super().__init__(x, y, width, height, image_path)

        self.speed = speed

    def move (self, max_width):
        #I wrote the movement as one line changing direction by multiplying by negative one
        #abs(value) will take the absolute value of something. Wanted to note it because I'm impressed.
        if (self.x <= 0) or (self.x >= max_width-self.width):
            self.speed = (self.speed*-1)

        self.x += self.speed
