#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
#  edisontanav.py
#  
#  Copyright 2025 Leo <oefica@disroot.org>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

"""
Crea un clase producto
"""

class Producto:
    
    def __init__(self, cadcodigo, cadnombre, fprecio: float, istock: int):
        """
        Crea un constructor para clase producto
        """
        self.cadcodigo = cadcodigo
        self.cadnombre = cadnombre
        self.fprecio = fprecio
        self.istock = istock
        
    def mostrarexistencia( self):
        """
        Muestra la información del producto
        """
        print(f"Codigo: {self.cadcodigo}, Nombre: {self.cadnombre}, Precio: {self.fprecio:.2f}, Stock: {self.istock}")
        
    def generarventa( self, icantidad: int ):
        self.icantidad = icantidad
        if self.icantidad <= self.istock:
            ftotal = self.icantidad * self.fprecio
            self.istock = self.istock - self.icantidad
            resp = ftotal
        else:
            print("no se dispone del producto")
            resp = 0        
        return resp
        
    def actualizarstock(self, icantidad: int):
        """
        Actualiza el stok de productos, la cantida puede ser positiva o negativa
        """
        self.icantidad = icantidad
        self.istock = self.istock + self.icantidad
        return self.istock

class Tienda:
    def __init__(self, cadnombretienda):
        """
        Crea un constructor para clase producto
        """
        self.cadnombretienda = cadnombretienda
        self.productos = []

    def agregaproductos(self, productos: Producto):
        self.productos.append(productos)
        
    def listar_productos(self):
        """
        Lista los productos en la tienda
        """
        print(f"Tienda: {self.cadnombretienda}")
        print("codigo,producto,precio,stock")
        for producto in self.productos:
            print(f"{producto.cadcodigo},{producto.cadnombre},{producto.fprecio},{producto.istock}")
    
    def venderproducto(self, codigoproducto):
        """
        Vende un producto de la tienda
        """
        for producto in self.productos:
            if producto.cadcodigo == codigoproducto:
                self.productos.remove(producto)
                print(f"Producto vendido: {producto.cadcodigo}")
                return
        print(f"Producto '{codigoproducto}' no encontrado en tienda.")
        
if __name__ == '__main__':
    print("Programa para simular productos de una tienda")
    producto1 = Producto("A100", "Arroz", 12.5, 200)
    producto2 = Producto("A101", "Aceite", 1.5, 100)
    #print(producto1.cadnombre)
    producto1.mostrarexistencia()
    producto1.actualizarstock(100)
    producto1.mostrarexistencia()
    venta = 10
    print(f"Se vendió {venta} cantidades del producto: {producto1.cadnombre} \n \tSu Valor total de: $ {producto1.generarventa(venta):.2f}") # cantidad en numero enteros
    producto1.mostrarexistencia()

    # Parte 2    
    #Crea un objeto de tipo Tienda
    tienda1 = Tienda("GeoQuito S.A.S")
    tienda1.agregaproductos(producto1)
    tienda1.agregaproductos(producto2)
    print("-------------------")
    print("REPORTE PRODUCTOS")
    print("-------------------")    
    tienda1.listar_productos()
    tienda1.venderproducto("A100")
    print("-------------------")
    print("REPORTE DE VENDIDOS")
    print("-------------------")
    tienda1.listar_productos()
    print("Gracias por usar este programa")
    
# SALIDA DEL PROGRAMA
# Programa para simular productos de una tienda
# Codigo: 100, Nombre: Arroz, Precio: 12.50, Stock: 200
# Codigo: 100, Nombre: Arroz, Precio: 12.50, Stock: 300
# Se vendió 10 cantidades del producto: Arroz 
 	# Su Valor total de: $ 125.00
# Codigo: 100, Nombre: Arroz, Precio: 12.50, Stock: 290
# -------------------
# REPORTE PRODUCTOS
# -------------------
# Tienda: GeoQuito S.A.S
# codigo,producto,precio,stock
# 100,Arroz,12.5,290
# 101,Aceite,1.5,100
# Producto vendido: 100
# -------------------
# REPORTE DE VENDIDOS
# -------------------
# Tienda: GeoQuito S.A.S
# codigo,producto,precio,stock
# 101,Aceite,1.5,100
