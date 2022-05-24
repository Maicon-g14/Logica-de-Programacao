#O Lobo de Wall Street, programa que determina a decisões de compra e venda visando maximizar o lucro
#Recebe numero de dias + valor diario de açoes e declara quais e quando compra-las e vende-las
#Maicon Gabriel de Oliveira, ra 221329

loop = 0
Database = []
ini = 0
Flucro = []
CoordFinal = []
Lnumeros = []
Inicio_do_SubLucro = []
firstlucro = []
finallucro = []
data_temp = []
coord = []
Ativador_de_saida2 = 0
dc = 0
dv = 0
Pos_em_Database = []
Posicao_em_Database = []
emp = []




def FXYZLucro(N_dias,Database,Num_da_empresa,ini):							
	'''Função que recebe valores e armazena posição onde há lucro na lista de entrada'''
	
	Pos_em_Database = []
	
	for Posicao in range(len(Database[ini])-1):		#0 a 4/								#Laço de localização de valores na lista de valores
		
		if Database[ini][Posicao] >= Database[ini][Posicao+1]:											#Se valor na lista for maior que valor na proxima posição
			
			if Database[ini][Posicao] != Database[ini][0] and Database[ini][Posicao] >= Database[ini][Posicao-1]:
			
				Pos_em_Database.append(Posicao)
			
			continue																				#Pula esse laço
			
		else:
		
			Pos_em_Database.append(Posicao)															#Armazena em lista posição na lista onde houve aumento do valor							k
	
	if Database[ini][-1] > Database[ini][-2]:								#Analiza se ultima posição correspondente a Num_da_empresa na lista é maior que a penultima
	
		Pos_em_Database.append(len(Database[ini])-1)
		
	Posicao_em_Database.append(Pos_em_Database)

	
	
	
	
	
	

def Lucro(Posicao_em_Database,Database):
	'''Função responsavel por repartir e comprarar substring caso empresa tente realizar mais de uma operação no mesmo dia'''
	midlucro = []													#Zera lucro armazenao da empresa anterior
	NarutoTheLastLista = []
	Ativador_de_saida2 = 0										#0 = Off/ 1 = On
	if Posicao_em_Database != []:												#Dia da compra e venda
	
		for laco in range(len(Posicao_em_Database)-1):								#Para tamanho de Posicao_em_Database-1(Coordenada do lucro na database menos ultimo laço*)
			
			if Database[ini][Posicao_em_Database[laco]+1] < Database[ini][Posicao_em_Database[laco]]:			#Caso a posicao posteior for menor que a atual
				
				Inicio_do_SubLucro.append(Posicao_em_Database[laco]+1)			#Armazena a posição inicial do sublucro que acontece no dia[sublucro = 1,3,2,3,4(em 2 começa o sublucro)]

		if Database[ini][Posicao_em_Database[-1]] < Database[ini][Posicao_em_Database[-2]]:			#(*ultimo laço) caso a ultima posição for menor que a penultima
		
			if Database[ini][Posicao_em_Database[laco]+1] != Database[ini][Posicao_em_Database[-1]] and Database[ini][Posicao_em_Database[laco]] != Database[ini][Posicao_em_Database[-2]]:	#!!!!!!!!!!!Se a ultima açao do laço+1 tiver valor diferente da ultima e a penultima for diferente da penultima 
				
				Inicio_do_SubLucro.append(Posicao_em_Database[-1])			#Adiciona ultima posição do lucro

		#Saida 2--------------Caso no mesmo dia o valor das açoes caia e suba novamente
		if Inicio_do_SubLucro != []:
		
			Ativador_de_saida2 = 1
			print(midlucro)
			midlucro.append(Database[ini][Posicao_em_Database[0]:Inicio_do_SubLucro[0]])
			print('mid',midlucro)
			NarutoTheLastLista.append(midlucro[0][-1]-midlucro[0][0])
			
			for separa in range(1,len(Inicio_do_SubLucro)):
				
				midlucro.append(Database[ini][Inicio_do_SubLucro[separa-1]:Inicio_do_SubLucro[separa]])
				NarutoTheLastLista.append((midlucro[-1][-1])-(midlucro[-1][0]))
				
			midlucro.append(Database[ini][Inicio_do_SubLucro[-1]:Posicao_em_Database[-1]+1])
			NarutoTheLastLista.append((midlucro[-1][-1])-(midlucro[-1][0]))
			
			
			#É possivel erro por so acusar coordenada do primeiro numero repetido
			lucro = max(NarutoTheLastLista)						#Encontra o maior lucro
			coord = NarutoTheLastLista.index(lucro)				#Encontra a posição do maior lucro
			dc = midlucro[coord].index(midlucro[coord][0])+1		#Mostra qual o dia de fato ex:[0 a 4]
			dv = midlucro[coord].index(midlucro[coord][-1])+1		#Mostra qual o dia de fato ex:[0 a 4]
			print(dc,dv)
			#Se erro por repetir [0,1,0,1] e der erro so na posição erro deve ser aquiabaixo por nao haver contador de repeticao
			
		
		elif Inicio_do_SubLucro == []:					
			
			lucro = Database[ini][Posicao_em_Database[-1]] - Database[ini][Posicao_em_Database[0]]											#Subtrai posição de sua anterior
			CoordFinal.append(Posicao_em_Database[0])				#Dia da compra
			CoordFinal.append(Posicao_em_Database[-1])				#Dia da venda
	
	else:
		
		lucro = 0
	
	return lucro
	
	

