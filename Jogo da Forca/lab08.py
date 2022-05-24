#ra 221329
from forca import lista_palavras, cenas_forca
import re


def busca(resp,letra):
	'''busca todas as ocorrencias da letra na palavra e poe em lista'''
	ocorrencias_pos = []
	a = re.compile(letra)		#prepara letra a ser buscada
	aux = a.search(resp)		#busca 1 ocorrencia
	if aux is not None:		#se houver uma ocorrencia
		if aux not in ocorrencias_pos:
			ocorrencias_pos.append(aux.span()[0])		#guardo posicao da ocorrencia
		while aux is not None and len(resp) > aux.span()[-1]:		#se houver espaço para mais busca
			aux = a.search(resp,aux.span()[-1])		#busco a partir da da proxima posicao a encontrada
			if aux is not None and aux not in ocorrencias_pos:		#se algo for encontrado
				ocorrencias_pos.append(aux.span()[0])	#acrescento sua posicao na lista
	return ocorrencias_pos
	
	
	
def superprint(cena,palavra,erro):
	'''Exibe conteudos da tela'''
	print(cenas_forca[cena])
	print("Palavra:",end=" ")
	print(*palavra,sep="  ")
	if erro != []:
		print("Tentativa(s) incorreta(s):",*erro,sep=" ")
		
		
		
def entrada(palavra,erro,cena):
	'''chama/verifica entrada'''
	while True:
		letra = input("Proxima letra: ")
		if letra in erro or letra in palavra:
			print("Voce jah escolheu esta letra.\n")
			superprint(cena,palavra,erro)
		else:
			break
	return letra
	
	
	
def cenario(resposta,palavra,cena=0,erro=[]):
	'''Atualiza status do jogo e chama proxima cena'''
	while cena < 6:
		print()
		superprint(cena,palavra,erro)		#exibe cena atua+palavra
		letra = entrada(palavra,erro,cena)
		val = busca(resposta,letra)
		
		if val == []:
			cena += 1
			erro.append(letra)
		else:
			for i in val:
				palavra[i] = letra
		if "".join(palavra) == resposta:
			print()
			superprint(cena,palavra,erro)
			return True
	print()
	superprint(cena,palavra,erro)
	return False
		
		
		
def main():
	'''Inicializa e finaliza o game'''
	i = int(input("Escolha um numero entre 0 e 49: "))
	if i > 49 or i < 0:
		print("Numero invalido.")
	else:	
		resposta = lista_palavras[i]
		palavra = ["_" for i in range(len(resposta))]
		O_Jogo = cenario(resposta,palavra)
		
		if O_Jogo:
			print("Palavra encontrada!")
		else:
			print("Palavra oculta:",resposta)
			
main()