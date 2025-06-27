
class Mascota:
    def __init__(self, tipo, nombre):
        self.tipo = tipo
        self.nombre = nombre
        
    def dueño(self, nombre):
        print(f"El dueñ@ de {self.nombre} es {nombre}")
        print("El dueñ@ de ", self.nombre ," es " , nombre)

class Perro(Mascota):

    def hablar(self):
        print(f"{self.nombre} es perro y ladra")
        
    def acciones(self):
        print(f"{self.nombre} mueve la cola")
        
class Gato(Mascota):
        
    def hablar(self):
        print(f"{self.nombre} dice miau")
        
    def acciones(self):
        print(f"{self.nombre} trepa a los arbol")

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = ["Shampoo"] 
        
    def agregar_producto(self, nombre):
        self.productos.append(nombre)
        
    def listar_producto(self):
        print("Los productos son: ")
        for producto in self.productos: 
            print(f"{producto}")
        
    def vender_producto(self, nombre_producto, cantidad):
        for producto in self.productos: 
            if producto.capitalize() == nombre_producto.capitalize():
                print(f"Existe el producto {nombre_producto}, se vende la cantidad de {cantidad}")
                return
        print(f"No existe el producto")
                
class Producto(Tienda):
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        
    def vender(self, cantidad):
        if (self.stock > cantidad):
            total = self.precio * cantidad
            self.stock -= cantidad
            return total
        else: 
            print("No existe el stock suficiente")
            return None      
            
if __name__ == "__main__":
    tienda = Tienda("Micromercado Maria")
    tienda.agregar_producto("Jabon")
    tienda.agregar_producto("Acondicionador")
    tienda.agregar_producto("Cepillo")
    tienda.agregar_producto("Galletas")
    tienda.listar_producto()
    tienda.vender_producto("JABON", 3)
    producto1 = Producto("jabon", 1, 15)
    producto2 = Producto("shampoo", 2, 15)
    producto3 = Producto("galletas", 3, 2)
    
    total3 =producto3.vender(5)
    print(total3)
    
    total2 =producto2.vender(6)
    print(total2)
    stock2 = producto2.stock
    
    print(stock2)
    
    
    

        