def correge(d):
	'''Função que corrige o numero de saida de empresas no dia, de acordo com o numero de dias inseridos'''
	
	for listaN in range(d*2):
	
		for listaN2 in range(1,d+1):
		
			Lnumeros.append(listaN2)
			

	
def Saida(Flucro,CoordFinal,Lnumeros,Ativador_de_saida2,dc,dv):		#------------------------------------------OK?

	bendito = -1
	repete = []
	lucro_total = 0

	for i in range(0,4):

		if Flucro[i] >= bendito:
		
			if Flucro[i] == bendito:
				
				if Flucro[i] != 0:
				
					repete.append(i)			#Bloco(empresa) d onde há lucro(se d1 d2 d3 ou d4)
					continue
				
			bendito = Flucro[i]
			
			if Flucro[i] != 0:
			
				repete = [i]
				
	lucro_total = bendito*len(repete)				#Cuidado pois posicao inicial de bendito é -1 logo pode implicaar na soma

	if repete != []:

		for j in range(len(repete)):					#Na CoordFinal [0] = dia da compra e [1] é dia da venda; toda compra = 0+2*n e venda = 0+1*nv
			#Numero que de acordo com empre trabalhada aumente 2 na coordenada se nao for falsou repete erro no j
			if Ativador_de_saida2 == 1:
				print('nao e dia')
				dc = Lnumeros[CoordFinal[2*repete[j]]]
				dv = Lnumeros[CoordFinal[(2*repete[j])+1]]
			else:
				print('è dia')
			print("acao %d: compra %d, venda %d, lucro %.2f" % (repete[0+j]+1, dc, dv, (lucro_total/len(repete))))

	print("Lucro: %.2f" % (lucro_total))



#Entrada
#-------
	
while loop == 0:

	d = int(input())											#Entrada do numero de dias a ser considerados

	if d > 15:

		continue
	
	else:
	
		break

		
		
for j in range(4):

	for k in range(d):
		
		Ent = float(input())														#Recebe valores
		data_temp.append(Ent)														#Armazena valores em lista
		
Database = [data_temp[i:i+d] for i in range(0,len(data_temp),d)]					#Divide em sublistas
	
	
	
for Lempresa in range(1,5):									#Define que sera calculado Posicao_em_Database e venda em 4 empresas

	FXYZLucro(d,Database,Lempresa,ini)						#Função responsavel por encontrar quando Posicao_em_Databaser/vender ações
	print(Posicao_em_Database)
	lucroNew = Lucro(Posicao_em_Database,Database,ini)						#Função responsavel por calcular lucro
	ini = Lempresa													#Muda inicializador de laço da função FXYZLucro ao mudar empresa em foco
	
	Flucro.append(lucroNew)
correge(d)
Saida(Flucro,CoordFinal,Lnumeros,Ativador_de_saida2,dc,dv)
	

#add ON/OFF para mesma empresa nao fazer mais Posicao_em_Database e venda