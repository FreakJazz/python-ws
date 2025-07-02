# Sistema Básico de Tienda - Programación Orientada a Objetos
# Clase 2
# Versión: 1.00
# Autor: Gabriel Rivera
# Descripción: Sistema para gestionar productos y ventas en una tienda

class Producto:
    """
    Clase que representa un producto en la tienda.
    
    Attributes:
        nombre (str): Nombre del producto
        precio (float): Precio unitario del producto
        stock (int): Cantidad disponible en inventario
    """
    
    def __init__(self, nombre, precio, stock):
        """
        Inicializa un nuevo producto.
        
        Args:
            nombre (str): Nombre del producto
            precio (float): Precio unitario
            stock (int): Cantidad inicial en stock
        """
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def mostrar_info(self):
        """
        Muestra la información completa del producto.
        """
        print(f"{self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}")
    
    def actualizar_stock(self, cantidad):
        """
        Actualiza el stock del producto.
        
        Args:
            cantidad (int): Cantidad a sumar (positiva) o restar (negativa)
        """
        self.stock += cantidad
        print(f"Stock de {self.nombre} actualizado a: {self.stock}")
    
    def vender(self, cantidad):
        """
        Procesa la venta de una cantidad específica del producto.
        
        Args:
            cantidad (int): Cantidad a vender
            
        Returns:
            float or str: Total a pagar si hay stock suficiente, 
                         mensaje de error si no hay stock
        """
        if cantidad <= self.stock:
            self.stock -= cantidad
            total = cantidad * self.precio
            return total
        else:
            return f"Error: No hay suficiente stock. Stock disponible: {self.stock}"


class Tienda:
    """
    Clase que representa una tienda que gestiona múltiples productos.
    
    Attributes:
        nombre (str): Nombre de la tienda
        productos (list): Lista de objetos Producto
    """
    
    def __init__(self, nombre):
        """
        Inicializa una nueva tienda.
        
        Args:
            nombre (str): Nombre de la tienda
        """
        self.nombre = nombre
        self.productos = []
    
    def agregar_producto(self, producto):
        """
        Agrega un producto a la tienda.
        
        Args:
            producto (Producto): Objeto producto a agregar
        """
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado a {self.nombre}")
    
    def listar_productos(self):
        """
        Lista todos los productos disponibles en la tienda.
        """
        print(f"\nTienda: {self.nombre}")
        print("\nProductos disponibles:")
        print("-" * 40)
        
        if not self.productos:
            print("No hay productos disponibles.")
        else:
            for producto in self.productos:
                producto.mostrar_info()
    
    def vender_producto(self, nombre_producto, cantidad):
        """
        Vende una cantidad específica de un producto.
        
        Args:
            nombre_producto (str): Nombre del producto a vender
            cantidad (int): Cantidad a vender
        """
        # Buscar el producto por nombre
        producto_encontrado = None
        for producto in self.productos:
            if producto.nombre.lower() == nombre_producto.lower():
                producto_encontrado = producto
                break
        
        if producto_encontrado is None:
            print(f"Error: Producto '{nombre_producto}' no encontrado en la tienda.")
            return
        
        print(f"\nVendiendo {cantidad} {nombre_producto}...")
        resultado = producto_encontrado.vender(cantidad)
        
        if isinstance(resultado, float):
            print(f"Total a pagar: ${resultado:.2f}")
            print(f"\nStock actualizado:")
            print(f"{producto_encontrado.nombre} | Stock: {producto_encontrado.stock}")
        else:
            print(resultado)


# Ejemplo de uso del sistema
def main():
    """
    Función principal que demuestra el uso del sistema de tienda.
    """
    # Crear tienda
    tienda = Tienda("Super Market")
    
    # Crear productos
    pan = Producto("Pan", 0.50, 20)
    jugo = Producto("Jugo", 1.25, 10)
    leche = Producto("Leche", 2.00, 5)
    
    # Agregar productos a la tienda
    tienda.agregar_producto(pan)
    tienda.agregar_producto(jugo)
    tienda.agregar_producto(leche)
    
    # Listar productos disponibles
    tienda.listar_productos()
    
    # Realizar ventas
    tienda.vender_producto("Jugo", 3)
    
    # Intentar vender más cantidad de la disponible
    print("\n" + "="*50)
    tienda.vender_producto("Leche", 7)
    
    # Actualizar stock manualmente
    print("\n" + "="*50)
    leche.actualizar_stock(10)
    
    # Vender después de actualizar stock
    tienda.vender_producto("Leche", 7)
    
    # Mostrar estado final
    print("\n" + "="*50)
    print("Estado final de la tienda:")
    tienda.listar_productos()


if __name__ == "__main__":
    main()