import global_var
import global_funct
import config
from time import time,sleep
import random

class GamePlay():

    def __init__(self,score,lives):
        self.score = score
        self.lives = lives
        self.remaininglives = lives
        # to display you lose header
        self.lose = 0

        #powerup boolean
        self.thrupower = 0
        self.fastball = 0
    
    def startTimer(self):
        global_var.TIME_START = round(time())

    def incScore(self,brick):

        if brick == 1:
            self.score += 10
        if brick == 2:
            self.score += 20
        if brick == 3:
            self.score += 30
    
    def setThruPower(self,boolval):
        self.thrupower = boolval
    
    def setFastBall(self,boolval):
        self.fastball = boolval

class Object():
    
    def __init__(self, character, x, y):
        self.posx = x
        self.posy = y
        self._width = len(character[0])
        self._height = len(character)
        self._shape = character

    def render(self):
        for i in range(self._width):
            for j in range(self._height):
                global_var.mp.matrix[j+self.posy][i+self.posx] = self._shape[j][i]

    def xget(self):
        return self.posx

    def yget(self):
        return self.posy
    
    def xdset(self, x):
        self.posx = x
    
    def ydset(self, x):
        self.posy = x

    def xset(self, x):
        self.posx += x
    
    def yset(self, x):
        self.posy += x

    def clear(self):
        for i in range(self._width):
            for j in range(self._height):
                global_var.mp.matrix[j+self.posy][i+self.posx] = " "

class Brick(Object):

    def __init__(self, character, x, y, level):
        super().__init__(character,x,y)
        self.__level = level
        self.lives = level
    
    def initialize_bricks(self):
        
        flag = 1

        for y in range(9,23):
            x = int(config.columns/6)
            val = y%4
            while(x < (5 * int(config.columns/6) + 1)):
                if(x%4 == (val)):
                    brick1 = Brick(config.brick1,x,y,1)
                    global_var.lvl1bricks.append(brick1)
                elif(x%4 == ((val + 1) % 4) ):
                    brick2 = Brick(config.brick2,x,y,2)
                    global_var.lvl2bricks.append(brick2)
                elif(x%4 == ((val + 2) % 4) ):
                    brick3 = Brick(config.brick3,x,y,3)
                    global_var.lvl3bricks.append(brick3)
                elif(x%4 == ((val + 3) % 4) ):
                    brick4 = Brick(config.brick4,x,y,4)
                    global_var.lvl4bricks.append(brick4)
                x += 15

    #idx is which brick in the lists lvlbricks

    def render(self,idx):
        for i in range(self._width):
            for j in range(self._height):
                global_var.mp.matrix[j+self.posy][i+self.posx] = self._shape[j][i]
                global_var.mp.brickMatrix[j+self.posy][i+self.posx] = self.__level*100 + idx

