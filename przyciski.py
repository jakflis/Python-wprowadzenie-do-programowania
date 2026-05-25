from peripherals_credit import ButRead
from my_peri import LedPoint
from time import sleep

def ReadKeyboard():
    for i in range(4):
        if ButRead(i):
            return i
    return None
while(True):
    print(ReadKeyboard())
    sleep(0.2)