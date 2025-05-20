kolikrat = int(input("Zadej kolik chceš zadat zvířat"))

seznam = []

for i in range(kolikrat):
    seznam.append(input("Zadej postupně zvířata: "))


if "tapír" in seznam:
    print("Super")

elif "mýval" in seznam:
    print("Super")

elif "kočka" in seznam:
    print("Super")

else:
    print("Nic moc")