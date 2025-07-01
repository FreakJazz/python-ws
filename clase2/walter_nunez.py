class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"{self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}")

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            total = self.precio * cantidad
            return total
        else:
            return f"No hay suficiente stock de {self.nombre}. Stock disponible: {self.stock}"


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):
        print("\nProductos disponibles:")
        for producto in self.productos:
            producto.mostrar_info()

    def vender_producto(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre.lower() == nombre_producto.lower():
                resultado = producto.vender(cantidad)
                if isinstance(resultado, float):
                    print(f"\nVendiendo {cantidad} {producto.nombre}(s)...")
                    print(f"Total a pagar: ${resultado:.2f}")
                else:
                    print(resultado)
                return
        print(f"Producto '{nombre_producto}' no encontrado.")


# Ejemplo de uso
if __name__ == "__main__":
    tienda = Tienda("Super Market")

    pan = Producto("Pan", 0.50, 20)
    jugo = Producto("Jugo", 1.25, 10)

    tienda.agregar_producto(pan)
    tienda.agregar_producto(jugo)

    print(f"Tienda: {tienda.nombre}")
    tienda.listar_productos()

    tienda.vender_producto("Jugo", 3)

    print("\nStock actualizado:")
    jugo.mostrar_info()
