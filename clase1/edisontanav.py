#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  tarea1.py
#  
#  Copyright 2025 leontv <oefica@disroot.org>

def agregarnombre():
	cadnombre = input("por favor, ingrese su nombre: ")
	return cadnombre
	
def agregaredad():
	iedad = input("por favor, ingrese su edad: ")
	return iedad
	
def agregartalla(): # en metros
	ftalla = input("por favor, ingrese su talla (en metros): ")
	return float(ftalla)
	
def agregarpeso(): # en metros
	fpeso = input("por favor, ingrese su peso (en kilogramos): ")
	return float(fpeso)

def calculaIMC( talla, peso):
	fvalor = peso / talla ** 2
	return float( fvalor )
	
def resultadoIMC( valor ):
	if valor >= 30:
		print("obesidad")
	elif valor >=25 or valor <30:
		print("sobrepeso")
	elif valor >18.5 or valor <25:
		print("sobrepeso")
	else:
		print("obesidad")		
	
if __name__ == '__main__':
    print("Progrma para halla el IMC de un ser humano")
    nombre= agregarnombre()
    edad = agregaredad()
    peso = agregarpeso()
    talla = agregartalla()
    valorimc = calculaIMC( talla, peso)
    print(f"Su IMC es {valorimc:.2f}")
    resultadoIMC( valorimc )

