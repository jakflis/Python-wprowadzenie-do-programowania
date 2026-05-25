# Sprawdzam dzialanie programu z potencjometrem

adc_min = 336 # minimalny zakres z zadania
adc_max = 65535 # maksymalny zakres z zadania

przykladowy_adc = [100, 336, 1000, 50000, 65535, 80000]

def test(lista_adc):
    licznik_diod = [0, 0, 0, 0]
    
    for adc in lista_adc:
        print(f"\nTest dla wartosci: {adc}: ")
        
        if adc_max == adc_min:
            print(f"Zakres potencjometru wynosi zero.")
            return
        
        if adc < adc_min or adc > adc_max:
            print(f"Wartość {adc} jest poza zakresem.")
            continue
            
        pot_norm = (adc - adc_min) / (adc_max - adc_min)
        led_pos = 3 - int(pot_norm * 3)
        
        if led_pos < 0 or led_pos > 3:
            print(f"Dioda numer {led_pos} jest poza zakresem.")
            continue
        else:
            print(f"Test wykonany poprawnie. Dioda: {led_pos}.")
            licznik_diod[led_pos] += 1
            
        
    print(f"\n\n STATYSTYKI ")
    for i in range(4):
        print(f"Dioda nr {i} zapaliła się: {licznik_diod[i]} razy.")
        
        
            
test(przykladowy_adc)