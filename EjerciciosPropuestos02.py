# -*- coding: iso-8859-15 -*-

from ctypes.wintypes import INT
import os
from pickle import TRUE
import time
import csv
import SumarListaNumeros

class switch:
	def __init__(self, variable, comparator=None, strict=False):
		self.variable = variable
		self.matched = False
		self.matching = False
		if comparator:
			self.comparator = comparator
		else:
			self.comparator = lambda x, y: x == y
		self.strict = strict

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		pass

	def case(self, expr, break_=False):
		if self.strict:
			if self.matched:
				return False
		if self.matching or self.comparator(self.variable, expr):
			if not break_:
				self.matching = True
			else:
				self.matched = True
				self.matching = False
			return True
		else:
			return False

	def default(self):
		return not self.matched and not self.matching

def LimpiarPantalla():
	time.sleep(2)
	#var = os.name
	#print ("El sistema operativo de mi ordenador es: "+var) 
	if os.name == "posix":
		os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system ("cls")



if __name__ == '__main__':
	opcion = 0
	while opcion!='8':
		LimpiarPantalla()
		print ("---------------------------------------------")
		print ("------- Ejercicios de Python Parte 2 --------")
		print ("---------------------------------------------")
		print ("\nMenú de opciones")
		print ("1. Ejercicio 01")
		print ("2. Ejercicio 02")
		print ("3. Ejercicio 03")
		print ("4. Ejercicio 04")
		print ("5. Ejercicio 05")
		print ("6. Ejercicio 06")
		print ("7. Ejercicio 07")
		print ("8. Salir")
		print ("")
		opcion = input("Seleccione la opción deseada: ")

		with switch(opcion) as s:
			if s.case('1', True):
				frase = input("\nIngrese una frase: ")
				frase = frase.upper()
				print("\nLa frase ingresada en mayúsculas es: {}\n".format(frase))
			if s.case('2', True):
				texto = input("\nIngrese el texto: ")
				aux = ""
				for caracter in texto:
					if caracter == "a":
						aux += "@"
					elif caracter == "i":
						aux += "1"
					else:
						aux += caracter
				print("\nEl texto con los carateres reemplazados es: {}\n".format(aux))
			if s.case('3', True):
				print("\nLos números entre el 20 y 30 son: ")
				for i in range(21,31):
					print(i)
				print("")
			if s.case('4', True):
				Lista_numeros = []
				print("\nIngrese el listado de números, para finalizar ingrese la letra q")
				while True:
					try:
						aux = input ("Ingrese un número: ")
						if aux == "q" or aux == "Q":
							break
						else:
							aux = int(aux)
							Lista_numeros.append(aux)
					except:
						print("¡Por favor ingrese un dato númerico!")
				if len(Lista_numeros) != 0:
					print("\nLa lista de los números ingresados es: {}\n".format(Lista_numeros))
				else:
					print("\n¡No se ha ingresado ningún dato a la lista!\n")
			if s.case('5', True):
				Lista_numeros = []
				print("\nIngrese el listado de números, para finalizar ingrese la letra q")
				while True:
					try:
						aux = input ("Ingrese un número: ")
						if aux == "q" or aux == "Q":
							break
						else:
							aux = int(aux)
							Lista_numeros.append(aux)
					except:
						print("¡Por favor ingrese un dato númerico!")
				if len(Lista_numeros) != 0:
					print("\nLa suma de los números de la lista es: {}\n".format(SumarListaNumeros.SumarLista(Lista_numeros)))
				else:
					print("\n¡No se ha ingresado ningún dato a la lista!\n")
			if s.case('6', True):
				print("\nLas líneas del archivo de texto son:")
				archivo = open('ArchivoTexto.txt', 'r')
				ListaLineas = archivo.readlines()
				i = len(ListaLineas) - 1
				while i >= 0:
					print(ListaLineas[i], end="")
					i -= 1
				print("\n")
				archivo.close()
			if s.case('7', True):
				Lista_peliculas = []
				print("\nIngrese el listado de películas, para finalizar ingrese la letra q")
				while True:
					aux = input ("Ingrese la película: ")
					if aux == "q" or aux == "Q":
						break
					else:
						Lista_peliculas.append(aux)
				with open('ListaPeliculas.csv', 'w', newline="") as archivo:
					escribir = csv.writer(archivo, delimiter=",")
					escribir.writerow({"Listado de películas"})
					escribir.writerow(Lista_peliculas)
				if len(Lista_peliculas) != 0:
					print("\nLa lista de películas ingresadas es:\n{}\n".format(Lista_peliculas))
					print("¡El archivo CSV ha sido creado exitosamente!\n")
				else:
					print("\n¡No se ha ingresado ninguna película a la lista!\n")
			if s.case('8', True):
				print("\n¡Gracias, adiós!\n")
			if s.default():
				print("")
				print("¡No es una opción válida, por favor verifique!")

