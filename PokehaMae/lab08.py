#PokeéaMãe, calculadora de poder futuro de seu PokeMães
#Entra-se com seu numero de evolução, especie e poder antes e depois da evolução e recebe-se seu poder estimado futuro
#Maicon Gabriel de Oliveira, ra 221329

#Importa pacote com operções matematicas
import math				#Usado para concatenar o valor de PCf

#Definição de Variaveis in iciais
#--------------------------------

PCa = 1						
Data = ['null']					#Lista de armazenamento acumulado com p[0]=null para que IDs sejam multiplos de 3
lPdata = 0						#Define condição de entrada de Banco de dados
I = 1
N = 0							#Garante o inicio do laço de entrada
a = 3							#Torna o primeiro numero da somatoria equivalente ao primeiro multiplicador



#Entrada do programa
#-------------------

#Condição limitadora de entrada N
while N == 0 or N > 151:

	N = int(input())				#Entrada do numero de evoluções presentes na base de dados


#Laço principal
#--------------

while I != 0 and PCa != 0:			#Condição de saída do programa

	while lPdata != N-1:					#Condição de entrada de banco de dados definido por N

		for lPdata in range(N):
		 
			Pdata = input()											#Entrada de Identificador, Poder anterior e posterior a evolução
			data = [int(i) for i in Pdata.split()]					#Separa entrada em novas variaveis
			Data = Data + data										#Incrementa variaveis em uma so lista com id multiplo de 3
			Data.append(Data[a]/Data[a-1])							#Guarda a cada 4 casas espaço para salvar multiplicador
			a = a + 4												#Somador de posição para calculo
			
		
	
	Pcons = input()												#Entrada de PokeMãe para consulta
	cons = [int(i) for i in Pcons.split()]
	
	
	#Garante parada do programa	
	#--------------------------
	I  = cons[0]
	PCa = cons[1]
	#--------------------------
			
	
	soma = 0
	div = 0
	
			
	NovId = cons[0]						#Estabele posição pelo identificador de procura
		
	for id in range(1,len(Data),4):		#Especifica posição dos proximos ids
				
		if Data[id] == NovId:				#Compara se valor da id anterior é igual ao atual
				
			soma = soma + Data[id+3]			#Especifica onde encontrar multiplicador e o acumula
			div = div + 1						#Soma quantidadde de ocorrencias
				
	if div == 0:						#Laço de saida que evita divisão por zero
		continue
	
	M = soma/div						#Calcula multiplicador medio
	
	PCf = cons[1]*M						#Multiplica PCa inserido por multiplicador medio do id correspondente



 #Saida do programa
 #-----------------
	print(math.ceil(PCf))					#Saída do poder final estimado em numero inteiro