# Programa 11: el juego piedra papel o tijera pero en Python XD

#Librerias
import random
import math

#------
# input
#------

print(" ")
print("      PIEDRA  PAPEL  O  TIJERA      ")
print(" ")
print("  1 = Piedra  2 = Papel  3 = tijera  ")
print(" ")

computer_number = random.randint(1,3)

user_number = int(input("¿Qué escoges?: "))

#----------
#processing
#----------

if(computer_number == user_number):
    print(" ")
    print("empate")
elif((user_number == 3 and computer_number == 2)or(user_number == 1 and computer_number == 3)or(user_number == 2 and computer_number == 1)):
    print(" ")
    print("ganaste")
else:
    print(" ")
    print("la computadora gana")


#-----
#output
#-----

print(" ")
print("la computadora eligio: " +str(computer_number))
print(" ")