from utulek import pridej_zvire

nazev = input("Zadej název budovy, kterou chcete spravovat")

if nazev == "Nemocnice":
    print("Spravujete Nemocnici")

elif nazev == "Útulek":
    print("Spravujete Útulek")
    NazevZvirete = input("Zadej název zvířete, které chcete přidat")
    pridej_zvire(NazevZvirete)

elif nazev == "Radnice":
    print("Spravujete Radnici")

else:
    print("Takovou budovu nevlastníme, sorry")