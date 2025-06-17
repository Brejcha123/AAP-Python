dohromady = 0
dohromadyG = 0
while True:
    VahaKocky = float(input("Zadej váhu kočky v kg: "))
    dohromady = VahaKocky + dohromady

    Gram = VahaKocky * 30 + 70
    dohromadyG = dohromadyG + Gram
    print(f"Kočka váží {VahaKocky} a měla by dostat {Gram} gramů krmení denně")

  
    odpoved = input("Chceš zadat další kočku? (ano/ne)")
    if odpoved == "ano":
        continue
    else:
        break


print(f"Celková krmená dávka pro všechny kočky je: {dohromadyG} gramů")