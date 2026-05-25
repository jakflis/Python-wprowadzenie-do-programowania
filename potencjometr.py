from peripherals import PotRead
from my_peri import LedPoint
from time import sleep

adc_min=336 
adc_max=65535

while(True):
    adc=PotRead()
    pot_norm=(adc-adc_min)/(adc_max-adc_min)
    led_pos=3-int(pot_norm*3)
    LedPoint(led_pos)