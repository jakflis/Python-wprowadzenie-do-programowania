# Sprawdzam dzialanie programu z serwomechanizmem

przykladowy_adc = [100, 16000, 32000, 65535, 80000]

def test1(lista_adc):
    print(f"\nTest 1 sprawdza przelicznik ADC na pozycje docelowa.")
    
    for adc in lista_adc:
        if adc < 336 or adc > 65535:
            print(f"Wartosc {adc} poza zakresem.")
            continue
        des_pos = 48 - int((adc/65535) * 48)
        
        if des_pos < 0 or des_pos > 48:
            print(f" Dla: {adc}, pozycja docelowa: {des_pos} jest poza zakresem.")
        else:
            print(f"Dla: {adc}, pozycja docelowa: {des_pos}")
            
def test2(start_pos, des_pos):
    print(f"\n Test 2 sprawdza algorytm poruszania sie serwomechanizmu.")
    
    curr_pos = start_pos
    kroki = 0
    
    while curr_pos != des_pos and kroki <50:
        if des_pos < curr_pos:
            curr_pos -= 1
        elif des_pos > curr_pos:
            curr_pos += 1
    
        kroki += 1
        dioda = curr_pos % 4
        
    if curr_pos == des_pos:
        print(f" Serwomechanizm wykonał {kroki} kroki.")
    else:
        print(f" Serwomechanizm nie dotarł do celu.")
            
test1(przykladowy_adc)
test2(0,5)
test2(48,45)
    
    
    