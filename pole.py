OvoceZelenina = ["citron", "jablko", "hruška", "broskev", "třešně", "malina"]

print("Délka pole je: "), print(len(OvoceZelenina))

print("Výpis všech hodnot: ")
for vypis in OvoceZelenina:
    print(vypis)

DalsiHodnota = input("Zadejte další věc ")
OvoceZelenina.append(DalsiHodnota)

OvoceZelenina.pop(1)

OvoceZelenina.sort()
print(OvoceZelenina)

OvoceZelenina.reverse()
print(OvoceZelenina)