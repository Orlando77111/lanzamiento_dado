# Programa para simular el lanzamiento de un dado

import random

print("----------------------------------")
print("------LANZAMIENTO DE UN DADO------")
print("----------------------------------")

# Input

# processing

d1 = random.randint(1,6)
# d2 = random.randint(1,6)

d2 = int(input("Digite un numero "))

if (d1==1):
    rta = "UNO"
elif (d1==2):
    rta = "DOS"
elif (d1==3):
    rta = "TRES"
elif (d1==4):
    rta = "CUATRO"
elif (d1==5):
    rta = "CINCO"
elif (d1==6):
    rta = "SEIS"
else:
    print("No es la cara de un dado ")

if (d1==d2):
    rta = "ADIVINASTE EL NUMERO"
else:
    rta = "I AM SORRY.... NO ADIVINADTE"

# ouput
print(rta)
print("Dado 1 " + str(d1))
print("Usted digito " + str(d2))