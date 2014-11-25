import cocos
import configparser

config = configparser.ConfigParser()
config.sections()
config.read('iceblocks.conf')

PROGRAM_NAME= "Ice Blocks"
# View
FONT_NAME = config.get('view', 'font_name')
FONT_SIZE = config.getint('view', 'font_size')

# Window
WINDOW_W = config.getint('window', 'width')
WINDOW_H = config.getint('window', 'height')
RESIZABLE = config.getboolean('window', 'resizable')

# Bindings
KEY_LEFT = config.get('bindings', 'key.LEFT')
KEY_RIGHT = config.get('bindings', 'key.RIGHT')
from cocos.actions import *

# world to view scales
scale_x = config.getint("window", "width")/config.getint("world", "width")
scale_y = config.getint("window", "height")/config.getint("world", "height")

class Actor(cocos.sprite.Sprite):
    palette = {}
    def __init__(self, cx, cy, w, h, img, vel=None):
        super(Actor, self).__init__(img)
        
    
class MessageLayer( cocos.layer.Layer ):
    """Transitory messages over worldview

    
    Full display cycle for transitory messages, with effects and
    optional callback after hiding the message.
    """

    def show_message( self, msg, callback=None ):
        w,h = director.get_window_size()

        self.msg = cocos.text.Label( msg,
            font_size=FONT_SIZE,
            font_name=FONT_NAME,
            anchor_y='center',
            anchor_x='center' )
        self.msg.position=(w/2.0, h)

        self.add( self.msg )

        actions = (
            cocos.actions.Show() + cocos.actions.Accelerate(
                cocos.actions.MoveBy( (0,-h/2.0), duration=0.5)) + 
            cocos.actions.Delay(1) +  
            cocos.actions.Accelerate(cocos.actions.MoveBy( (0,-h/2.0), duration=0.5)) + 
            cocos.actions.Hide()
            )

        if callback:
            actions += cocos.actions.CallFunc( callback )

        self.msg.do( actions )



class IceBlocks(cocos.layer.ColorLayer):
    is_event_handler = True
    def __init__(self):
        self.keys_pressed = {}
        super(IceBlocks, self).__init__(64, 64, 224, 255)
        label = cocos.text.Label(PROGRAM_NAME,
                                 font_name=FONT_NAME,
                                 font_size=FONT_SIZE,
                                 anchor_x='center',
                                 anchor_y='center')
        label.position = WINDOW_W / 2, WINDOW_H / 2
        self.add(label)

        self.sprite = cocos.sprite.Sprite('peddle.png')
        self.sprite.position =  WINDOW_W / 2, WINDOW_H / self.sprite.height
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
        move = MoveBy((80, 0), duration=0.2)
        self.sprite.do(move)

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
