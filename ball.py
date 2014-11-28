import cocos
import math
import time
from consts import BALL_SPEED, WINDOW_W, WINDOW_H
from cocos import collision_model as cm, euclid as eu


class Ball(cocos.sprite.Sprite):
    dx = dy = BALL_SPEED
    pos_x = 0

    def __init__(self, img='ball.png',
                 x=None,
                 y=None,
                 vel=None):
        super(Ball, self).__init__(img)
        if x is None:
            x = WINDOW_W / 2
        if y is None:
            y = WINDOW_H / 2
        self.position = x, y
        self.dx = self.dy = BALL_SPEED
        self.cshape = cm.AARectShape(eu.Vector2(x, y), self.width / 2, self.height / 2)

    def update(self, peddle):
        x, y = self.cshape.center[0], self.cshape.center[1]
        result = 0
        center_x = self.position[0]

        peddle_x, peddle_y = math.ceil(peddle.position[0]), math.ceil(peddle.height)

        if x + self.width > WINDOW_W or x < 0:
            self.dx = -1 * self.dx
        if y + self.height >= WINDOW_H:
            self.dy = -1 * self.dy
        if y == peddle.height:
            if (math.ceil(x) >= peddle_x and math.ceil(x) <= (peddle_x + peddle.width)) or (x + self.width >= peddle_x and x <= (peddle_x + peddle.width)):
                self.dy = -1 * self.dy
                self.dx = (center_x - (peddle.position[0] + peddle.width/2)) / 7
            else:
                result = -1
                newPos = peddle.position[0]+peddle.width/2, peddle.height
                self.update_position(newPos)
                self.dy = -1 * self.dy
                x = math.ceil(self.cshape.center[0])
                y = math.ceil(self.cshape.center[1])
                time.sleep(1.0)

        newPos = x + self.dx, y + self.dy
        self.update_position(newPos)
        return result

    def update_position(self, new_position):
        self.position = new_position
        self.cshape.center = new_position
