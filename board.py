# import global_var
import config
import random
from colorama import init, Fore, Back, Style
import numpy as np
import objects
import bricks
# import global_var

class Map(object):

    height = int(config.rows)
    width = int(config.columns)

    def __init__(self):

        self.start_index = 0
        
        self.matrix = np.array([[" " for i in range(self.width)] for j in range(self.height)])
        
        #keeps track of placement of bricks
        self.brickMatrix = np.array([[0 for i in range(self.width)] for j in range(self.height)])

        self._step = 1

        objects.Brick(" ",0,0,0).initialize_bricks()
            
    
    def render(self):
        for y in range(3, self.height):
            pr = []
            for x in range(self.start_index, self.start_index + config.columns):
                if y == 3:
                    pr.append(Back.LIGHTCYAN_EX + Style.BRIGHT+(self.matrix[y][x] + Style.RESET_ALL))

                elif y == self.height - 1:
                    pr.append(Back.LIGHTCYAN_EX + Style.BRIGHT+(self.matrix[y][x] + Style.RESET_ALL))

                # elif global_var.mp.start_index <= 980 and global_var.mando.get_shield() == 1 and x >= global_var.mando.xget() and x < global_var.mando.xget() +  global_var.mando.get_width() and y >= global_var.mando.yget() and y < global_var.mando.yget() + global_var.mando.get_height():
                #     pr.append(Fore.LIGHTGREEN_EX + Style.BRIGHT +(self.matrix[y][x] + Style.RESET_ALL))
                
                elif x == self.start_index + config.columns - 1:
                    pr.append(Back.LIGHTCYAN_EX + Style.BRIGHT+(self.matrix[y][x] + Style.RESET_ALL))
                
                elif x == self.start_index:
                    pr.append(Back.LIGHTCYAN_EX + Style.BRIGHT+(self.matrix[y][x] + Style.RESET_ALL))
                
                elif self.matrix[y][x] == "/":
                    pr.append(Fore.LIGHTYELLOW_EX + Back.LIGHTYELLOW_EX + Style.BRIGHT +(self.matrix[y][x] + Style.RESET_ALL))

                elif self.matrix[y][x] == "#":
                    pr.append(Fore.BLUE + Back.BLUE + Style.BRIGHT +(self.matrix[y][x] + Style.RESET_ALL))

                elif self.matrix[y][x] == "-":
                    pr.append(Fore.LIGHTRED_EX + Back.LIGHTRED_EX + Style.BRIGHT +(self.matrix[y][x] + Style.RESET_ALL))
                
                elif self.matrix[y][x] == "%":
                    pr.append(Fore.LIGHTGREEN_EX + Back.LIGHTGREEN_EX + Style.BRIGHT +(self.matrix[y][x] + Style.RESET_ALL))

                elif self.matrix[y][x] == "L" or self.matrix[y][x] == "s" or self.matrix[y][x] == "+" or self.matrix[y][x] == "&" or self.matrix[y][x] == "^" or self.matrix[y][x] == "x":
                    pr.append(Fore.GREEN + Back.LIGHTCYAN_EX + Style.BRIGHT +(self.matrix[y][x] + Style.RESET_ALL))

                else:
                    pr.append(Back.WHITE + (self.matrix[y][x] + Style.RESET_ALL))

            print(''.join(pr))


    # def create_side

# class BrickMap(object):

#     height = int(config.rows)
#     width = int(config.columns)

#     def __init__(self):

#         self._x = int(config.columns/6)
#         self.checkBrick = np.array([[" " for i in range(self.width)] for j in range(self.height)])

#         while(self._x < 5 * int(config.columns/6) + 1):

#             for y in range(10,23):
#                 if(y%3 == 0):
#                     brick1 = objects.Brick(config.brick1,self._x,y,1)
#                     global_var.lvl1bricks.append(brick1)
#                 elif(y%3 == 1):
#                     brick1 = objects.Brick(config.brick2,self._x,y,1)
#                     global_var.lvl2bricks.append(brick2)
#                 elif(y%3 == 2):
#                     brick1 = objects.Brick(config.brick3,self._x,y,1)
#                     global_var.lvl3bricks.append(brick3)

#             self._x += 5



