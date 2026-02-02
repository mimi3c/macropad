import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.OLED import OLED
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()
macros = Macros()
oled = OLED(
    oled_addr = 0x3C,
    to_display="",
    i2c_sda = board.GP5,
    i2c_scl= board.GP6,
)
rgb = RGB(pixel_pin=board.GP29, num_pixels=2)

keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(macros)
keyboard.extensions.append(oled)
keyboard.extensions.append(rgb)


PINS = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4]

keyboard.matrix = KeysScanner(
    pins = PINS,
    value_when_pressed = False,
)

keyboard.keymap = [
    [
    KC.RGB_TOG
    KC.VOLU,
    KC.MUTE,
    KC.MEDIA_NEXT_TRACK,
    KC.VOLD
    ]
]

if __name__=="__main__":
    keyboard.go()