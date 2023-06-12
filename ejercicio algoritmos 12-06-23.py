def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def calcular_factorial(numero):
    factorial = 1
    for i in range(2, numero + 1):
        factorial *= i
    return factorial

def es_palindrome(frase):
    frase = frase.lower().replace(" ", "")
    return frase == frase[::-1]

# Función principal del programa
def menu():
    opcion = 0
    while opcion != 4:
        print("----- MENU -----")
        print("1. Número Primo")
        print("2. Factorial")
        print("3. Palindrome")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            numero = int(input("Ingrese un número entre 1 y 15: "))
            if 1 <= numero <= 15:
                if es_primo(numero):
                    print("El número", numero, "es primo.")
                else:
                    print("El número", numero, "no es primo.")
            else:
                print("Número inválido.")
        
        elif opcion == 2:
            numero = int(input("Ingrese un número entre 3 y 10: "))
            if 3 <= numero <= 10:
                factorial = calcular_factorial(numero)
                print("El factorial de", numero, "es:", factorial)
            else:
                print("Número inválido.")
        
        elif opcion == 3:
            frase = input("Ingrese una frase: ")
            if es_palindrome(frase):
                print("La frase es un palíndromo.")
            else:
                print("La frase no es un palíndromo.")
        
        elif opcion == 4:
            print("Gracias por usar el programa. Autor: Dante Carreño.")
        
        else:
            print("Opción inválida. Intente nuevamente.")

# Llamada a la función principal del programa
menu()