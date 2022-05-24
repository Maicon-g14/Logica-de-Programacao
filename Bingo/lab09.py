#ra221329

def saida(mat,bingo):
	print("+----------------+\n| B  I  N  G  O  |\n+================+")
	for i in range(5):
		print("|",end=" ")
		for j in range(5):
			print(mat[i][j],end=" ")
		print("|")
	print("+----------------+")
	if bingo:
		print("BINGO!")
	
def ver_linha(linha):
	'''verifica linha ou coluna passada em lista'''
	bingo = True
	for i in linha:
		if i != "XX":
			return False
	return True
	
def verificaBingo(mat):
	diagonalP = True;	diagonalS = True
	for i in range(len(mat)):
		linha = ver_linha(mat[i])
		coluna = True
		for lin in range(len(mat)):
			if mat[lin][i] != "XX":
				coluna = False
				break

		if mat[i][i] != "XX":
			diagonalP = False
		if mat[i][(len(mat)-1)-i] != "XX":
			diagonalS = False
			
		if linha or coluna:
			return True
	if diagonalP or diagonalS:
		return True
	return False
	
def entradaCartela():
	armazenaMat = []
	for i in range(5):
		armazenaMat.append(input().split())
	return armazenaMat

def entrada(mat):
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
	bingo = ["B","I","N","G","O"]
	for i in range(len(bingo)):
		if letra == bingo[i]:
			return i

def marcaBingo(letra,val_linha,cartela,qual_laco):
	col = achaCol(letra)
	for i in range(5):
		if cartela[i][col] == val_linha:
			cartela[i][col] = "XX"
			if verificaBingo(cartela):
				return True
			if qual_laco > 1:
				saida(cartela,False)
	return False

def main():
	mat = entradaCartela()
	bingo = entrada(mat)
	saida(mat,bingo)

main()