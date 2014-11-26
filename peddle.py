import cocos
import pyglet
from cocos.actions import *
from consts import *

class Peddle(cocos.sprite.Sprite):
    palette = {}
    def __init__(self, img='peddle.png',
                 x = None,
                 y = None,
                 vel=None):
        super(Peddle, self).__init__(img)
        if x is None :
            x = WINDOW_W / 2
        if y is None :
            y = self.height / 2
        self.position = x, y    
    
        
    def update(self, keys_pressed):
        if keys_pressed[KEY_LEFT]:
            move = MoveBy((-80, 0), duration=0.2)
            self.do(move)
        if keys_pressed[KEY_RIGHT]:
            move = MoveBy((80, 0), duration=0.2)
            self.do(move)        
