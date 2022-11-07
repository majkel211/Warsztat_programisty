def silnia(n):
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik