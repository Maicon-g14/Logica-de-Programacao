#Sudoku
#Maicon Gabriel de Oliveira, 221329
#Atraves de uma funcao recursiva resolve-se um determinado jogo de Sudoku
#!/usr/bin/env python3

# Funcao: print_sudoku
# Essa funcao ja esta implementada no arquivo lab20_main.py
# A funcao imprime o tabuleiro atual do sudoku de forma animada, isto e,
# imprime o tabuleiro e espera 0.1s antes de fazer outra modificacao.
# Voce deve chamar essa funcao a cada modificacao na matriz resposta, assim
# voce tera uma animacao similar a apresentada no enunciado.
# Essa funcao nao tem efeito na execucao no Susy, logo nao ha necessidade de
# remover as chamadas para submissao.
from lab20_main import print_sudoku

# O aluno pode criar outras funcoes que ache necessario

# Funcao: resolve
# Resolve o Sudoku da matriz resposta.
# Retorna True se encontrar uma resposta, False caso contrario
def resolve(resposta):
    # Implementar a funcao e trocar o valor de retorno
    sudoku = []
    for i in resposta:      #Copia lista original
        sudoku.append(i[:])
    fim = main_recursivo(resposta,0,0,sudoku)      #Funcao recursiva do sudoku
    print_sudoku(resposta)
    return fim

def gera3x3(lista,num,num2):
    '''Entra com copia da lista principal e numero da coluna buscada,arredonda-se o valor e gera mini lista 3x3 conforme necessidade'''
    if num <= 2:
        num = 0
    elif num >= 3 and num <=5:
        num = 3
    elif num >= 6:
        num = 6
    if num2 <= 2:
        num2 = 0
    elif num2 >= 3 and num2 <=5:
        num2 = 3
    elif num2 >= 6:
        num2 = 6
    min33 = []
    for x in range(3):
        for y in range(3):
            min33.append(lista[x+num][y+num2])
    return min33

def geraCol(sudoku,col):
    '''Dado o valor coluna de um numero, gera e retorna toda a coluna desse numero em uma lista'''
    cols = []
    for i in range(9):
        cols.append(sudoku[i][col])
    return cols

def pos_possiveis(tam,linha,coluna,quad,livre):
    '''Essa recursao dada uma posicao acha possiveis numeros levando em consideracao os numeros da linha,coluna e quadrado 3x3 atual.
    Cada numero ja existente e removido de uma lista de possibilidades que e retornada depois'''
    if tam >= 9:        #Se passadas 9 interacoes, percorreu toda linha/coluna/quadrado do sudoku
        return livre        #Retorna posicoes disponiveis recursao acima
    else:
        if linha[tam] != 0:
            if linha[tam] in livre: livre.remove(linha[tam])        #Na linha remove numero ja existente da lista de possibilidades
        if coluna[tam] != 0:
            if coluna[tam] in livre: livre.remove(coluna[tam])        #Na coluna remove numero ja existente da lista de possibilidades
        if quad[tam] != 0:
            if quad[tam] in livre: livre.remove(quad[tam])      #No quadrado remove numero ja existente da lista de possibilidades
        pos_possiveis(tam+1,linha,coluna,quad,livre)
        return livre        #Retorna posicoes disponiveis

def main_recursivo(sudoku,posL,posC,resposta):
    '''Funcao recursiva principal. Dado o tabuleiro, procura sua resolucao por recursao e retorna True caso exista ou False caso sua resposta nao exista'''
    #---------------Mantem a recursao correndo pelas posicoes-----------------
    if posC >= 9:                                   #Faz a troca de linha quando chega a coluna final
        posL += 1;        posC = 0
    if posL >= 9:                               #Caso chegue ao final da ultima linha manda sinal de retorno e saida
        return True
    while resposta[posL][posC] != 0:        #Ignora posicoes fixas enquanto existirem
        posC += 1
        if posC >= 9:                                   #Faz a troca de linha quando chega ao final
            posL += 1;            posC = 0
        if posL >= 9:                               #Caso chegue ao final do tabuleiro(por existir numeros fixos la) inicia retorno
            return True
    #-------------------------Busca a poscao------------------------
    pos_livres = pos_possiveis(0, sudoku[posL], geraCol(sudoku, posC), gera3x3(sudoku, posL, posC), [i for i in range(1,10)])       #Recursao de busca de posicoes livres
    #-----------------------Condicao de Retorno------------------------
    if pos_livres == []:                    #Caso nao haja numeros livres
        if resposta[posL][posC] == 0:               #Se a posicao nao for de numero fixo
            sudoku[posL][posC] = 0                  #Zera a posicao
            print_sudoku(sudoku)
        return                             #Somente faz rodar lista de possiveis anteriores no for
    # -----------------------Testa as posicoes encontradas------------------------
    for cada_pos_livre in pos_livres:               #Para cada possivel solucao
        if resposta[posL][posC] == 0:                   #Se nao for um numero fixo
            sudoku[posL][posC] = cada_pos_livre             #Substitui a posicao
            print_sudoku(sudoku)
        fim = main_recursivo(sudoku, posL, posC+1,resposta)             #Chama proxima posicao
        if fim:                     #Caso esteja em retorno de saida, continua ele
            return True
    if resposta[posL][posC] == 0:       #Se a posicao nao for fixa
        sudoku[posL][posC] = 0              #Zera valor
        print_sudoku(sudoku)
    return      #Esse return faz voltar 1 pos na coluna ou subir linha dependendo do caso