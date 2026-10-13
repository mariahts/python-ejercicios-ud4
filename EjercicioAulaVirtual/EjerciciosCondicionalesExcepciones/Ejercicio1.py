#EJERCICIO

### Ejercicio 1: Verificación de edad

try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        print("Error: La edad debe ser un número entero positivo.")
    elif edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")
except ValueError:
    print("Error: Debes introducir un número entero válido.")





### Ejercicio 2: Comparación de dos números


try:
    num1 = int(input("Introduce el primer número entero: "))
    num2 = int(input("Introduce el segundo número entero: "))

    if num1 > num2:
        print(f"El número mayor es {num1} y el menor es {num2}.")
    elif num2 > num1:
        print(f"El número mayor es {num2} y el menor es {num1}.")
    else:
        print("Ambos números son iguales.")
except ValueError:
    print("Error: Debes introducir números enteros válidos.")





### Ejercicio 3: Validación de nota


try:
    nota = float(input("Introduce una nota numérica entre 0 y 10: "))

    if nota < 0 or nota > 10:
        print("Error: La nota debe estar en el rango de 0 a 10.")
    elif nota < 5.0:
        print("Suspenso")
    elif nota < 7.0:
        print("Aprobado")
    elif nota < 9.0:
        print("Notable")
    else:
        print("Sobresaliente")
except ValueError:
    print("Error: Debes introducir un número decimal válido.")




### Ejercicio 4: Acceso con clave

# Para la clave no se requiere conversión de tipo (las entradas siempre son str),
# pero se incluye el bloque try-except por consistencia con los requisitos.
try:
    clave_correcta = "python123"
    clave_usuario = input("Introduce la clave de acceso: ")

    if clave_usuario == clave_correcta:
        print("Acceso concedido.")
    else:
        print("Acceso denegado.")
except Exception as e:
    print(f"Error inesperado al procesar la entrada: {e}")


### Ejercicio 5: Menú de selección

print("--- MENÚ ---")
print("1. Ver perfil")
print("2. Editar perfil")
print("3. Salir")

try:
    opcion = int(input("Selecciona el número de una opción (1-3): "))

    if opcion == 1:
        print("Has seleccionado: Ver perfil")
    elif opcion == 2:
        print("Has seleccionado: Editar perfil")
    elif opcion == 3:
        print("Saliendo del programa...")
    else:
        print("Error: Opción fuera de rango. Debes elegir 1, 2 o 3.")
except ValueError:
    print("Error: Debes introducir un número entero válido.")



### Ejercicio 6: Validación de número par o impar


try:
    numero = int(input("Introduce un número entero: "))

    if numero % 2 == 0:
        print(f"El número {numero} es PAR.")
    else:
        print(f"El número {numero} es IMPAR.")
except ValueError:
    print("Error: Debes introducir un número entero válido.")

### Ejercicio 7: Verificación de permisos para conducir según edad


#EXCEPCION PROPIA





