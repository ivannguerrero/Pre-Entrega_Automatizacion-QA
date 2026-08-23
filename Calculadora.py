def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


try:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")

    opcion = input("Seleccione una operación: ")

    if opcion == "1":
        resultado = sumar(numero1, numero2)
    elif opcion == "2":
        resultado = restar(numero1, numero2)
    elif opcion == "3":
        resultado = multiplicar(numero1, numero2)
    elif opcion == "4":
        resultado = dividir(numero1, numero2)
    else:
        print("Opción inválida.")
        resultado = None

    if resultado is not None:
        print("Resultado:", resultado)

except ValueError:
    print("Error: debe ingresar un número válido.")

except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")