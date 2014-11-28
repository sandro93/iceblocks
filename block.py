import pprint
import cocos
from cocos import collision_model as cm
from cocos import euclid as eu


class Block(cocos.sprite.Sprite):
    def __init__(self, x, y, img='block.png'):
        super(Block, self).__init__(img, anchor=(0, 0))
        self.position = x, y
        self.cshape = cm.AARectShape(
            eu.Vector2(x+self.width/2, y+self.height/2),
            self.width / 2,
            self.height / 2
        )
