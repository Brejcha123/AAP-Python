znamky = [1,5,3,1,4]

delka = (len(znamky))

soucet = sum(znamky)

prumer = soucet / delka
print("Průměr všech známek je: ",prumer)

print("Výpis všech známek: ")
for vypis in znamky:
    print(vypis)
