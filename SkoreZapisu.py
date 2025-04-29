hodnoty = [10, 5, 50, 55, 15, 8, 14, 35, 42, 58]

print("Celkové skore je:", sum(hodnoty))
print("Nejnižší skore je:", min(hodnoty))
print("Nejvyšší skore je:", max(hodnoty))
print("Průměrné skore je:", sum(hodnoty) / len(hodnoty))

VicNez50 = sum(1 for s in hodnoty if s >50)

if VicNez50 >5:
    print("Výborný výkon!")

else:
    print("Můžete to příště zkusit lépe.")