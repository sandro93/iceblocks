import cocos
import pyglet
import math
import time
from cocos.actions import *
from actions import *
from consts import *
from peddle import Peddle

class Ball(cocos.sprite.Sprite):
    dx = dy = BALL_SPEED
    pos_x = 0
    #ball_rect = get_rect()
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
        self.ball_rect = self.get_rect()
        #self.pos_x = self.position[0] - self.width/ 2
    
        
    def update(self, peddle):
        x, y = self.ball_rect.position[0], self.ball_rect.position[1]
        center_x, center_y = self.position[0], self.position[1]  
        peddle_rect = peddle.get_rect()
        
        peddle_x, peddle_y = math.ceil(peddle_rect.position[0]), math.ceil(peddle.height)
       
        if x+self.width > WINDOW_W or x < 0:
            self.dx = -1 * self.dx
        if y+self.height >= WINDOW_H:
            self.dy = -1 * self.dy
        if y == peddle.height:
            if (math.ceil(x) >= peddle_x and math.ceil(x) <= (peddle_x + peddle.width)) or (x+self.width >= peddle_x and x <= (peddle_x + peddle.width)):
                self.dy = -1 * self.dy                
                self.dx = (center_x-peddle.position[0]) / 7                
            else:                
                newPos = peddle.position[0], peddle.height                                
                self.ball_rect.position = newPos
                self.position = self.ball_rect.center
                self.dy = -1 * self.dy
                x, y = math.ceil(self.ball_rect.position[0]), math.ceil(self.ball_rect.position[1])
                time.sleep(1.0)
                # self.remove_action(self.mv)
                #self.do(MoveTo((WINDOW_W / 2, WINDOW_H / 2), duration = 0.2))
        
        newPos = x + self.dx, y + self.dy
        self.ball_rect.position = newPos
        self.position = self.ball_rect.center
#        self.mv = self.do(MoveBy((self.dx, self.dy), duration=0.21))
#        self.do(MoveBy((self.dx, self.dy), duration=0.2))
