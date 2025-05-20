#Úkol 1
def soucet():
    a = 10
    b = 15
    print(a + b)

soucet()

#Úkol 2

def pozdrav():
    jmeno = input("Zadej jméno")
    print("Ahoj", jmeno)

pozdrav()

#Úkol 3
def PrumerZnamek():
    znamky = [1,5,3,1,2,2,5,4]
    SoucetZnamek = sum(znamky)
    pocet = len(znamky)

    prumer = SoucetZnamek / pocet

    print(prumer)
    
PrumerZnamek()

#Úkol 4
print("ahoj")
def ahoj():
    for i in range(5):
        print("ahoj")

ahoj()

#Úkol BONUS
def bonus():
    pole = []
    
    pole.append("pes")
    pole.append("kočka")
    pole.append("křeček")

    print(pole)

    velikost = len(pole)
    print(velikost)

bonus()