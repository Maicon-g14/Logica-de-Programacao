#ra 221329

#Entrada inicial
tipo_do_objeto = input()
caractere = input()


#Condição principal
if tipo_do_objeto == "Q":

	#Quadrado
	medida_lado = int(input())
	if medida_lado < 3:
		print("Dimensao incorreta.")
	else:
		for i in range(medida_lado):	#Representa linha
			if i == 0 or i == (medida_lado-1):	#Em primeira ou ultima linha
				print(caractere*medida_lado)
			else:		#Em demais linhas
				print(caractere + (" " * (medida_lado-2)) + caractere)

elif tipo_do_objeto == "R":

	#Retangulo
	medida_da_largura = int(input())
	medida_da_altura = int(input())
	if medida_da_largura < 3 or medida_da_altura < 3:
		print("Dimensao incorreta.")
	else:
		for i in range(medida_da_altura):	#Representa linha
			if i == 0 or i == (medida_da_altura-1):	#Em primeira ou ultima linha
				print(caractere*medida_da_largura)
			else:		#Em demais linhas
				print(caractere + (" " * (medida_da_largura-2)) + caractere)

elif tipo_do_objeto == "P":

	#Paralelogramo
	medida_da_largura = int(input())
	medida_da_altura = int(input())
	if medida_da_largura < 3 or medida_da_altura < 3:
		print("Dimensao incorreta.")
	else:
		for i in range(medida_da_altura):	#Representa linha
			if i == 0:	#Em primeira linha
				print(caractere*medida_da_largura)
			elif (i == (medida_da_altura-1)):	#Em ultima linha
				print((" " * (medida_da_altura-1)) + caractere*medida_da_largura)
			else:		#Em demais linhas
				print((" " * i) + caractere + (" " * (medida_da_largura-2)) + caractere)

elif tipo_do_objeto == "L":

	#Losango
	medida_lado = int(input())
	if medida_lado < 3:
		print("Dimensao incorreta.")
	else:
		aux = 1
		for i in range(1,2*medida_lado):	#Representa linha
			if i == 1 or (i == (2*medida_lado-1)):	#Em primeira ou ultima linha

				print((" " * (medida_lado-1)) + caractere)

			elif i < medida_lado:	#1 metade do losango

				print((" " * (medida_lado-i)) + caractere + (" " * aux) + caractere)
				aux += 2

			elif i > medida_lado:	#2 metade do losango

				aux -= 2
				print((" " * (i-medida_lado)) + caractere + (" " * aux) + caractere)

			else:	#Meio do losango

				print(caractere + (" " * (2*medida_lado-3)) + caractere)

elif tipo_do_objeto == "C":

	#Cruz
	medida_lado = int(input())
	if medida_lado < 3:
		print("Dimensao incorreta.")
	else:
		for i in range(3*medida_lado-2):	#Representa linha
			if i == 0 or i == (3*medida_lado-3):	#Em primeira ou ultima linha
				print((" " * medida_lado) + caractere*medida_lado)
			elif i < medida_lado-1:		#Primeira parte
				print((" " * medida_lado) + caractere + (" " * (medida_lado-2)) + caractere)
			elif i == medida_lado-1 or i == 2*medida_lado-2:		#Linhas continuas centrais
				print((3 * medida_lado) * caractere)
			elif i > medida_lado-1 and i < 2*medida_lado-2:		#Parte central
				print(caractere + (" " * (medida_lado-2)) + caractere + caractere + (" " * (medida_lado-2)) + caractere + caractere + (" " * (medida_lado-2)) + caractere)
			elif i > 2*medida_lado-2 and i < 3*medida_lado-3:	#Ultima parte
				print((" " * medida_lado) + caractere + (" " * (medida_lado-2)) + caractere)
			else:		#Em demais linhas
				print(caractere + (" " * (medida_lado-2)) + caractere)

else:
	print("Objeto incorreto.")
