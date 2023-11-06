import controler

device = controler.Controler()

while(True):
    device.loop(report=True)