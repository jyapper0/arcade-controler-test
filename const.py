#module for constant 

import digitalio, board
from adafruit_hid.keyboard import Keycode

DEFAULT_IN_PINS = [digitalio.DigitalInOut(i) for i in [board.GP17, board.GP18, board.GP19, board.GP16]]
DEFAULT_OUT_PINS =  [digitalio.DigitalInOut(i) for i in [board.GP0, board.GP1, board.GP2, board.GP3]]


DEFAULT_CODE_MAP = [
  [Keycode.Y, Keycode.U, Keycode.I, Keycode.O],
  [Keycode.H, Keycode.J, Keycode.K, Keycode.L],
  [Keycode.A, Keycode.S, Keycode.D, Keycode.W],
  [Keycode.ESCAPE, Keycode.F, Keycode.ESCAPE, Keycode.F]
  ]


