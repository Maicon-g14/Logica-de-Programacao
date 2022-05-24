#Divisores com saida em matriz
#Maicon Gabriel de Oliveira, 221329

#Valor inicial de variáveis
cFinal = 0 			#Contador Final de divisiveis

#Entrada do programa
n = int(input())

if n >= 1 and n <= 100:				#Condição de entrada do programa
	
	for i in range(1,n+1):
		
		for i2 in range(1,n+1):
			
			if i % i2 == 0:			#Compara se é divisivel
			
				print('*',end='')
				cFinal = cFinal + 1
				
			elif i2 % i == 0:		#Compara divisivel no outro eixo
			
				print('*',end='')
				cFinal = cFinal + 1
				
			else:
	
				print('-',end='')
				
			
			#----------------------------
			if i2 == n:
			
				print('')		#Qurbrador de linhas
		
	print(cFinal)