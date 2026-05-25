# Modyfikacja programu umozliwiajaca wlaczanie/wylaczanie diody 0
# pojedynczym nacisnieciem przycisku 0, niezaklocajac punktu swietlnego
# z zabezpieczeniem gdy przycisk jest trzymany na dluzej w tym stanie,
# to dioda 0 nie zmienia swojego stanu

from time import sleep
from peripherals_credit import LedSet, LedClr, ButRead

print ("Jakub Flis, grupa 4, 21.01.2026")

licznik_punktu=0
poprzedni_stan = 0
stan_diody = False
    
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
    
def zadanie5(nr):
    global poprzedni_stan, stan_diody
    przycisk = ButRead(nr)
    
    if przycisk == 1 and poprzedni_stan == 0:
        if stan_diody:
            LedClr(0)
            stan_diody = False
        else:
            LedSet(0)
            stan_diody = True
            
    poprzedni_stan = przycisk
    
while True:
    
    sleep(0.001)
        
    if zadanie2(3):
        break
    
    zadanie3(licznik_punktu)
    
    licznik_punktu += 1 
    if licznik_punktu == 4000:
        licznik_punktu=0
        
    zadanie5(0)