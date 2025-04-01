#Brejcha, Cafourek

jidloJedna = str(input("Napište jídlo č. 1: "))
KalorieJedna = int(input("Kolik mělo kalorií: "))
jidloDva = str(input("Napište jídlo č. 2: "))
KalorieDva = int(input("Kolik mělo kalorií: "))
jidloTri = str(input("Napište jídlo č. 3: "))
KalorieTri = int(input("Kolik mělo kalorií: "))

celkove_kalorie = (KalorieJedna + KalorieDva + KalorieTri)


běh = int(input("Jak dlouho jsi běhal?"))
chuze = int(input("Jak dlouho jsi šel?"))

celkovy_vydej = (běh * 5) + (chuze * 5)

print("Celkový počet kalorií je:",celkove_kalorie)
print("Celkem spálené kalorie:", celkovy_vydej) 

if celkove_kalorie < celkovy_vydej:
    print("Máš nedostatek kalorií")

