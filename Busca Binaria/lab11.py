#ra221329


def checa_ordem(lista):		
	'''checa se lista esta ordenada crescentemente'''
	if len(lista) > 1:
		for i in range(len(lista)-1):
			if lista[i] > lista[i+1]:
				return False
	return True
	
def ini_lista(lista,chave):		
	'''mostra lista inicial'''
	print("Elemento procurado:",str(chave).zfill(3))
	linha(0,len(lista))
	print()
	print("|",end="")
	for i in lista:
		print(" ",end="")
		print(str(i).zfill(3),end=" |")
	print()
	linha(0,len(lista))
	print()
	
def linha(ini,fim):	
	'''mostra borda'''
	while ini+1 <= fim:
		print("+-----",end="")
		ini+=1
	print("+",end="")
	
def linha_null(ini,fim):		
	'''cria espaços na printagem'''
	pos = 0
	while pos < ini:
		print("      ",end="")
		pos+=1
	
def linha_sf(ini,fim):	
	linha_null(ini,fim)
	linha(ini,fim)
	
def borda_esp(ini,meio,fim):
	'''cria as bordas'''
	linha_sf(ini,meio)
	print("=====",end="")
	linha(meio,fim)
	print()

def estado_lista(lista,meio,ini,fim):		
	'''exibe saida'''
	tam = len(lista)
	borda_esp(ini,meio,fim)
	linha_null(ini,fim)
	print("|",end="")
	for i in range(tam):
		if meio == i:
			print("|",end="")
			print(str(lista[i]).zfill(3),end="||")
		elif i > fim:
			aux = fim - i
			[print(" ",end="") for j in range(aux)]
		elif i < ini:
			aux = i - ini
			[print(" ",end="") for j in range(aux)]
		else:
			print(" ",end="")
			print(str(lista[i]).zfill(3),end=" |")
	print()
	borda_esp(ini,meio,fim)
	
def busca_bin(lista,chave):		
	'''busca binaria'''
	if not checa_ordem(lista):
		return -2
	ini = 0
	fim = len(lista)-1
	while fim >= ini:
		meio = (ini+fim)//2
		estado_lista(lista,meio,ini,fim)
		if lista[meio] == chave:
			return meio
		elif lista[meio] > chave:
			fim = meio-1
		else:
			ini = meio+1
	return -404
	
def interaliza(lista):		#passa pra inteiros
	'''transforma elementos da lista em inteiros'''
	for i in range(len(lista)):
		lista[i] = int(lista[i])
	
def entrada():		#recebe valores
	chave = int(input())
	lista = input().split()
	interaliza(lista)
	return (lista,chave)
	
def main():
	aux = entrada()
	ini_lista(aux[0],aux[1])
	res = busca_bin(aux[0],aux[1])
	if res == -404:
		print("O elemento nao foi encontrado")
	elif res == -2:
		print("Vetor nao estah ordenado")
	else:
		print("O elemento estah na posicao",res)
	
main()
	
	
