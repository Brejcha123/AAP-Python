#2ukol
jidlo = ["kiwi", "hruška", "jablko"]

print(jidlo[0])
print(jidlo[1])
print(jidlo[2])

#3ukol
znamky = [1,5,5,2,3,1]

print(znamky)

#4ukol
zvirata = ["pes", "kočka", "kůň", "křeček"]

print(zvirata[1])
print(zvirata[3])

#5ukol
seznam = []

for i in range (3):
    seznam.append(int(input("Zadej postupně 3 čísla:")))

print(seznam)

#6ukol
filmy = ["Walking dead", "The last of us", "Joker"]

for polozka in filmy:
    print(polozka)

#7ukol
SeznamCisel = [1,5,3]
SeznamCisel[1] = 999

print(SeznamCisel)

#8ukol
cisla = [5,2,3,4,5]
soucet = sum(cisla)
print(soucet)

#9ukol
pole = [1,5,3,4,8]
velikost = len(pole)
print(velikost)

#10ukol
PoleZnamky = [1,3,4,1,5]
SoucetZnamky = sum(PoleZnamky)
VelikostZnamky = len(PoleZnamky)

AritmetickyPrumer = SoucetZnamky / VelikostZnamky
print(AritmetickyPrumer)

#11ukol
ovoce = ["Jablko", "Banán", "Hruška"]

hledane = "x"

for i in ovoce:
    if i == "Banán":
        print("Je tam banán")


#12ukol
Cisla1 = [1,5,6,2,8,10,15,81]
hodnoty = 0

for x in Cisla1:
    if x >= 10:
        hodnoty = hodnoty + 1

print(hodnoty)

#13ukol

TabulkaZnamek = []
PocetZnamek = int(input("Kolik známek chceš přidat?"))

for i in range(PocetZnamek):
    NovaZnamka = int(input("Zadej známku:"))
    TabulkaZnamek.append(NovaZnamka)

SoucetCisel = sum(TabulkaZnamek)
PoleDelka = len(TabulkaZnamek)

prumer = SoucetCisel / PoleDelka

print("Průměr je:", prumer)