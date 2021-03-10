import config
import random
import os
import global_var
# import board
from colorama import Fore, Back, Style
import objects
from time import time
import numpy as np

def you_lose():
    print("\033[15;1H" + Fore.WHITE + Back.BLUE + Style.BRIGHT + ("You Lose!")  .center(config.columns), end='')

def legend():

    print("\033[2;1H" + Fore.WHITE + Back.BLUE + Style.BRIGHT + ( "BRICK BREAKER")  .center(config.columns), end='')

    print("\033[3;1H" + Fore.BLUE + Back.WHITE + Style.BRIGHT + ( "BRICKS").center(config.columns), end='')
    print("\033[4;1H" + Fore.LIGHTGREEN_EX + Back.WHITE + Style.BRIGHT + ("Unbreakable Bricks ").center(config.columns), end='')
    print("\033[5;1H" + Fore.LIGHTRED_EX + Back.WHITE + Style.BRIGHT + ("Level 3 Bricks ").center(config.columns), end='' )
    print("\033[6;1H" + Fore.LIGHTBLUE_EX + Back.WHITE + Style.BRIGHT + ("Level 2 Bricks ")  .center(config.columns), end='')
    print("\033[7;1H" + Fore.LIGHTYELLOW_EX + Back.WHITE + Style.BRIGHT + ("Level 1 Bricks ")  .center(config.columns), end='')

    print("\033[8;1H" + Fore.BLUE + Back.WHITE + Style.BRIGHT + ( "POWERUPS") .center(config.columns), end='')

    print("\033[9;1H" + Fore.GREEN + Back.LIGHTCYAN_EX + Style.BRIGHT + ("Expand Paddle: L") .center(config.columns), end='' )
    print("\033[10;1H" + Fore.GREEN + Back.LIGHTCYAN_EX + Style.BRIGHT + ("Shrink Paddle: s").center(config.columns), end='' )
    print("\033[11;1H" + Fore.GREEN + Back.LIGHTCYAN_EX + Style.BRIGHT + ("Ball Multiplier: x") .center(config.columns), end='')
    print("\033[12;1H" + Fore.GREEN + Back.LIGHTCYAN_EX + Style.BRIGHT + ("Fast Ball: +") .center(config.columns), end='')
    print("\033[13;1H" + Fore.GREEN + Back.LIGHTCYAN_EX + Style.BRIGHT + ("Thru-Ball: &") .center(config.columns), end='')
    print("\033[14;1H" + Fore.GREEN + Back.LIGHTCYAN_EX + Style.BRIGHT + ("Paddle Grab: ^") .center(config.columns), end='')
    
    print(Style.RESET_ALL)


def create_header():
    legend()
    if global_var.TIME_START != 0:
        print("\033[15;1H" + Fore.WHITE + Back.BLUE + Style.BRIGHT + ("SCORE: " + str(global_var.gp.score) +  "   |  LIVES: " + str(global_var.gp.remaininglives) + "   |  TIME: " + str( round(time()) - (global_var.TIME_START)) )  .center(config.columns), end='')
    else:
        print("\033[15;1H" + Fore.WHITE + Back.BLUE + Style.BRIGHT + ("SCORE: " + str(global_var.gp.score) +  "   |  LIVES: " + str(global_var.gp.remaininglives) + "   |  TIME: " + str( 0 ) )  .center(config.columns), end='')

    print(Style.RESET_ALL)

def print_board():
    if global_var.gp.lose == 1:
        you_lose()
    else: create_header()
    global_var.mp.render()

def create_board():

    i = 1
    x = 10
    
    # while x < global_var.mp.width - 250:

    #     no = random.randint(0, 3)
    #     y = random.randint(10, global_var.mp.height-15)
        
    #     i += 1
            
    #     #coins
    #     coin = objects.Object(config.coins, x, y)
    #     global_var.coins.append(coin)
    #     coin.render()

    #     x += random.randint(20, 50)

    #bricks

    
    #ball

def loseLife():

    #if only one balls is remaining
    if(len(global_var.balls) == 1):

        global_var.gp.remaininglives -= 1

        global_var.ball.resumeGame()
        # global_var.ball.beginGame()
        
        #reset ball
        global_var.ball.clear()
        global_var.ball.xdset(int(int(config.columns)/2))
        global_var.ball.ydset(global_var.mp.height-4)
        global_var.ball.xspeed = 0
        global_var.ball.yspeed = -1

        #reset paddle
        global_var.paddle.clear()
        global_var.paddle.xdset(int(int(config.columns)/2) - 3)
        global_var.paddle.ydset(global_var.mp.height-2)
        
        limit = len(global_var.powerups)
        oglen = len(global_var.powerups)
        y=0
        #get rid or powerups
        while y < (limit):
            if y > len(global_var.powerups) - 1: break
            global_var.powerups[y].resetPowerUp()
            if oglen > len(global_var.powerups):
                oglen = len(global_var.powerups)
            else: y+=1

        # for y in range(len(global_var.powerups)):
        #     global_var.powerups[y].resetPowerUp()
            # global_var.powerups.remove(global_var.powerups[y])
            # global_var.powerups = np.delete(global_var.powerups, y)
        
        #get rid of all balls except one - not required
        for i in range(1,len(global_var.balls)):
            global_var.balls[i].clear()
            global_var.balls.remove(global_var.balls[i])

        if global_var.gp.remaininglives == 0:
            restart_game()
            return
    
    else:
        return

def initialize_board():

    create_board()
    global_var.ball.beginGame(0)
    global_var.balls.append(global_var.ball)
    global_var.paddle.render()

    for y in range(len(global_var.lvl1bricks)):
        global_var.lvl1bricks[y].render(y)
    for y in range(len(global_var.lvl2bricks)):
        global_var.lvl2bricks[y].render(y)
    for y in range(len(global_var.lvl3bricks)):
        global_var.lvl3bricks[y].render(y)
    for y in range(len(global_var.lvl4bricks)):
        global_var.lvl4bricks[y].render(y)

    print_board()

def restart_game():

    # display you lose
    global_var.gp.lose = 1
    #set lives back to 3
    global_var.gp.remaininglives = global_var.gp.lives
    
    # reset score
    global_var.gp.score = 0
    # reinitialize bricks
    objects.Brick(" ",0,0,0).initialize_bricks()
    

