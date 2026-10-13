

class excepcionPropia (Exception):
    pass


try:
    edad = int(input("Introduce tu edad: "))

    if edad < 0:
        print("Error: La edad no puede ser negativa.")
        raise excepcionPropia
    elif edad < 14:
        print("No puedes conducir ningún vehículo.")
    elif edad < 16:
        print("Puedes conducir: Moto de poca cilindrada.")
    elif edad < 18:
        print("Puedes conducir: Moto de poca cilindrada y moto de gran cilindrada.")
    else:
        print("Puedes conducir: Coche, moto de gran cilindrada y moto de poca cilindrada.")
except ValueError:
    print("Error: Debes introducir un número entero válido.")

except excepcionPropia:
    print("Introduce  un numero entero valido.")