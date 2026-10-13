class excepcionPropia(Exception):
    pass



numero = int(input("Introduce un numero: "))


try:
    if numero<=0:

        raise excepcionPropia
    print("Introduzca un numero entero valido.")

except ValueError:
    print("Introduzca un numero entero valido.")

except excepcionPropia:
    print("Introduzca un numero entero valido.")










