

puntuacion = float(input("Introduzca una opcion entra 0.0 y 1.0 "))


if puntuacion <= 0.0 or puntuacion > 1.0:
    print("INTRODUZCA UN NUMERO VALIDO")
elif puntuacion >= 0.9:
    print("GRADE A")
elif puntuacion >= 0.8:
    print("GRADE B")
elif puntuacion >= 0.7:
    print("GRADE C")
elif puntuacion >= 0.6:
    print("GRADE D")
elif puntuacion < 0.6:
    print("GRADE F")
