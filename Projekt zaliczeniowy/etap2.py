# Rozbudowa programu: nacisniecie przycisku nr 3
# konczy dzialanie programu

from time import sleep
from peripherals_credit import LedSet, LedClr, ButRead

print ("Jakub Flis, grupa 4, 21.01.2026")

licznik = 0
def zadanie1(nr):
    global licznik
    if licznik == 0:
        LedSet(nr)
    if licznik == 100:
        LedClr(nr)
    
def zadanie2(nr):
    przycisk = ButRead(nr)
    if przycisk == 1:
        LedClr(0)
        LedClr(1)
        LedClr(2)
        LedClr(3)
        return True
    return False
        
while True:
    
    sleep(0.001)
    
    licznik += 1
    if licznik >= 200:
        licznik = 0
        
    zadanie1(0)
    if zadanie2(3):
        break
