#Simulador de Street Fighter Avancado
#Ryu aplica e/ou recebe golpes com bonus por 2 turnos e entao se exibe o vencedor da disputa 
#Maicon Gabriel de Oliveira, 221329

#Variaveis iniciais
v = 0 					#Contador de Vitórias
pvold = 0 				#Armazena pontos de vida(HP)
somao = 0				#Armazena soma final de pontos recebidos ou inflingidos 
pv = 0
soma = 0

#Define 2 turnos
for i in range(1,3): 
	
	golpe = int(input()) 		#Primeira entrada para o laço no turno
	ken = 2000 				#Vida inicial
	ryu = 2000 				#Idem acima
	
	while ken > 0 and ryu > 0:
	
		somaGolpe = 0
		somaLacoT = 0
		
		
		if golpe == 0: #Evita crash em caso de golpe nulo (não direcionado a Ryu nem a Ken)
			continue
		
		
		
		#-------------------------------
		#Processamneto do combo para Ken
		#-------------------------------
		
		elif golpe > 0: 
			
			soma = 0 					#Zera soma somadora de golpes
			
			while golpe > 0: 				#Looping para somatoria de golpes recebidos pelo ken
								
				ken2 = ken
				soma = soma + golpe 					#Realiza somatoria de golpes
				golpeOLD = golpe
				triangular = True 						#Ativa Proccessamento de numero triangular
				
				
				
				#Processamento de numero perfeito
				#--------------------------------
				
				somaGolpe = 0									##Atenção!!!
				
				while golpeOLD > 0:
						
					golpeOLD = golpeOLD - 1
						
					if golpeOLD != 0 and golpe%golpeOLD == 0: 		#Evita divisao por zero e compara se golpe é divisivel
							
						somaGolpe = somaGolpe + golpeOLD 						
					
				if somaGolpe == golpe:
						
					soma = soma - golpe
					soma = soma + (golpe*3) 			#3X valor caso perfeito ou perf e triangular
					triangular = False 						
								
				
				
				#Processamento de numero triangular
				#----------------------------------
				
				if triangular:	
					 
					for lacoT in range(1,golpe+1):
						
						somaLacoT = somaLacoT + lacoT 		#Somatoria crescente de numeros
						
						if somaLacoT == golpe:
							
							soma = soma - golpe 
							soma = soma + (golpe*2) 
							break
							
							
				
				#Teste de hit-kill
				#-----------------
				ken2 = ken2 - soma 				
				
				if ken2 > 0: 						#Caso nao hit-kill
					
					somaLacoT = 0
					golpe = int(input()) 					#Recebe proxima entrada
					continue
					
				else: 								#Caso hit-kill
					
					break
					
					
					
		#-------------------------------			
		#Processamento do combo para Ryu
		#-------------------------------
		
		elif golpe < 0: 
			
			soma = 0
			
			while golpe < 0:
				
				ryu2 = ryu
				soma = soma + golpe
				soma = soma * (-1) 					#Inverte valor da soma
				golpePOS = golpe * (-1)				#Inverte valor do golpe
				golpeOLD = golpePOS
				triangular = True
				
				
				
				#Processamento de numero perfeito
				#--------------------------------
				
				somaGolpe = 0									##Atenção!!!
				
				while golpeOLD > 0:
					
					golpeOLD = golpeOLD - 1
					
					if golpeOLD != 0 and golpePOS % golpeOLD == 0:
						
						somaGolpe = somaGolpe + golpeOLD
						
				if somaGolpe == golpePOS:
					
					soma = soma + golpe
					soma = soma - (golpe*3)
					triangular = False
			
				
				
				#Processamento de numero triangular
				#----------------------------------
				
				if triangular:	
					
					somaLacoT = 0										##Atenção!!!
					
					for lacoT in range(1,golpePOS+1):
						
						somaLacoT = somaLacoT + lacoT
						
						if somaLacoT == golpePOS:
						
							soma = soma + golpe
							soma = soma - (golpe*2)
							break
							
							
							
				soma = soma*(-1) 			#Retorna soma para valor negativo
				
				
				
				#Teste de hit-kill
				#-----------------
				
				ryu2 = ryu2 + soma
	
				if ryu2 > 0:						#Caso nao hit-kill
			
					somaLacoT = 0
					golpe = int(input())					#Recebe proxima entrada	
					continue
					
				else:								#Caso hit-kill
					
					break
					
					

		#----------------------
		#Processamento de Saída
		#----------------------
		
		if ken > 0 and ryu > 0: 					#Condição de ocorrencia caso ambos tenham HP
			
			l = "" 											#Zera string do print abaixo
			
			
			
			#Variaveis do Ken
			#----------------
			
			if soma > 0: 
				
				pvold = ken
				ken = ken - soma 									#Define novo HP
				l = "Ken:" 											#Define string para Ken
				pv = ken
				somao = soma
				
				
			
			#Variaveis do Ryu
			#----------------
			
			if soma < 0: 
				
				pvold = ryu
				ryu = ryu + soma									#Define novo HP
				l = "Ryu:"											#Define string para Ryu
				pv = ryu
				somao = soma * (-1)
				
				
				
			#-----
			#Saída
			#-----
			
			print(l,pvold,"-",somao,"=",pv) 
			
			
	
	#---------------------
	#Definição de Vencedor
	#---------------------
	
	#Armazena quem ganhou em cada turno
	#----------------------------------
	
	if ken > 0: 
	
		v = v + 1
		
	elif ryu > 0:
		
		v = v + 2
		
		
		
#--------------------
#Exibição de Vencedor
#--------------------

if v == 2:
	
	print("Ken venceu")
	
elif v == 4:
	
	print("Ryu venceu")
	
else:
	
	print("empatou")
