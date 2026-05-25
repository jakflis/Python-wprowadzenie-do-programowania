# Sprawdzam dzialanie programu z klawiatura

def test1(stan_przyciskow):
    for i in range(4):
        if stan_przyciskow[i] == 1:
            return i
    return None

przyklad1 = test1([0, 0, 0, 0])
print(f"Dla przykladu 1: {przyklad1}")

przyklad2 = test1([0, 0, 1, 0])
print(f"Dla przykladu 2: {przyklad2}")

przyklad3 = test1([0, 1, 0, 1])
print(f"Dla przykladu 3: {przyklad3}")
