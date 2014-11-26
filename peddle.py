import cocos
from consts import *

class Peddle(cocos.sprite.Sprite):
    palette = {}
    def __init__(self, cx, cy, img, vel=None):
        super(Actor, self).__init__(img)

    def update(keys_pressed):
        if keys_pressed[KEY_LEFT]:
            move = MoveBy((-80, 0), duration=0.2)
            self.sprite.do(move)
        if keys_pressed[KEY_RIGHT]:
            move = MoveBy((80, 0), duration=0.2)
            self.sprite.do(move)        
