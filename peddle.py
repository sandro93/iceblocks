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
            if self.x - (self.width / 2) >= 0 :
                if self.x - (self.width / 2) > self.width / 2 :
                    dpos = self.width / 2
                else :
                    dpos = self.x - (self.width / 2)
            move = MoveBy((-dpos, 0), duration=0.07)
            self.do(move)
        elif keys_pressed[KEY_RIGHT]:
            if (self.x + (self.width / 2)) < WINDOW_W :
                if WINDOW_W - (self.x + (self.width / 2)) > self.width / 2 :
                    dpos = self.width / 2
                else :
                    dpos = WINDOW_W - (self.x + (self.width / 2))                
                move = MoveBy((dpos, 0), duration=0.07)
                self.do(move)        
