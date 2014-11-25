import cocos

PROGRAM_NAME= "Ice Blocks"
FONT_NAME = 'Times New Roman'
FONT_SIZE = 32
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

from cocos.actions import *

class HelloActions(cocos.layer.ColorLayer):
    is_event_handler = True
    
    def __init__(self):
        self.keys_pressed = set()
        super(HelloActions, self).__init__(64, 64, 224, 255)
        label = cocos.text.Label(PROGRAM_NAME,
                                 font_name= FONT_NAME,
                                 font_size=FONT_SIZE,
                                 anchor_x='center',
                                 anchor_y='center')
        label.position = WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2
        self.add(label)

        self.sprite = cocos.sprite.Sprite('peddle.png')
        self.sprite.position =  WINDOW_WIDTH / 2, WINDOW_HEIGHT / self.sprite.height
        self.sprite.scale = 3
        self.add(self.sprite, z=1)

        scale = ScaleBy(3, duration=2)

        label.do(Repeat(scale + Reverse(scale)))
        # sprite.do(Repeat(Reverse(scale) + scale))
    def on_key_press(self, key, modifiers):
        """This function is called when a key is pressed.
        'key' is a constant indicating which key was pressed.
    'modifiers' is a bitwise or of several constants indicating which
        modifiers are active at the time of the press (ctrl, shift, capslock, etc.)
    """
        move = MoveBy((80, 0), duration=1)
        self.sprite.do(move)

cocos.director.director.init(width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
hello_layer = HelloActions()

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

cocos.director.director.run(main_scene)