class PowerUp(Object):

    def __init__(self,character,x,y,powerupidx,idx):
        super().__init__(character, x, y)
        self.yspeed = 1
        #active is when it shows on game
        self.__active = 1
        #activate is powerup being used
        self.__activate = 0
        self.__timeActivated = 0
        self.__idx = powerupidx
        self.puidx = idx

    def resetPowerUp(self):

        self.__active = 0
        self.__activate = 0

        if self.__idx == 0 or self.__idx == 1:
            global_var.paddle.changePaddle(config.paddle)
        if self.__idx == 2:
            # might have to reset ball speeds here
            global_var.gp.setFastBall(False)
            global_var.ball.xspeed = 1
        if self.__idx == 3:
            global_var.gp.setThruPower(False)
        if self.__idx == 4:
            # global_var.gp.UnsetPaddleGrab()
            global_var.paddle.UnsetPaddleGrab()
        if self.__idx == 5:
            self.removeMultiplyBallsPowerUp()

        self.clear()
        self.removePowerUp()

    def removePowerUp(self):
        self.clear()
        global_var.powerups[self.puidx].clear()
        global_var.powerups.remove(global_var.powerups[self.puidx])
        for y in range(self.puidx,len(global_var.powerups)):
            global_var.powerups[y].puidx -= 1
        self.__active = 0

    def checkPowerUpStatus(self):

        #if time has elapsed
        if self.__activate == 1:
            if ( round(time()) - self.__timeActivated ) >= global_var.TIME_POWERUP:
                self.resetPowerUp()
                return 0
        
        #powerUp has hit the bottom
        elif (self.yget() + 3 == config.rows ): 
            self.removePowerUp()
            return 0

        elif self.__active == 0: return 0

        else: return 1
    
    def checkCollision(self):

        #paddle misses catching powerup
        if(self.yget() + 2 == config.rows): self.__active = 0

        #paddle gets powerup
        if(self.__active == 1 and global_var.mp.matrix[self.posy + 1][self.posx] == "T" ):

            self.__active = 0
            self.__activate = 1
            self.__timeActivated = round(time())

            if self.__idx == 0:
                global_var.paddle.changePaddle(config.bpaddle)
            if self.__idx == 1:
                global_var.paddle.changePaddle(config.spaddle)
            if self.__idx == 2:
                global_var.gp.setFastBall(True)
            if self.__idx == 3:
                global_var.gp.setThruPower(True)
            if self.__idx == 4:
                global_var.paddle.setPaddleGrab()
            if self.__idx == 5:
                self.MultiplyBalls()

            # self.clear()
    
    def MultiplyBalls(self):

        curr_ball_num = len(global_var.balls)
        req_ball_num = 2*(curr_ball_num)

        for i in range(curr_ball_num,req_ball_num):
            oldball = global_var.balls[i - curr_ball_num]
            newball = oldball
            newball.xspeed = -(oldball.xspeed)
            global_var.balls.append(newball)
    
    def removeMultiplyBallsPowerUp(self):

        curr_ball_num = len(global_var.balls)
        req_ball_num = (curr_ball_num)/2

        for i in range(curr_ball_num,req_ball_num):
            global_var.balls[i].clear()
            global_var.balls.remove(global_var.balls[i])


    def clear(self):
        for i in range(self._width):
            for j in range(self._height):
                global_var.mp.matrix[j+self.posy][i+self.posx] = " "
        # self.posx = 0
        # self.posy = 0

    def render(self):
        
        self.checkCollision()

        status = self.checkPowerUpStatus()

        # print("powerup being rendered before" + str(status))
        # print("thrupower:" + str(global_var.gp.thrupower))
        # print(str(self.posx) + "  " + str(self.posy))

        if status == 1:
            self.yset(self.yspeed)
            # print("powerup being rendered")
            for i in range(self._width):
                for j in range(self._height):
                    global_var.mp.matrix[j+self.posy][i+self.posx] = self._shape[j][i]
        # else:
        #     for i in range(self._width):
        #         for j in range(self._height):
        #             global_var.mp.matrix[j+self.posy][i+self.posx] = " "



class Paddle(Object):

    def __init__(self, character, x, y, size):
        super().__init__(character, x, y)
        # 0 is default, 1 is large, 2 is small
        self.size = size
        #boolean for PaddleGrab powerup
        self.paddlegrab = 0

    def changePaddle(self, character):

        global_var.paddle.clear()
        char = character
        self._shape = char
        self._width = len(char[0])
        self._height = len(char)
        # print(self.posx)
        # print(self.posy)

        global_var.paddle.render()
    
    def setPaddleGrab(self):
        self.paddlegrab = 1
    
    def UnsetPaddleGrab(self):
        self.paddlegrab = 0


    def render(self):
        for i in range(self._width):
            for j in range(self._height):
                global_var.mp.matrix[j+self.posy][i+self.posx] = self._shape[j][i]

    
