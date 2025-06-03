#Úkol 1

import random

def HadaniCisla(TajneCislo):
   
    while True:

        HadaniCisla = int(input("Zadej číslo: "))

        if TajneCislo > HadaniCisla:
            print("Hledané číslo je vyšší")

        elif TajneCislo < HadaniCisla:
            print("Hledané číslo je nižší")
    
        else:
            print("Správně!")
            break

TajneCislo = random.randint(1,100)
HadaniCisla(TajneCislo)



#Úkol 2

