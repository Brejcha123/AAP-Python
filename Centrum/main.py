from evidence import PridatZvire, VypsatZvirata

akce = input("Zadejte co chcete udělat")

if akce == "Přidat zvíře":
    PridatZvire(input("Zadejte název zvířete"))

elif akce == "Vypsat zvířata":
    VypsatZvirata()