from global_var import paddle,ball,lvl1bricks,lvl2bricks,lvl3bricks,lvl4bricks,powerups,balls
import global_var
import global_funct
import config
import os
from colorama import Fore, Back, Style
# import objects
# import time
from time import time,sleep
import inputs
import os

global_funct.initialize_board()

while True:

    os.system("stty -echo")

    ball.clear()
    paddle.clear()
    for y in range(len(powerups)):
        powerups[y].clear()

    inputs.move()
    
    paddle.render()


    for y in range(len(lvl1bricks)):
        lvl1bricks[y].render(y)
    for y in range(len(lvl2bricks)):
        lvl2bricks[y].render(y)
    for y in range(len(lvl3bricks)):
        lvl3bricks[y].render(y)
    for y in range(len(lvl4bricks)):
        lvl4bricks[y].render(y)

    for y in range(len(balls)):
        balls[y].render()
    
    limit = len(powerups)
    oglen = len(powerups)
    y=0
    #rendering of powerups (deleting from powerups list when removing)
    while y < (limit):
        if y > len(powerups) - 1: break
        powerups[y].render()
        if oglen > len(powerups):
            oglen = len(powerups)
        else: y+=1
    
    # print("thrupower:" + str(global_var.gp.thrupower))
    # print("bricks broken " + str(global_var.ball.no_bricks))


    global_funct.print_board()

    if global_var.gp.lose == 1:
        sleep(2)
        # set time back to 0
        global_var.TIME_START = round(time())
        global_var.gp.lose = 0

    os.system("stty echo")


