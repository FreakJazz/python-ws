# Clase 1 – Fundamentos de Python

## 🎯 Objetivo:
Aplicar estructuras básicas de programación en Python: variables, condicionales, bucles y funciones.

---

## 📋 Instrucciones:

1. Crea un archivo con tu nombre en la carpeta 'clase_1'. Ejemplo: 'nombre_apellido.py'.
2. Resuelve los ejercicios propuestos a continuación.
3. Guarda tus cambios, haz 'commit' y 'push'.
4. Crea un Pull Request a este repositorio con el título:  
   '"Clase 1 - TuNombre TuApellido"'

---

## 🧪 Ejercicio 1: Calculadora de IMC (Índice de Masa Corporal)

### 📌 Requisitos:
- Solicita al usuario su:
  - Nombre
  - Edad
  - Talla (en metros)
  - Peso (en kilogramos)
- Calcula el IMC con la fórmula:  
  \[
  IMC = \frac{peso}{talla^2}
  \]
- Muestra el resultado con 2 decimales.
- Dependiendo del valor, muestra un mensaje personalizado:
  - Menor a 18.5: Bajo peso
  - Entre 18.5 y 24.9: Peso saludable
  - Entre 25.0 y 29.9: Sobrepeso
  - Mayor o igual a 30.0: Obesidad

### ✅ Salida esperada:

Nombre: 
Edad: 24
Talla (m): 1.60
Peso (kg): 55

Hola ________, tu IMC es 21.48.
Tienes un peso saludable.


## 🔢 Ejercicio 2: Números pares en un intervalo

### 📌 Requisitos:
- Solicita dos números enteros: uno menor y uno mayor.
- Valida que el primer número sea menor que el segundo.
- Validar que sean números enteros positivos.
- Muestra:
  - Todos los números pares en ese rango (inclusive)
  - La cantidad total de números en ese rango

### ✅ Salida esperada:

Ingresa el número menor: 4
Ingresa el número mayor: 14

Números pares entre 4 y 14:
4, 6, 8, 10, 12, 14

Cantidad total de números en el intervalo: 11

## ⭐ Recomendaciones:
- Utiliza funciones para cada ejercicio.
- Escribe comentarios en el código explicando cada parte.
- Usa f-strings para los mensajes (por ejemplo: 'f"Hola {nombre}"').
