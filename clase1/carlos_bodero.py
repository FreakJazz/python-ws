#Ejercicio 1
def ejercicio1():
    nombre = input("Nombre: ")
    edad = input("Edad ")
    peso = float(input("peso (kg): "))
    talla = float(input("talla (m): "))
    imc = peso / (talla*talla)
    print(f"Hola {nombre} tienes {edad} años y tu imc es {round(imc,2)} estas en")
    if imc < 18.5:
        print("Bajo peso")
    elif imc >= 18.5 and imc <24.9:
        print("Peso saludable")
    elif imc >= 25.0 and 29.9:
        print("sobrepeso")
    else:
        print("obesidad")

def ejercicio2():
    Numero_menor = int(input("Ingresa el número menor:"))
    Numero_mayor = int(input("Ingresa el número mayor:"))
    if Numero_menor < 0 or Numero_mayor < 0:
        print("Ingrese Número entero positivo ")
    elif Numero_menor > Numero_mayor:
        print()
    else:
        numeros = range(Numero_menor,Numero_mayor + 1)
        cuenta_pares = 0
        cuenta_numeros = 0
        salida_numeros = ""
        for iterador in numeros:
            #print(iterador)
            cuenta_numeros = cuenta_numeros + 1
            if iterador % 2 == 0:
                cuenta_pares = cuenta_pares + 1
                salida_numeros = salida_numeros + str(iterador) + ", "
        print(f"Números pares entre {Numero_menor} y {Numero_mayor} :{cuenta_pares}")
        print(f"{salida_numeros}")
        print(f"Cantidad total de números en el intervalo: {cuenta_numeros}")
   
if __name__ == "__main__":
    ejercicio1()
    ejercicio2()

