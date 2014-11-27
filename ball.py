import cocos
import math
import time
from consts import BALL_SPEED, WINDOW_W, WINDOW_H


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
        self.ball_rect = self.get_rect()

    def update(self, peddle):
        result = 0
        x, y = self.ball_rect.position[0], self.ball_rect.position[1]
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
                self.ball_rect.position = newPos
                self.position = self.ball_rect.center
                self.dy = -1 * self.dy
                x = math.ceil(self.ball_rect.position[0])
                y = math.ceil(self.ball_rect.position[1])
                time.sleep(1.0)

        newPos = x + self.dx, y + self.dy
        self.ball_rect.position = newPos
        self.position = self.ball_rect.center
        return result
