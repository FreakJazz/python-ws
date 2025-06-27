# EJERCICIO 1

def person():
    name = input("Nombre: ")
    edad = input("Edad: ")
    talla = input("Talla (en metros): ")
    peso = input("Peso (en kilogramos): ")
    return name, edad, talla, peso
    
def calcular_imc(peso, talla):
    peso = float(peso)
    talla = float(talla)
    return peso/(talla**2)

def clasificar_imc(imc):
    if (imc < 18.5): 
        mensaje = "Bajo peso"
    elif (imc < 25):
        mensaje = "Peso saludable"
    elif (imc < 30):
        mensaje = "Sobrepeso"    
    else:
        mensaje = "Obesidad"
    return mensaje

def ejercicio1(peso, talla):
    imc = calcular_imc(peso, talla)
    mensaje = clasificar_imc(imc)
    return mensaje

def ejercicio2(num1, num2):
    pares = None
    cantidad_total = 0
    if (num1 > num2):
        msn = f"Error el número {num1} es mayor a {num2}"
    if (num1 < 0 or num2 < 0):

        msn = f"Error el número {num1} o {num2} es negativo, o ambos"
    else:
        pares = [i for i in range(num1, num2+1) if i % 2 == 0]
        cantidad_total = len(pares)
        msn = f"Los números pares entre {num1} y el {num2} son: {cantidad_total}, {pares}"
        
    return msn
            
        

if __name__ == "__main__":
    # name, edad, talla, peso = person()
    
    # msn = ejercicio1(peso, talla)

    # print(f"Hola {name} tienes {edad} años y estas en: {msn}")
    num1 = input("ingrese el primer número: ")
    num2 = input("ingrese el segundo número: ")
    
    msn = ejercicio2(int(num1), int(num2))
    print(msn)