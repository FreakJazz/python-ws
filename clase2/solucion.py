# clase_2

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
            total = self.precio * cantidad
            self.stock -= cantidad
            return total
        else:
            print(f"No hay suficiente stock de {self.nombre}. Stock disponible: {self.stock}")
            return None

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):
        print(f"\nProductos disponibles en {self.nombre}:")
        for prod in self.productos:
            prod.mostrar_info()

    def vender_producto(self, nombre_producto, cantidad):
        for prod in self.productos:
            if prod.nombre.lower() == nombre_producto.lower():
                total = prod.vender(cantidad)
                if total is not None:
                    print(f"\nVenta realizada. Total a pagar: ${total:.2f}")
                return
        print(f"Producto '{nombre_producto}' no encontrado.")

# Ejecutar programa
if __name__ == "__main__":
    tienda = Tienda("Super Alison")

    pan = Producto("Pan", 0.50, 20)
    jugo = Producto("Jugo", 1.25, 10)

    tienda.agregar_producto(pan)
    tienda.agregar_producto(jugo)

    tienda.listar_productos()
    tienda.vender_producto("Jugo", 3)
    tienda.listar_productos()
