import cocos
import pyglet
from cocos.actions import *
from actions import *
from consts import *
from peddle import Peddle

class Ball(cocos.sprite.Sprite):
    dx = dy = BALL_SPEED
    def __init__(self, img='ball.png',
                 x = None,
                 y = None,
                 vel=None):
        super(Ball, self).__init__(img)
        if x is None :
            x = WINDOW_W / 2
        if y is None :
            y = WINDOW_H / 2
        self.position = x, y    
        self.dx = self.dy = BALL_SPEED
    
        
    def update(self, keys_pressed, peddle):
        x, y = self.position
        peddle_x, peddle_y = peddle.position
        if x > WINDOW_W or x < 0:
            self.dx = -1 * self.dx
        if y >= WINDOW_H:
            self.dy = -1 * self.dy
            
        if y < peddle.height:
            if x >= peddle_x and (x + self.width) <= (peddle_x + peddle.width):
                self.dy = -1 * self.dy
            else:
                newPos = WINDOW_W / 2, WINDOW_H / 2
                x, y = newPos
                self.position = newPos
                self.dy = -1 * self.dy
                # self.remove_action(self.mv)
                #self.do(MoveTo((WINDOW_W / 2, WINDOW_H / 2), duration = 0.2))
        
        newPos = x + self.dx, y + self.dy
        self.position = newPos
#        self.mv = self.do(MoveBy((self.dx, self.dy), duration=0.21))
#        self.do(MoveBy((self.dx, self.dy), duration=0.2))
