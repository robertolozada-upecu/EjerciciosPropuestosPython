import os
import time

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

def ImprimirCadena(cadena):
	print(cadena)


if __name__ == '__main__':
	while opcion!='6':
		LimpiarPantalla()
		print ("---------------------------------------------")
		print ("------- Ejercicios de Python Parte 1 --------")
		print ("---------------------------------------------")
		print ("")
		print ("Menú de opciones")
		print ("1. Ejercicio 01")
		print ("2. Ejercicio 02")
		print ("3. Ejercicio 03")
		print ("4. Ejercicio 04")
		print ("5. Ejercicio 05")
		print ("6. Salir")
		print ("")
		opcion = input("Seleccione la opción deseada: ")

		with switch(opcion) as s:
			if s.case('1', True):
				print("")
				print("2 elevado a la quinta potencia es: ",2**5)
			if s.case('2', True):
				print("")
				resultado = (10==10 or 10==3)
				print(resultado)
			if s.case('3', True):
				print("")
				edad = int(input("Ingrese la edad: "))
				if edad>=18:
					print("Eres adulto")
				else:
					print("Eres un niño")
			if s.case('4', True):
				print("")
				texto = input("Ingrese el texto a imprimir: ")
				ImprimirCadena(texto)
			if s.case('5', True):
				print("")
				print("Lista actual:")
				artista = ["Maná","Magneto","Hombres G","Soda Stereo","Vilma Palma"]
				print(artista)
				nuevoArtista = input("Ingrese el nuevo artista: ")
				artista.append(nuevoArtista)
				print("\nNueva lista:")
				artista
			if s.case('6', True):
				print("")
				print("¡Gracias, adiós!")
			if s.default():
				print("")
				print("¡No es una opción válida, por favor verifique!")
