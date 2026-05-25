# Rozbudowa programu: wlaczanie i wylaczanie trybu pulsowania diody nr 0
# przyciskiem nr 1 (z zabezpieczeniem jak poprzednio)

from time import sleep
from peripherals_credit import LedSet, LedClr, ButRead

print ("Jakub Flis, grupa 4, 21.01.2026")

licznik_punktu=0
poprzedni_stan5 = 0
stan_diody5 = False

poprzedni_stan6 = 0
tryb_pulsowania = False 
stan_migania = False    
zegar_migania = 0
    
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
    global poprzedni_stan5, stan_diody5
    przycisk = ButRead(nr)
    
    if przycisk == 1 and poprzedni_stan5 == 0 and not tryb_pulsowania:
        stan_diody5 = not stan_diody5
            
        if stan_diody5:
            LedSet(0)
        else:
            LedClr(0)
            
    poprzedni_stan5 = przycisk
    

def zadanie6(nr):
    global poprzedni_stan6, tryb_pulsowania, zegar_migania, stan_migania, stan_diody0
    przycisk = ButRead(nr)
    
    if przycisk == 1 and poprzedni_stan6 == 0:
        tryb_pulsowania = not tryb_pulsowania
        
        if not tryb_pulsowania:
            LedClr(0)
            stan_diody5 = False
            
    poprzedni_stan6 = przycisk
    
    if tryb_pulsowania:
        zegar_migania +=1
        if zegar_migania >= 100:
            zegar_migania = 0
            stan_migania = not stan_migania
            
            if stan_migania:
                LedSet(0)
            else:
                LedClr(0)
    else:
        stan_migania = False
        zegar_migania = 0 

while True:
    
    sleep(0.001)
    
    if zadanie2(3):
        break
    
    zadanie3(licznik_punktu)
    
    licznik_punktu += 1
    if licznik_punktu == 4000:
        licznik_punktu=0
        
    zadanie5(0)
    zadanie6(1)