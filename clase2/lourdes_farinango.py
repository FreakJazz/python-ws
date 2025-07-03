# -*- coding: utf-8 -*-
"""
Este código implementa un sistema básico de gestión de una tienda utilizando
Programación Orientada a Objetos en Python.
@author: Lourdes Farinango
"""

class Producto:
    """
    Representa un producto con nombre, precio y stock.
    """
    def __init__(self, nombre: str, precio: float, stock: int):
        """
        Inicializa un nuevo producto.

        Args:
            nombre (str): El nombre del producto.
            precio (float): El precio del producto.
            stock (int): La cantidad disponible en inventario.
        """
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        """
        Muestra la información completa del producto.
        """
        print(f"{self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}")

    def actualizar_stock(self, cantidad: int):
        """
        Actualiza el stock del producto.

        Args:
            cantidad (int): La cantidad a sumar (si es positiva) o restar
                            (si es negativa) del stock.
        """
        self.stock += cantidad
        print(f"Stock actualizado:\n{self.nombre} | Stock: {self.stock}")


    def vender(self, cantidad: int):
        """
        Realiza la venta de una cantidad del producto.

        Args:
            cantidad (int): El número de unidades a vender.

        Returns:
            float or str: El total a pagar si la venta es exitosa, o un
                          mensaje de error si no hay suficiente stock.
        """
        if self.stock >= cantidad:
            total_pagar = self.precio * cantidad
            self.actualizar_stock(-cantidad)
            return total_pagar
        else:
            return "Error: No hay suficiente stock para realizar la venta."

class Tienda:
    """
    Representa una tienda que gestiona una lista de productos.
    """
    def __init__(self, nombre: str):
        """
        Inicializa una nueva tienda.

        Args:
            nombre (str): El nombre de la tienda.
        """
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto: Producto):
        """
        Añade un producto a la lista de la tienda.

        Args:
            producto (Producto): El objeto Producto a agregar.
        """
        self.productos.append(producto)
        print(f"'{producto.nombre}' ha sido agregado a la tienda '{self.nombre}'.")

    def listar_productos(self):
        """
        Imprime la información de todos los productos disponibles en la tienda.
        """
        print(f"\nTienda: {self.nombre}\n")
        print("Productos disponibles:")
        for producto in self.productos:
            producto.mostrar_info()

    def vender_producto(self, nombre_producto: str, cantidad: int):
        """
        Busca un producto por su nombre y lo vende si hay stock.

        Args:
            nombre_producto (str): El nombre del producto a vender.
            cantidad (int): La cantidad de unidades a vender.
        """
        print(f"\nVendiendo {cantidad} {nombre_producto}(s)...")
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                resultado = producto.vender(cantidad)
                if isinstance(resultado, float):
                    print(f"Total a pagar: ${resultado:.2f}")
                else:
                    print(resultado) # Imprime el mensaje de error
                return
        print(f"Error: Producto '{nombre_producto}' no encontrado.")

# --- Ejemplo de uso ---

# 1. Crear instancia de la Tienda
mi_tienda = Tienda("Super Market")

# 2. Crear instancias de Producto
pan = Producto("Pan", 0.50, 20)
jugo = Producto("Jugo", 1.25, 10)

# 3. Agregar productos a la tienda
mi_tienda.agregar_producto(pan)
mi_tienda.agregar_producto(jugo)

# 4. Listar productos disponibles
mi_tienda.listar_productos()

# 5. Vender un producto
mi_tienda.vender_producto("Jugo", 3)