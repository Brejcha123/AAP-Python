#uživatel tohoto programu je doktor, který chce přidávat pacienty do svojí databáze
#uprav kód pomocí cyklu tak, aby se program nejdřív zeptal uživatele kolik pacientů chce přidat a podle toho pak proběhl kód níže


cislo = int(input("Zadej kolikrát cheš opakovat"))

for i in range (1, cislo+1, 1):
    #tento kousek kódu se bude opakovat tolikrát kolikrát zadá uživatel
    jmeno = input("Zadejte jméno pacienta, kterého chcete přidat")
    prijmeni = input("Zadejte příjmení pacienta, kterého chcete přidat")
    rok = int(input("Zadejte rok narození pacienta ktetého chcete přidat"))
    print(f"Pacient {jmeno} {prijmeni} rok narození {rok} byl přidán")