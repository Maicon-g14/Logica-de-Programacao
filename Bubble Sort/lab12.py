#221329

def entrada():
	'''recebe entrada'''
	return input().split()

def intera(lista):
	'''transforma numeros em inteiro'''
	for i in range(len(lista)):
		lista[i] = int(lista[i])
	
def printa(lista):
	'''Chama saida do programa'''
	print(str(len(lista)*".")+str(".."))
	aux = maior(lista)
	while aux > 0:		#roda linha
		print(".",end="")
		for i in lista:		#roda coluna
			if i >= aux:
				print("|",end="")
			else:
				print(" ",end="")
		aux-=1
		print(".")
	print(str(len(lista)*".")+str(".."))
	
def maior(vet):
	'''retorna maior elemento da lista'''
	maior = vet[-1]
	for i in range(len(vet)-1,-1,-1):
		if vet[i] > maior:
			maior = vet[i]
	return maior
	
def bubble(lista):
	'''ordena por bubble-sort'''
	printa(lista)
	for j in range(len(lista)-1):
		for i in range(len(lista)-1):
			if lista[i] > lista[i+1]:
				lista[i],lista[i+1] = lista[i+1],lista[i]
				printa(lista)
				
def main():
	vals = entrada()
	intera(vals)
	bubble(vals)
	
main()