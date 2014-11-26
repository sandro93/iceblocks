#!/bin/env python3

import cocos
import configparser
import pyglet
import pprint
import message
import peddle
from consts import *
from cocos.actions import *

# world to view scales
scale_x = config.getint("window", "width")/config.getint("world", "width")
scale_y = config.getint("window", "height")/config.getint("world", "height")

class IceBlocks(cocos.layer.ColorLayer):
    is_event_handler = True
    def __init__(self):
        super(IceBlocks, self).__init__(64, 64, 224, 255)
        self.bindings = config['bindings']
        self.keys_pressed = {}
        self.keys_pressed[KEY_LEFT] = False
        self.keys_pressed[KEY_RIGHT] = False
        self.schedule(self.update)
        '''
        = cocos.text.Label(PROGRAM_NAME,
                                 font_name=FONT_NAME,
                                 font_size=FONT_SIZE,
                                 anchor_x='center',
                                 anchor_y='center')
                                 '''
        self.sprite = cocos.sprite.Sprite(pyglet.resource.image('peddle.png'))
        self.sprite.position =  WINDOW_W / 2, self.sprite.height / 2
        self.sprite.scale = 2
        self.add(self.sprite, z=1)
        scale = ScaleBy(3, duration=1)
    def update(self, dt):
        if self.keys_pressed[KEY_LEFT]:
            move = MoveBy((-80, 0), duration=0.2)
            self.sprite.do(move)
        if self.keys_pressed[KEY_RIGHT]:
            move = MoveBy((80, 0), duration=0.2)
            self.sprite.do(move)        

    def on_key_press(self, key, modifiers):
        """This function is called when a key is pressed.
        'key' is a constant indicating which key was pressed.
        'modifiers' is a bitwise or of several constants indicating which
        modifiers are active at the time of the press (ctrl, shift, capslock, etc.)
        """
        if key == pyglet.window.key.LEFT:
            self.keys_pressed[KEY_LEFT] = True
            return True
        if key == pyglet.window.key.RIGHT:
            self.keys_pressed[KEY_RIGHT] = True
            return True
        return False
    def on_key_release(self, key, modifiers):
        self.keys_pressed[KEY_LEFT] = False
        self.keys_pressed[KEY_RIGHT] = False
        
cocos.director.director.init(vsync = True, resizable = True, width=WINDOW_W, height=WINDOW_H)
hello_layer = IceBlocks()

def Blink(times, duration):
    return (
        Hide() + Delay(duration/(times*2)) +
        Show() + Delay(duration/(times*2))
    ) * times


# hello_layer.do(RotateBy(360, duration=10))
# hello_layer.do( Twirl( grid=(16,12), duration=4) )
# hello_layer.do( Lens3D( grid=(32,24), duration=5 ))
# hello_layer.do(Blink(2, 2))
main_scene = cocos.scene.Scene(hello_layer)
if __name__ == '__main__':
    cocos.director.director.run(main_scene)
