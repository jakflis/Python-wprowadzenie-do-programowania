from machine import Pin
from peripherals import PotRead
from my_peri import DetRead, LedPoint
from time import sleep

# kalibracja
i=0
while(True):
    LedPoint(i)
    i = (i - 1) % 4
    if DetRead() == 0:
        break
    sleep(1/50)
# pozycjonowanie
curr_pos = 0
while(True):
    des_pos = 48-int((PotRead()/65535)*48)
    if des_pos < curr_pos:
        curr_pos = curr_pos - 1
    elif des_pos > curr_pos:
        curr_pos = curr_pos + 1
    LedPoint(curr_pos % 4)
    sleep(1/50)