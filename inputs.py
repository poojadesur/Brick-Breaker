from getch import KBHit
import global_var
import global_funct
import config
from time import time,sleep
import objects
import keyboardInput

kb = KBHit()

def move():

    # sleep(0.05)
    #moving paddle
    # ip = kb.getinput()
    getch = keyboardInput.Get()
    ip = keyboardInput.input_to(getch)

    if ip == 'd':
        global_var.paddle.xset(1)

    if ip == 'a':
        global_var.paddle.xset(-1)

    if ip == 'e':
        global_var.ball.beginGame(1)
        global_var.gp.startTimer()
    
    if ip == 'r':
        global_var.ball.resumeGame()

