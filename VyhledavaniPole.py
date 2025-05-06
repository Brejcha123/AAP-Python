cisla = []

kolikrat = int(input("Kolik čísel chcete přidat?"))
for i in range(1, kolikrat + 1, 1):
    cisla.append(int(input("Zadej číslo: ")))

hledane = int(input("Jaké číslo chce najít?"))

if hledane in cisla:
    print("Číslo: ", hledane ," se nachází v poli")

else:
    print("Číslo: ", hledane ," se v poli nenachází")