nabidka = int(input("Vyber si jednu z možností: 1. poudrav, 2. dnešní den, 3. čísla 1 až 5, 4. obdélník z hvězdiček, 5. nálada dne, 6. konec, Zadej číslo: "))

def pozdrav():
    print("Ahoj, jak se máš?")

def DnesniDen():
    print("Dneska je úterý")

def VypisCisel():
    for i in range(1,6):
        print(i)

def Obdelnik():
    for obd in range(3):
        print("*****")

def NaladaDne():
    nalada = ["smutná", "veselá"]
    VybranaNalada =
    print("Dnešní nálada je:", VybranaNalada)

def Konec():
    print("Konec programu")

if nabidka == 1:
    pozdrav()

elif nabidka == 2:
    DnesniDen()

elif nabidka == 3:
    VypisCisel()

elif nabidka == 4:
    Obdelnik()

elif nabidka == 5:
    NaladaDne()

elif nabidka == 6:
    Konec()