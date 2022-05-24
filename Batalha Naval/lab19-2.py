#Batalha Naval
#Maicon Gabriel de Oliveira,ra 221329
#Jogo de tabuleiro de dois jogadores, cada jogador deve adivinhar onde estão os navios do oponente e os destruir. Ganha o jogo quem destruir todos os navios do oponente primeiro.


def main():
    lc = input().split("x")     #Entra num de linhas e colunas separando em x
    mat1 = []       #Tabuleiro global do jogador 1
    mat2 = []       #Tabuleiro global do jogador 2
    entrada(lc,mat1,mat2)       #Chama função de leitura e criação de tabuleiros
    atk(mat1,mat2)       #Chama função responsável por receber e realizar ataque em tempo de execução


def entrada(lxc,tab1,tab2):
    '''Recebe o numero de linhas do tabuleiro e os respectivos vazios, criando após cada tabuleiro de um jogador através de uma matriz'''
    for mat in range(2):        #Para 2 tabuleiros
        for linha in range(int(lxc[0])):        #no numero de linhas especificado
            tab = []
            entra = input()     #Entra linha
            for coluna in entra:        #Separa itens em colunas
                tab.append(coluna)
            if mat == 0:        #Se no primeiro tabuleiro
                tab1.append(tab)        #Salva no tabuleiro do jogador 1
            else:
                tab2.append(tab)        #Senao salva no tabuleiro do jogador 2


def atk(tab1,tab2):
    '''Função que realiza entrada de ataque de embarcações'''
    playing = True
    alternancia = 0
    while playing:      #Laço responsável pela entrada enquanto embarcações
        if alternancia%2 == 0:      #Define a alternancia de jogadores com seus tabuleiros invertidos
            player = tab2       #Player 1 ataca, logo usa-se tab2
            j = 1
        else:
            player = tab1       #Player 2 ataca, logo usa-se tab1
            j = 2
        atkPos = input().split(",")     #Lista com coordenadas do ataque, pos[0] = linha e pos[1] = coluna
        try:
            print("Ataque em (%s,%s) do jogador %s" % (atkPos[0],atkPos[1],j))
        except IndexError:
            break
        realizaATK(int(atkPos[0])-1,int(atkPos[1])-1,player)      #Função recursiva que realiza dano e, se for o caso naufraga a embarcação
        mostraTab(player)
        playing = verificaTab(player)     #Função que verifica se ainda há embarcações no tabuleiro
        alternancia = alternancia + 1       #Incrementador de alternancia


def mostraTab(tabuleiro):
    '''Função responsavel por mostrar os elementos do tabuleiro'''
    for x in tabuleiro:
        for y in range(len(x)-1):
            print(x[y],end="")
        print(x[-1])


def realizaATK(linha,coluna,playerTab):
    '''Função recursiva que identifica posição de ataque e, em caso de acerto remove semelhantes adjuntos'''
    try:        #Se a posição buscada for valida
        if playerTab[linha][coluna] == "@":         #Se houver embarcacoes na posição atacada
            playerTab[linha][coluna] = "-"      #Aquela parte da embarcação deixa de existir
            try:  # Testa se existem proximas linhas/colunas nas bordas
                linhaD = playerTab[linha + 1][coluna]
            except IndexError:
                linhaD = playerTab[linha][coluna]
            try:
                if linha > 0:       #Para evitar que a lista seja lida inversamente a subtração só ocorre caso o numero seja maior que 0
                    linhaA = playerTab[linha - 1][coluna]
                else:
                    linhaA = playerTab[linha][coluna]
            except IndexError:      #Caso haja extrapolamento de borda
                linhaA = playerTab[linha][coluna]       #Mante-se a ultima posição
            try:
                if coluna > 0:
                    colunaA = playerTab[linha][coluna - 1]
                else:
                    colunaA = playerTab[linha][coluna]
            except IndexError:
                colunaA = playerTab[linha][coluna]
            try:
                colunaD = playerTab[linha][coluna + 1]
            except IndexError:
                colunaD = playerTab[linha][coluna]

            if linhaA == "-" and linhaD == "-" and colunaA == "-" and colunaD == "-":     #Caso só haja agua nas posições vizinhas o programa retorna
                return
            else:       #Caso haja partes da embarcação no entorno
                if linhaA == "@":       #Testa se há partes da embarcação a esquerda
                    realizaATK(linha-1,coluna,playerTab)        #Caso haja re-chama a função para sua destruição
                if linhaD == "@":       #Testa se há partes da embarcação a direita
                    realizaATK(linha+1,coluna,playerTab)
                if colunaA == "@":       #Testa se há partes da embarcação abaixo
                    realizaATK(linha,coluna-1,playerTab)
                if colunaD == "@":       #Testa se há partes da embarcação acima
                    realizaATK(linha,coluna+1,playerTab)
        else:       #Caso o jogador tenha acertado apenas a agua, retorna
            return
    except IndexError:      #Se a posição for invalida retorna sem fazer nada
        return


def verificaTab(tabuleiro):
    '''Função que verifica se ainda há embarcaçoes no tabuleiro dado e retorna False caso nao haja'''
    for i in tabuleiro:     #Para cada linha do tabuleiro
        try:
            aux = i.index("@")      #Busca por embarcações
            return True     #Se houver, retorna True
        except ValueError:
            pass
    return False        #Senao, retorna False


main()