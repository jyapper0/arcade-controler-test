#module about keyboard and key-matrix handling
from adafruit_hid.keyboard import Keyboard
from const import DEFAULT_CODE_MAP, DEFAULT_IN_PINS, DEFAULT_OUT_PINS
import usb_hid, time
import digitalio


class Controler:
  def __init__(self, codeMap=DEFAULT_CODE_MAP, inPinMap=DEFAULT_IN_PINS, outPinMap=DEFAULT_OUT_PINS) -> None:
    self.codeMap = codeMap
    self.inPins  = inPinMap
    self.outPins = outPinMap
    self.keyboard = Keyboard(usb_hid.devices)
    
    #valuable to decide pressing/releasing keys.
    self.state = [[False for j in row]for row in self.codeMap]
    
    #initializing gpio pins I/O and output value
    for pin_out in self.outPins:
      pin_out.direction = digitalio.Direction.OUTPUT
      pin_out.value = False
      
    for pin_in in self.inPins:
        pin_in.direction = digitalio.Direction.INPUT
      
  #report : when it's set True, display how long use to scan key-matrix
  def loop(self, report=False):
    if(report):
      start_time=time.monotonic_ns()
    for i, pin_out in enumerate(self.outPins):
        #turn scan-row ON
        pin_out.value = True
        #wait for 10μs
        time.sleep(0.000001)
        #行内のボタンを判定
        for j,pin_in in enumerate(self.inPins):
            #button is pressed & button wasn't pressed on previous cycle
            if pin_in.value == 1:
                if self.state[j][i] == False:
                    self.keyboard.press(self.codeMap[j][i])
                    self.state[j][i] = True
            #button isn't pressed & button was pressed on previous cycle   
            elif self.state[j][i]:
                self.keyboard.release(self.codeMap[j][i])
                self.state[j][i] = False
        
        #turn scan-row OFF
        pin_out.value = False
        #wait for 10μs
        time.sleep(0.000001)
    if(report):
      print(f'\r{(time.monotonic_ns()-start_time)/1000000:} [ms]', end="")

