import random
def adivina_el_numero():
    numero =  random.randint(1, 100)
    intentos = 0
    adivinado = False
    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinarlo?")
    while not adivinado:
        try:
            adivinanza = int(input("Introduce tu adivinanza: "))
            intentos += 1
            if adivinanza < numero:
                print("Demasiado bajo. Intenta de nuevo.")
            elif adivinanza > numero:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                adivinado = True
                print(f"¡Felicidades! Has adivinado el número {numero} en {intentos} intentos.")
        except ValueError:
            print("Por favor, introduce un número válido.")

adivina_el_numero()
##estoy añadiendo desde git hub
