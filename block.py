import cocos


class Block(cocos.sprite.Sprite):
    def __init__(self, x, y, img='block.png'):
        super(Block, self).__init__(img, anchor=(0, 0))
        self.position = x, y
