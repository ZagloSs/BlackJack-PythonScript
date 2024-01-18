import random

class Carta:
    def __init__(self, nombre, palo, valor):
        self.nombre = nombre
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return f"{self.nombre}"


def repartir(who):
    who.append(baraja.pop())


manoJugador = []
valorJugador = 0
planteJugador = False

manoMaquina = []
valorMaquina = 0
planteMaquina = False


#---Creación de la Baraja---
baraja = []
palos = ["bastos", "oros", "copas", "espadas"]
for palo in palos:
    for j in range(1,11):
        if j == 1:
            baraja.append(Carta(f"As de {palo}", palo, 1))
        elif j == 8:
            baraja.append(Carta(f"Sota de {palo}", palo, 10))
        elif j == 9:
            baraja.append(Carta(f"Caballo de {palo}", palo, 10))
        elif j == 10:
            baraja.append(Carta(f"Rey de {palo}", palo, 10))
        else:
            baraja.append(Carta(f"{j} de {palo}", palo, j))
random.shuffle(baraja)
#---Fin de creación de la baraja---



for i in range(2):
    repartir(manoJugador)
    repartir(manoMaquina)

print("Se han repartido las cartas iniciales\nEstas son tus cartas:")
for cartas in manoJugador:
    print(cartas)
    valorJugador += cartas.valor
print(f"El valor de tus cartas es de {valorJugador}")















