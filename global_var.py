import objects
import config
import board

TIME_REM = 0
TIME_START = 0
TIME_TOTAL = 180
TIME_POWERUP = 10

lvl1bricks = []
lvl2bricks = []
lvl3bricks = []
lvl4bricks = []

#temp
pu = 5

bricks = 0

powerups = []

#game map
mp = board.Map()

paddle = objects.Paddle(config.paddle,int(int(config.columns)/2) - 3,mp.height-2, 0)

ball = objects.Ball(config.ball,int(int(config.columns)/2),mp.height-3,0,0)

balls = []

#game play
# gp = objects.GamePlay()
gp = objects.GamePlay(0,3)







