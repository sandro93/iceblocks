import cocos
import pyglet
from cocos.actions import *
from actions import *
from consts import *
from peddle import Peddle

class Ball(cocos.sprite.Sprite):
    palette = {}
    dx = consts = BALL_SPEED
    dy = consts = BALL_SPEED
    
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
    
        
    def update(self, keys_pressed, peddle):
        x, y = self.position
        peddle_x, peddle_y = peddle.position
        if x == WINDOW_W or x == 0:
            dx = -1 * dx
        if y == WINDOW_Y or y <= peddle.height:
            dy = -1 * dx
        
        self.do(MoveBy((self.dx, self.dy), duration=0.2))
        
