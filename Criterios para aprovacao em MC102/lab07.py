#ra221329

def entrada():
	'''recebe parametros de entrada'''
	return ([float(x) for x in input().split()])

def entra_tupla(x):
	'''entra tuplas (nota,peso) e sai media'''
	x = x[1:-1]
	x = x.split(",")
	f = float(x[0])
	i = int(x[1])
	return (f,i)
	
def media(x,y):
	'''calcula media de lista de valores'''
	aux = 0
	for i in x:
		aux += i
	if y == 0:
		return aux/len(x)
	else:
		return aux/y

def provas():
	'''faz entrada das notas de prova e acrescenta seu peso'''
	ps = entrada()
	ps[0] = ps[0]*2
	ps[1] = ps[1]*3
	return ps

def nota(ac,lab,ps):
	'''calcula media final de aprovado'''
	m = (0.6*ps)+(0.3*lab)+(0.1*ac)
	if m > 5:
		return m
	else:
		return 5

def medialab(x):
	'''calcula media dos laboratorios recebendo tuplas (nota,peso)'''
	aux = 0
	somapeso = 0
	for i in x:
		aux += i[0]*i[-1]
		somapeso += i[-1]
	return aux/somapeso

def Cexa(x,ps,lab):
	'''calcula nota final de exame'''
	a = entremin(ps,lab)
	return ((a+x)/2)
	
def saida(ac,lab,ps,exa):
	'''mostra as primeiras saidas do programa'''
	print("Media das atividades conceituais:", format(ac, ".1f"))
	print("Media das tarefas de laboratorio:", format(lab, ".1f"))
	print("Media das provas:", format(ps, ".1f"))
	if exa != 0:
		print("Nota no exame:", format(exa, ".1f"))

def entremin(x,y):
	'''retorna menor entre 2 valores'''
	if x < y:
		return x
	else:
		return y

def main():
	ac = entrada()	#notas conceituais
	lab = [entra_tupla(x) for x in input().split()]	#notas de lab
	ps = provas()	#notas de provas
	freq = int(input())	#recebe frequencia

	ac = media(ac,0)	#media das conceituais
	lab = medialab(lab)
	ps = media(ps,5)	#tira media de provas

	if freq < 75:	#frequencia
		mfinal = entremin(lab,ps)
		saida(ac,lab,ps,0)
		print("Reprovado(a) por frequencia.")
		print("Media final:", format(mfinal, ".1f"))

	elif ps >=5 and lab >=5:	#passou direto
		mfinal = nota(ac,lab,ps)
		saida(ac,lab,ps,0)
		print("Aprovado(a) por nota e frequencia.")
		print("Media final:", format(mfinal, ".1f"))

	elif ps >= 2.5 and lab >= 2.5:	#exame
		exam = float(input())	
		mfinal = Cexa(exam,ps,lab)
		saida(ac,lab,ps,exam)
		if mfinal >= 5:
			print("Aprovado(a) por nota e frequencia.")
		else:
			print("Reprovado(a) por nota.")
		print("Media final:", format(mfinal, ".1f"))

	else:
		mfinal = entremin(ps,lab)
		saida(ac,lab,ps,0)
		print("Reprovado(a) por nota.")
		print("Media final:", format(mfinal, ".1f"))

main()
