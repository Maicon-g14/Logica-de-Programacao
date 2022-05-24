#ra221329

def fortab(saida,qtde):
	'''impressao de cabecalho/rodape'''
	for i in range(qtde-1):
		print(saida,end=" ")
	print(saida)
	
def saida(mat,bingo):
	'''Funcao de saida'''
	fortab("+----------------+",len(mat))
	fortab("| B  I  N  G  O  |",len(mat))
	fortab("+================+",len(mat))
	
	for i in range(5):		#nas linhas
		for j in range(len(mat)):		#nas matrizes
			print("|",end=" ")
			for k in range(5):		#nas colunas
				print(mat[j][i][k],end=" ")
			if j == len(mat)-1:
				print("|")
			else:
				print("|",end=" ")
	fortab("+----------------+",len(mat))
	if bingo:
		print("BINGO!")
	
def ver_linha(linha):
	'''verifica linha ou coluna passada em lista'''
	bingo = True
	for i in linha:
		if i != "XX":
			return False
	return True
	
def verificaBingo(mat,cart):
	'''verifica ocorrencia de bingo'''
	diagonalP = True;	diagonalS = True
	for i in range(len(mat[cart])):
		linha = ver_linha(mat[cart][i])
		coluna = True
		for lin in range(len(mat[cart])):
			if mat[cart][lin][i] != "XX":
				coluna = False
				break

		if mat[cart][i][i] != "XX":
			diagonalP = False
		if mat[cart][i][(len(mat[cart])-1)-i] != "XX":
			diagonalS = False
			
		if linha or coluna:
			return True
	if diagonalP or diagonalS:
		return True
	return False
	
def entradaCartela():
	'''recebe matriz'''
	armazenaMat = []
	for i in range(5):
		armazenaMat.append(input().split())
	return armazenaMat

def entrada(mat):
	'''recebe numeros cantados'''
	saida(mat,False)
	contador = int(input())
	for i in range(contador):
		j = input().split("-")
		print(str(j[0])+"-"+str(j[1]))
		bingo = marcaBingo(j[0],j[1],mat,contador - i)
		if bingo:
			return bingo
	return False
		
def achaCol(letra):
	'''acha coluna segundo letra'''
	bingo = ["B","I","N","G","O"]
	for i in range(len(bingo)):
		if letra == bingo[i]:
			return i

def marcaBingo(letra,val_linha,cartela,qual_laco):
	'''faz a marcacao na cartela'''
	col = achaCol(letra)
	mostra = False
	bingo = False
	for h in range(len(cartela)):
		for i in range(5):
			if cartela[h][i][col] == val_linha:
				cartela[h][i][col] = "XX"
				if verificaBingo(cartela,h):
					bingo = True
				if qual_laco > 1:		#quando modifica os dois deve mostarr apos modificar o segundo
					mostra = True
	if bingo:
		return True
	elif mostra:
		saida(cartela,False)
	return False

def main():	#OK
	qtde_cart = int(input())
	cartelas = []
	for i in range(qtde_cart):
		cartelas.append(entradaCartela())
	bingo = entrada(cartelas)		#substitui-se matriz por cartelas agora tridimensional
	saida(cartelas,bingo)

main()