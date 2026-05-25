# Program naprzemiennie zapalajacy i gaszacy
# diode nr 0 co 0,1 sekundy

from time import sleep
from peripherals_credit import LedSet, LedClr

print ("Jakub Flis, grupa 4, 21.01.2026")

licznik = 0
def zadanie1(nr):
    global licznik
    if licznik == 0:
        LedSet(nr)
    if licznik == 100:
        LedClr(nr)
    
while True:
    sleep(0.001)
    
    zadanie1(0)
    licznik += 1
    
    if licznik >= 200:
        licznik = 0
    