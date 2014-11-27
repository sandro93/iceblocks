#!/bin/env python3

import cocos
import pyglet
from peddle import Peddle
from ball import Ball
from consts import config, WINDOW_W, WINDOW_H
from icefactory import BlockFactory
from cocos import collision_model as cm
from actions import Blink

# world to view scales
scale_x = WINDOW_W / config.getint("world", "width")
scale_y = WINDOW_H / config.getint("world", "height")


class IceBlocks(cocos.layer.ColorLayer):
    is_event_handler = True
    keys_pressed = {}

    def __init__(self):
        super(IceBlocks, self).__init__(64, 64, 224, 255)
        self.keys_pressed = []
        self.schedule(self.update)
        '''
        = cocos.text.Label(PROGRAM_NAME,
                                 font_name=FONT_NAME,
                                 font_size=FONT_SIZE,
                                 anchor_x='center',
                                 anchor_y='center')
                                 '''
        self.peddle = Peddle()
        self.ball = Ball()
        self.blocks = BlockFactory().level0.blocks
        for block in self.blocks:
            self.add(block, z=1)
        self.add(self.peddle, z=1)
        self.add(self.ball, z=1)
        self.collman = cm.CollisionManagerBruteForce()

    def update(self, dt):
        self.peddle.update(self.keys_pressed)
        self.ball.update(self.peddle)
        self.collman.clear()
        for z, node in self.children:
            if not isinstance(node, Peddle):
                self.collman.add(node)
        self.collman.add(self.ball)
        for obj in self.collman.objs_colliding(self.ball):
            self.remove(obj)

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
