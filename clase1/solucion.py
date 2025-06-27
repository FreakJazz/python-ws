# clase_1

def calcular_imc(peso, talla):
    return peso / (talla ** 2)

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso saludable"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def ejercicio_1():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    talla = float(input("Talla (m): "))
    peso = float(input("Peso (kg): "))

    imc = calcular_imc(peso, talla)
    estado = clasificar_imc(imc)

    print(f"\nHola {nombre}, tu IMC es {imc:.2f}.")
    print(f"Estado: {estado}")

def ejercicio_2():
    menor = int(input("Ingresa el número menor: "))
    mayor = int(input("Ingresa el número mayor: "))

    if menor >= mayor:
        print("Error: el primer número debe ser menor.")
        return

    pares = [i for i in range(menor, mayor + 1) if i % 2 == 0]
    cantidad_total = (mayor - menor) + 1

    print(f"\nNúmeros pares entre {menor} y {mayor}:")
    print(", ".join(map(str, pares)))
    print(f"Cantidad total de números en el intervalo: {cantidad_total}")

# Ejecutar programa
if __name__ == "__main__":
    ejercicio_1()
    print("\n" + "="*40 + "\n")
    ejercicio_2()
