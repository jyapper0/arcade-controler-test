import digitalio, board

inPins = [digitalio.DigitalInOut(i) for i in [board.GP17, board.GP18, board.GP19, board.GP16]]
outPins =  [digitalio.DigitalInOut(i) for i in [board.GP0, board.GP1, board.GP2, board.GP3]]
