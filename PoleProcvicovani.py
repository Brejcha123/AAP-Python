jidlo = ["kiwi", "hruška", "jablko"]

print(jidlo[0])
print(jidlo[1])
print(jidlo[2])


znamky = [1,5,5,2,3,1]

print(znamky)


zvirata = ["pes", "kočka", "kůň", "křeček"]

print(zvirata[1])
print(zvirata[3])


seznam = []

for i in range (3):
    seznam.append(int(input("Zadej postupně 3 čísla:")))

print(seznam)


filmy = ["Walking dead", "The last of us", "Joker"]

for polozka in filmy:
    print(polozka)


SeznamCisel = [1,5,3]
SeznamCisel[1] = 999

print(SeznamCisel)


cisla = [5,2,3,4,5]
soucet = sum(cisla)
print(soucet)


pole = [1,5,3,4,8]
velikost = len(pole)
print(velikost)


PoleZnamky = [1,3,4,1,5]
SoucetZnamky = sum(PoleZnamky)
VelikostZnamky = len(PoleZnamky)

AritmetickyPrumer = SoucetZnamky / VelikostZnamky
print(AritmetickyPrumer)