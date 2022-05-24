#Simulador de Street Fighter
#Ryu aplica e/ou recebe golpes por 2 turnos e entao se exibe o vencedor da disputa 
#Maicon Gabriel de Oliveira, 221329
v = 0 
pvold = 0 
for i in range(1,3): #Define 2 turnos
	g = int(input()) #Primeira entrada para o laço no turno
	ken = 50 #Vida inicial
	ryu = 50 #Idem acima
	while ken > 0 and ryu > 0:
		if g>0: #Processamneto do combo para Ken
			aux = 0 #Zera aux somadora de golpes
			while g > 0: #Looping para somatoria de golpes recebidos pelo ken
				ken2 = ken
				aux = aux + g #Realiza somatoria de golpes
				ken2 = ken2 - aux #Testa se golpe anterior nao matou personagem
				if ken2 > 0: #Caso nao ocorra hit-kill
					g = int(input()) #Recebe proxima entrada					
					continue
				else: #Caso ocorra hit-kill
					break
		elif g<0: #Processamento do combo para Ryu
			aux = 0
			while g < 0:
				ryu2 = ryu
				aux = aux + g
				ryu2 = ryu2 + aux
				if ryu2 > 0:
					g = int(input())					
					continue
				else:
					break
		if ken > 0 and ryu > 0: #Condição de ocorrencia caso ambos tenham HP
			soma = 0
			l = "" #Zera string do print abaixo
			if aux > 0: #Processa vida de Ken
				pvold = ken
				ken = ken - aux
				l = "Ken:" #Define string de Ken ou Ryu
				pv = ken
				somao = aux
			if aux < 0: #Processa vida de Ryu
				pvold = ryu
				ryu = ryu + aux
				l = "Ryu:"
				pv = ryu
				somao = aux * (-1)
			print(l,pvold,"-",somao,"=",pv) #Exibe Resultados do golpe ou combo
	if ken > 0: #Armazena quem ganhou em cada turno
		v = v + 1
	elif ryu > 0:
		v = v + 2
if v==2: #Compara e define quem é o vencedor
	print("Ken venceu")
elif v==4:
	print("Ryu venceu")
else:
	print("empatou")
