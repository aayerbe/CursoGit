email=input("Introduzca su dirección de correo ")
def comprobar(palabra):
	if palabra.count("@")==1 and palabra.endswith("@")==False and palabra.startswith("@")==False:
		print("Es correctoooo")
	elif palabra.count("@")!=1: 
		print("Numero de @ incorrecto")
	elif palabra.endswith("@")==True:
		print("Termina en @")
	elif palabra.startswith("@")==True:
		print("Empieza por @")		
	else:
		print("Es incorrecto")
comprobar(email)
		

	

		