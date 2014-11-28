#!/bin/env python3

import cocos
import pyglet
from peddle import Peddle
from ball import Ball
from consts import config, WINDOW_W, WINDOW_H, LIVES
from icefactory import BlockFactory
from cocos import collision_model as cm
from block import Block

from message import MessageLayer
# world to view scales
scale_x = WINDOW_W / config.getint("world", "width")
scale_y = WINDOW_H / config.getint("world", "height")


class IceBlocks(cocos.layer.ColorLayer):
    is_event_handler = True
    keys_pressed = {}

    def __init__(self):
        super(IceBlocks, self).__init__(64, 64, 224, 255)
        self.keys_pressed = []
        self.current_lives = LIVES
        self.level = BlockFactory().get_level(0)
        self.schedule(self.update)

        self.peddle = Peddle()
        self.ball = Ball()
        self.add(self.peddle, z=1)
        self.add(self.ball, z=1)
        self.draw_blocks()
        self.collman = cm.CollisionManagerGrid(0, WINDOW_W, 0, WINDOW_H, self.width, self.height)
        self.draw_lives()

    def restart_game(self):
        self.remove(self.message)
        self.current_lives = LIVES
        self.level = BlockFactory().get_level(0)
        self.draw_blocks()
        self.draw_lives()
        self.resume_scheduler()

    def blocks_remaining(self):
        count = 0
        for z, node in self.children:
            if isinstance(node, Block):
                count += 1
        return count

    def level_up(self):
        self.level = BlockFactory().get_level(self.level.level + 1)
        self.draw_blocks()

    def update(self, dt):
        if self.current_lives > -1:
            self.peddle.update(self.keys_pressed)
            result = self.ball.update(self.peddle)
            if result == -1:
                self.current_lives -= 1
            self.update_lives()
            self.collman.clear()
            for z, node in self.children:
                if isinstance(node, Block):
                    self.collman.add(node)
            for obj in self.collman.objs_colliding(self.ball):
                if self.ball.cshape.center[0] < obj.position[0] or self.ball.cshape.center[0] > obj.position[0]:
                    self.ball.dy = self.ball.dy * -1
                else:
                    self.ball.dx = self.ball.dx * -1
                self.remove(obj)
                break
            if self.blocks_remaining() == 0:
                self.level_up()
        else:
            self.pause_scheduler()
            self.message = MessageLayer()
            self.message.show_message('Game Over!', self.restart_game)
            self.add(self.message)

    def update_lives(self):
        if self.current_lives >= 0 and len(self.lives) > self.current_lives:
            self.remove(self.lives[self.current_lives])
            self.lives.remove(self.lives[self.current_lives])

    def draw_blocks(self):
        for z, node in self.children:
            if isinstance(node, Block):
                self.remove(node)
        for block in self.level.blocks:
            self.add(block, z=1)

    def draw_lives(self):
        self.lives = []
        for i in range(1, self.current_lives + 1):
            live = cocos.sprite.Sprite('heart.png')
            live.position = 20 * i, WINDOW_H - 10
            self.lives.append(live)
            self.add(live, z=2)

    def on_key_press(self, key, modifiers):
        """This function is called when a key is pressed.
        'key' is a constant indicating which key was pressed.
        'modifiers' is a bitwise or of several constants indicating which
        modifiers are active at the time of the press (ctrl, shift, capslock,
        etc.)
        """

        if key in (pyglet.window.key.LEFT, pyglet.window.key.RIGHT):
            self.keys_pressed.append(key)

        return False

    def on_key_release(self, key, modifiers):
        if key in (pyglet.window.key.LEFT, pyglet.window.key.RIGHT):
            self.keys_pressed.remove(key)


cocos.director.director.init(vsync=True, resizable=True,
                             width=WINDOW_W, height=WINDOW_H)
game_layer = IceBlocks()

main_scene = cocos.scene.Scene(game_layer)
if __name__ == '__main__':
    cocos.director.director.run(main_scene)
