#ra221329

Dpont = {}		#pontuação dos jogadores
Dvit = {}		#quantidade de gols feitos
Dsaldo = {}		#gols_pro menos sofridos
Dgpro = {}		#valor dado
dic = [Dpont,Dvit,Dsaldo,Dgpro]
vence = []
empate = False
aff = []

n = int(input())

for i in range(n*(n-1)):	#Entrada
	inp = input().split()
	inp[1] = int(inp[1])
	inp[4] = int(inp[4])
	for p in dic:		#inicializa dicionarios
		if inp[0] not in p:
			p[inp[0]] = 0
		if inp[3] not in p:
			p[inp[3]] = 0

	#----Busca go pro-----
	Dgpro[inp[0]] += inp[1]
	Dgpro[inp[3]] += inp[4]
	
	#-----Busca vitorias/Pontuação-----
	if inp[1] > inp[4]:		#primeiro vence no jogo
		Dvit[inp[0]] += 1
		Dsaldo[inp[0]] += inp[4]
		Dsaldo[inp[3]] += inp[1]
	elif inp[1] == inp[4]:		#Empate
		Dpont[inp[0]] += 1
		Dpont[inp[3]] += 1
		Dsaldo[inp[0]] += inp[4]
		Dsaldo[inp[3]] += inp[1]
	else:		#Segundo vence
		Dvit[inp[3]] += 1
		Dsaldo[inp[3]] += inp[1]
		Dsaldo[inp[0]] += inp[4]
	
#-----Pontuação-----
for l in Dvit:
		Dpont[l] += Dvit[l] * 3
		
#-----Saldo corrigido-----
for q in Dsaldo:
	Dsaldo[q] = Dgpro[q] - Dsaldo[q]
		
for t in sorted(Dgpro):		#Saida
	print(t, Dpont[t], Dvit[t], Dsaldo[t], Dgpro[t])

#-----Vence-----
for i in Dpont:
	if vence == []:
		vence.append(i)
		vence.append(Dpont[i])
	elif Dpont[i] > vence[1]:
		vence[0] = i
		vence[1] = Dpont[i]
		empate = False
		aff = []
	elif Dpont[i] == vence[1]:
		empate = True
		if i not in aff:		#passa para frente somente os empatados
			aff.append(i)

if empate:
	aff.append(vence[0])	#passa o nome
	vence = []
	proximo = []
	for i in aff:
		if vence == []:
			vence.append(i)
			vence.append(Dvit[i])
		elif Dvit[i] > vence[1]:
			vence[0] = i
			vence[1] = Dvit[i]
			empate = False
			proximo = []
		elif Dvit[i] == vence[1]:
			empate = True
			if i not in proximo:
				proximo.append(i)

if empate:
	proximo.append(vence[0])	#passa o nome
	vence = []
	aff = []
	for i in proximo:
		if vence == []:
			vence.append(i)
			vence.append(Dsaldo[i])
		elif Dsaldo[i] > vence[1]:
			vence[0] = i
			vence[1] = Dsaldo[i]
			empate = False
			aff = []
		elif Dsaldo[i] == vence[1]:
			empate = True
			if i not in aff:
				aff.append(i)

if empate:
	aff.append(vence[0])	#passa o nome
	vence = []
	for i in aff:
		if vence == []:
			vence.append(i)
			vence.append(Dvit[i])
		elif Dgpro[i] > vence[1]:
			vence[0] = i
			vence[1] = Dgpro[i]
			empate = False
					
print("Vencedor:",vence[0])
