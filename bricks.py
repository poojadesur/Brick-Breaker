import global_var
import global_funct
import config
import time
import random

# can i do like this
class Bricks():

    def __init__(self):
        print("hi")
    # def __init__(self):
    #     super().__init__(character,x,y)
    #     self.__level = level
    
    # def collide(self):
    #     self._level -= 1
    
    # def breakBrick(self):
    #     for i in range(self._width):
    #         for j in range(self._height):
    #             global_var.mp.matrix[j+self._posy][i+self._posx] = " "

    def initialize_bricks(self):
        #bricks
        self._brickx = int(config.columns/6)

        while(self._brickx < 5 * int(config.columns/6) + 1):
            
            for y in range(9,23):
                if(y%3 == 0):
                    brick1 = objects.Brick(config.brick1,self._brickx,y,1)
                    global_var.lvl1bricks.append(brick1)
                elif(y%3 == 1):
                    brick2 = objects.Brick(config.brick2,self._brickx,y,1)
                    global_var.lvl2bricks.append(brick2)
                elif(y%3 == 2):
                    brick3 = objects.Brick(config.brick3,self._brickx,y,1)
                    global_var.lvl3bricks.append(brick3)
            self._brickx += 5

