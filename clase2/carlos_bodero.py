#clase 2
class Producto:
    def __init__(self,nombre,precio,stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"Nombre:{self.nombre} Precio:{self.precio} Stock:{self.stock}")

    def actualizar_stock(self,cantidad):
        self.stock +=cantidad
    
    def vender(self,cantidad):
        if cantidad > self.stock:
            print("no hay suficiente stock")
        else:
            self.stock -=cantidad
            print(f"Vendidos :{cantidad} Total a pagar:{cantidad*self.precio}")
    
    def __str__(self):
        return self.nombre+" Precio:"+str(self.precio)+" Stock:"+str(self.stock)


class Tienda:
    nombre = ""
    productos = []

    def __init__(self,nombre):
        self.nombre = nombre


    def agregar_producto(self,elproducto):
        self.productos.append(elproducto)

    def listar_productos(self):
        for iterador in self.productos:
            #print(f"nombre: {Producto(iterador).nombre} precio: {Producto(iterador).precio} stock: {Producto(iterador).stock}")
            print(iterador)

    def vender_producto(self,nombre_producto, cantidad):
        for iterador in self.productos:
            if iterador.nombre == nombre_producto:
                print(f"Por vender {iterador}")
                iterador.vender(cantidad)
                print("Vendido")
                

if __name__ == "__main__":
    latienda  = Tienda("Mercadito")
    destornillador = Producto("destornillador",14,10)
    martillo = Producto("martillo",7,15)
    pinzas = Producto("pinzas",5,20)
    latienda.agregar_producto(destornillador)
    latienda.agregar_producto(martillo)
    latienda.agregar_producto(pinzas)
    print(f"++++ Tienda {latienda.nombre} ++++++++")
    print("+++++Los productos son:  +++++++")
    latienda.listar_productos()
    print("+++++venta de Producto +++++++")
    latienda.vender_producto("martillo",4)
    print("+++++Stock de Tienda despues de venta ++++++++")
    latienda.listar_productos()


