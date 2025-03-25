cislo1 = int(input("Zadej první číslo"))
cislo2 = int(input("Zadej druhé číslo"))

opakovat = "ano"
while opakovat == "ano":
    operace = input("Jakou operci chcete udělat?")

    if operace == "sčítání":
        vysledek = cislo1 + cislo2
        print(vysledek)

    elif operace == "odčítání":
        vysledek = cislo1 - cislo2
        print(vysledek)

    elif operace == "násobení":
        vysledek = cislo1 * cislo2
        print(vysledek)

    elif operace == "dělení":
        vysledek = cislo1 / cislo2
        print(vysledek)

    else:
        print("Tahle možnost neexistuje")

    opakovat = input("Chceš program opakovat?")    