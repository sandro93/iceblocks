import cocos
from cocos.actions import *
from consts import *

class Peddle(cocos.sprite.Sprite):
    palette = {}
    def __init__(self, img, vel=None):
        super(Peddle, self).__init__(img)

    def update(self, keys_pressed):
        if keys_pressed[KEY_LEFT]:
            move = MoveBy((-80, 0), duration=0.2)
            self.do(move)
        if keys_pressed[KEY_RIGHT]:
            move = MoveBy((80, 0), duration=0.2)
            self.do(move)        
