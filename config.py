import os
import sys
import termios, tty, time
from colorama import init, Fore, Back, Style
import numpy as np

rows = 40
columns = 100
frames = 15
lives = 3


brick1 = [["/","/","/","/","/","/","/","/","/","/","/","/","/","/","/"]]
brick2 = [["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]]
brick3 = [["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]]
brick4 = [["%","%","%","%","%","%","%","%","%","%","%","%","%","%","%"]]
nobrick = [[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]]

brickCollsions = ["/","#","-","%"]

paddle = [["T","T","T","T","T","T","T"]]
bpaddle = [["T","T","T","T","T","T","T","T","T","T","T"]]
spaddle = [["T","T","T","T","T"]]

ball = [["o"]]

allPowerups = []

bigPaddle = [["L","L","L"],["L","L","L"]]
allPowerups.append(bigPaddle)

smallPaddle = [["s","s","s"],["s","s","s"]]
allPowerups.append(smallPaddle)

fastBall = [["+","+","+"],["+","+","+"]]
allPowerups.append(fastBall)

thruBall = [["&","&","&"],["&","&","&"]]
allPowerups.append(thruBall)

paddleGrab = [["^","^","^"],["^","^","^"]]
allPowerups.append(paddleGrab)

multiplyBalls = [["x","x","x"],["x","x","x"]]
allPowerups.append(multiplyBalls)


# bigPaddle = [["L","L","L"]]
# allPowerups.append(bigPaddle)

# smallPaddle = [["s","s","s"]]
# allPowerups.append(smallPaddle)

# fastBall = [["+","+","+"]]
# allPowerups.append(fastBall)

# thruBall = [["&","&","&"]]
# allPowerups.append(thruBall)

# paddleGrab = [["^","^","^"]]
# allPowerups.append(paddleGrab)

# multiplyBalls = [["x","x","x"]]
# allPowerups.append(multiplyBalls)



