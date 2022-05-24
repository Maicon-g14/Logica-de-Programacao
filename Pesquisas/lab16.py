#Engine de buscas
#Engine que busca as possíveis páginas de interesse do usuário segundo termos de busca e apresenta seus resultados
#Maicon Gabriel de Oliveira, ra 221329

#  Funcao: removePalavras
# 
#  Parametros:
#    s: string contendo o texto de entrada
#    vs: vetor de strings com as palavras a serem removidas
# 
#  Descricao:
#    Deve-se remover as palavras de s que estiverem listadas em vs.
#    Ao final, s nao deve conter espacos extras.
#
# Retorno:
#   string s sem as palavras de vs.

def removePalavras(s, vs):
    s = s.split() #copia e transforma string em lista para manipulação
    for j in vs:    #Para cada uma das palavras a serem removidas
        error = False
        while not error:    #Enquanto houver a palavra buscada na lista
            k = s.index(j) if j in s else -1    #procura se cada elemento esta contido na lista e retorna posição, senao -1
            if k != -1: #se estiver na lista
                retira = s[k]
                s.remove(retira)   #retira-se aquela posição de s
            else:   #se nao houver a palavra na lista sai do laço
                error = True
    s = ' '.join([str(i) for i in s])  #retorna s ao estado de string e retorna a lista s
    return s

# Parametros:
#   paginas: lista de strings cada uma representando uma pagina
#   termosBusca: lista de strings com os termos a serem buscados
#
# Descricao:
#	Deve verificar se cada página em paginas contém todos os termos
#	de busca em termosBusca. Se a paginas[i] contiver todos os termos
#	então deve-se atribuir 1 para resp[i] e 0 caso não contenha pelo
#	menus um dos termos de busca.
#
# Retorno:
#   lista a ser preenchida como resposta, de dimensao numPag.

def pagsResposta(paginas, termosBusca):
    resp = []
    for i in paginas:   #para cada uma das paginas
        posicoes = []
        dados = i.split()   #separa-se frases em palavras
        for j in termosBusca: #para cada uma das palavras a serem eliminadas
            k = dados.index(j) if j in dados else -1    #encontra-se sua posição ou retorna -1 se nao existir
            if k != -1: #caso exista o termo de busca na frase
                posicoes.append(k)  #armazena-se suas posições em um vetor
        if len(posicoes) == len(termosBusca):    #se o vetor tiver o mesmo tamanho dos itens a serem buscados, ou seja, contiver todos
            resp.append(1)  #define-se 1 ao laço
        else:
            resp.append(0)  #senao 0
    return resp

# Parametros:
#   links: matriz quadrada binária representando links entre as paginas 
#   resp: vetor obtido apos execucao de pagsResposta
#
# Descricao:
#   Deve-se preencher uma lista numLinks da seguinte maneira: para cada
#   posicao i (0 <= i < numPags), se resp[i] == 1, então numLinks[i] deve conter
#   o numero de links de outras paginas resposta para i. Caso resp[i] == 0,
#   entao numLinks[i] deve ser -1.
#
# Retorno
#   lista numLinks a ser preenchida como resposta, de tamanho numPag

def linksResposta(links,resp):
    numLinks = []
    for i in range(len(links)): #No tamanho numPag
        soma = -1   #Define-se a soma como nao encontrada
        for j in range(len(resp)):  #No tamanho das respostas = numpag
            if resp[i] == 1:    #Se os links existirem para i
                if resp[j] == 1:    #Confere-se se existe para j
                    if soma == -1:  #Caso tenha chegado aqui a soma existe
                        soma = 0    #Então zera-se a soma para nao interferir
                    soma = soma + links[j][i]   #Soma-se os links que direcionam a pagina atual
        numLinks.append(soma)   #adiciona-se a lista os resultados
    return numLinks