class Ball(Object):

    def __init__(self,character,x,y,xspeed,yspeed):
        super().__init__(character,x,y)
        self.__motion = 0
        self.xspeed = 0
        self.yspeed = 0
        global_var.bricks = 0
    
    def changeBallSpeed(self,speedx,speedy):
        # !!!! check if this is right bro
        self.xspeed += speedx
        self.yspeed += speedy
    
    #determines where on the paddle the ball hit
    def ballPaddlePosition(self):

        no_T_left = 0
        no_T_right = 0
        
        y = self.yget() + 1
        x = self.xget()

        while(global_var.mp.matrix[y][x] == "T"):
            no_T_left += 1
            x -= 1
        
        x = self.xget()

        while(global_var.mp.matrix[y][x] == "T"):
            no_T_right += 1
            x += 1

        speed_change = no_T_left - no_T_right

        # print(speed_change)

        return speed_change
    
    def createPowerUp(self):
        
        # if(global_var.bricks%5 == 0 and global_var.bricks != 0):
        #     print("powerupcreated")
        # print("\n\n")
        # if(global_var.bricks == 1):
        if(global_var.bricks%3 == 0 and global_var.bricks != 0):
            powerupidx = random.randint(0,4)
            character = []
            character = config.allPowerups[powerupidx]
            # print(character)
            powerup = PowerUp(character,self.posx,self.posy,powerupidx,len(global_var.powerups))
            global_var.powerups.append(powerup)

    def removeBrick(self,level,idx):

        if level == 1:

            if global_var.gp.thrupower == 0: global_var.lvl1bricks[idx].lives -= 1
            elif global_var.gp.thrupower == 1: global_var.lvl1bricks[idx].lives = 0
                
            lives_left = global_var.lvl1bricks[idx].lives

            nobrick = Brick(config.nobrick, global_var.lvl1bricks[idx].posx, global_var.lvl1bricks[idx].posy, 1)
            global_var.lvl1bricks[idx] = nobrick
            global_var.gp.incScore(1)
            global_var.bricks += 1
            self.createPowerUp()

        if level == 2:
            if global_var.gp.thrupower == 0: global_var.lvl2bricks[idx].lives -= 1
            elif global_var.gp.thrupower == 1: global_var.lvl2bricks[idx].lives = 0
            
            lives_left = global_var.lvl2bricks[idx].lives
            
            if lives_left == 1:
                newbrick = Brick(config.brick1, global_var.lvl2bricks[idx].posx, global_var.lvl2bricks[idx].posy, 2)
                newbrick.lives = 1
                global_var.lvl2bricks[idx] = newbrick

            if lives_left == 0:
                global_var.gp.incScore(2)
                global_var.bricks += 1
                newbrick = Brick(config.nobrick, global_var.lvl2bricks[idx].posx, global_var.lvl2bricks[idx].posy, 2)
                newbrick.lives = 0

                global_var.lvl2bricks[idx] = newbrick
            self.createPowerUp()

        if level == 3:
            if global_var.gp.thrupower == 0: global_var.lvl3bricks[idx].lives -= 1
            elif global_var.gp.thrupower == 1: global_var.lvl3bricks[idx].lives = 0
            
            lives_left = global_var.lvl3bricks[idx].lives
            
            if lives_left == 2:
                newbrick = Brick(config.brick2, global_var.lvl3bricks[idx].posx, global_var.lvl3bricks[idx].posy, 3)
                newbrick.lives = 2
                global_var.lvl3bricks[idx] = newbrick

            
            if lives_left == 1:
                newbrick = Brick(config.brick1, global_var.lvl3bricks[idx].posx, global_var.lvl3bricks[idx].posy, 3)
                newbrick.lives = 1
                global_var.lvl3bricks[idx] = newbrick


            if lives_left == 0:
                global_var.gp.incScore(3)
                global_var.bricks += 1
                newbrick = Brick(config.nobrick, global_var.lvl3bricks[idx].posx, global_var.lvl3bricks[idx].posy, 3)
                newbrick.lives = 0
                global_var.lvl3bricks[idx] = newbrick
            self.createPowerUp()

        if level == 4:
            if global_var.gp.thrupower == 1: 
                global_var.lvl4bricks[idx].lives = 0
                nobrick = Brick(config.nobrick, global_var.lvl4bricks[idx].posx, global_var.lvl4bricks[idx].posy, 1)
                global_var.lvl4bricks[idx] = nobrick
                global_var.gp.incScore(0)
                global_var.bricks += 1
                self.createPowerUp()

            
    def brickCollision(self,marker):
        
        marker = int(marker)
        level = int(marker/100)
        idx = int(marker%100)
       
        self.removeBrick(level,idx)


    def checkCollision(self):

        #top
        if global_var.mp.matrix[self.yget()-1][self.xget()] in config.brickCollsions:
            self.brickCollision(global_var.mp.brickMatrix[self.yget()-1][self.xget()])
            # self.ydset(0)
            self.yset(-(self.yspeed))
            self.yspeed = -(self.yspeed)
        
        # bottom
        elif global_var.mp.matrix[self.yget()+1][self.xget()] in config.brickCollsions:
            self.brickCollision(global_var.mp.brickMatrix[self.yget()+1][self.xget()])
            # self.ydset(0)
            self.yset(-(self.yspeed))
            self.yspeed = -(self.yspeed)

        # left + diag down from left outside + diag up from left outside
        elif global_var.mp.matrix[self.yget()][self.xget()-1] in config.brickCollsions:
            self.brickCollision(global_var.mp.brickMatrix[self.yget()][self.xget()-1])
            # self.xdset(0)
            self.xspeed = -(self.xspeed)

        # right + diag down from right outside + diag up from right outside
        elif global_var.mp.matrix[self.yget()][self.xget()+1] in config.brickCollsions:
            self.brickCollision(global_var.mp.brickMatrix[self.yget()][self.xget()+1])
            # self.xdset(0)
            self.xspeed = -(self.xspeed)
        
        #diagonals
        elif global_var.mp.matrix[self.yget()+self.yspeed][self.xget()+self.xspeed] in config.brickCollsions:
            self.brickCollision(global_var.mp.brickMatrix[self.yget()+self.yspeed][self.xget()+self.xspeed])
            self.xspeed = -(self.xspeed)


    def ballMove(self):

        if self.__motion == 1:

            # if (self.xspeed+self.posx > config.columns - 1 or self.xspeed+self.posx < 1):
            #     self.xspeed = -(self.xspeed)

            # elif (self.yspeed+self.posy > config.rows - 2 or  self.yspeed+self.posy < 1):
            #     self.yspeed = -(self.yspeed)
            
            # ball hits side box borders
            if self.xget() >= (config.columns - 2) or self.xget() <= 2:
                self.xspeed = -(self.xspeed)
                # print(self.xspeed)

            #ball hits top edge of box
            elif self.yget() <= 4 :
                self.yspeed = -(self.yspeed)
            
            # ball hits bottom edge of box
            elif self.yget() >= config.rows - 2 :
                # self.yspeed = -(self.yspeed)
                # you lose !
                global_funct.loseLife()

            # check if ball hits bricks
            if ((self.yget() + 8 <= config.rows - 3 and self.yget() - 8 >= 4 ) and (self.xget() + 8 < config.columns - 3 and self.xget() - 8 >= 2)):
                self.checkCollision()
            
            # ball hits paddle
            #speed of ball changes based on where it hits on the paddle
            if(global_var.mp.matrix[self.yget()+1][self.xget()] == "T"):

                if global_var.paddle.paddlegrab == 1:
                    self.__motion = 0
                    global_var.paddle.UnsetPaddleGrab()
                    global_var.ball.ydset(global_var.paddle.yget()-2)
                
                else: 
                    self.xspeed = self.ballPaddlePosition()
                    # if ball is coming from the top
                    if(self.yspeed > 0): self.yspeed = -(self.yspeed)
            
            if global_var.gp.fastball == True:
                if self.xspeed > 0: self.xspeed = 8
                if self.xspeed < 0: self.xspeed = -8

            self.yset(self.yspeed)
            self.xset(self.xspeed)

    def render(self):
        # sleep(0.05)

        self.ballMove()
        # if self.__motion == 1:
        # print(self.posx,self.posy)
        # print(self.posx,self.posy, end='\r', flush=True)
        # # print("\n")
        # print(self.xspeed,self.yspeed, end='\r', flush=True)

        # print(self.xspeed,self.yspeed)

        for i in range(self._width):
            for j in range(self._height):
                if (i+self.posx < config.columns - 1 and i+self.posx > 1) and (j+self.posy < config.rows - 1 and j+self.posy > 1):
                    global_var.mp.matrix[j+self.posy][i+self.posx] = self._shape[j][i]
    
    def clear(self):
        for i in range(self._width):
            for j in range(self._height):
                if (i+self.posx < config.columns - 1 and i+self.posx > 1) and (j+self.posy < config.rows - 1 and j+self.posy > 1):
                    global_var.mp.matrix[j+self.posy][i+self.posx] = " "

    def beginGame(self,begin):
        self.yspeed = -1
        if begin == 1:
            self.__motion = 1
    
    def resumeGame(self):
        self.__motion = 0
        global_var.paddle.UnsetPaddleGrab()


    