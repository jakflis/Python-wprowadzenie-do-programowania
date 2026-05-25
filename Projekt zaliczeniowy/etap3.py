#Rozbudowa programu: przesuwajacy sie punkt
# swietlny  na diodach 1,2,3 niezaklocajacy pulsowania diody 0

from time import sleep
from peripherals_credit import LedSet, LedClr, ButRead

print ("Jakub Flis, grupa 4, 21.01.2026")

licznik = 0
licznik_punktu=0

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
    
def zadanie3(nr):
    if nr == 0:
        LedSet(1)
    elif nr == 1000:
        LedClr(1)
        LedSet(2)
    elif nr == 2000:
        LedClr(2)
        LedSet(3)
    elif nr == 3000:
        LedClr(3)
    

while True:
    
    sleep(0.001)
    
    licznik += 1
    if licznik >= 200:
        licznik = 0
    zadanie1(0)
    
    if zadanie2(3):
        break
    
    zadanie3(licznik_punktu)
    
    licznik_punktu += 1
    if licznik_punktu == 4000:
        licznik_punktu=0
    
