# EJERCICIO 1
try:
    horas = float(input("Enter Hours: "))
except:
    print("Introduzca un numero valido")
try:
    tarifa = float(input("Enter Rate: "))
except:
    print("Introduzca un numero validos")

if horas <= 40:
    pago = horas * tarifa
else:
    pago = (40 * tarifa) + ((horas - 40) * tarifa * 1.5)

print("Pay:", pago)


