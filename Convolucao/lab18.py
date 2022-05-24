#Convolucao de imagens
#Maicon Gabriel de Oliveira, ra 221329
#A operacao de convolucao recebe como parametros uma matriz correspondente a uma imagem e aplica o efeito de convolucao nessa imagem
import sys

def CarregaArq(num,DeM):
    '''Função responsavel por carregar os arquivos 1 e 2 e devolve-los como matriz'''
    try:
        l = []
        arquivo = open(sys.argv[num], mode='r', encoding='utf-8')     #Abre o arquivo
        for s in arquivo.readlines():       #Para cada um das linhas
            k = s.replace("\n","")      #substitui-se \n por ""
            j = k.split(" ")        #Separa-se os componentes da lista em outra lista
            try:
                on = True
                while on:
                    j.remove("")    #Se houver remove locais com "" enquanto existirem
            except ValueError:
                pass
            l.append(j)     #Adiciona lista de colunas em um lista de linhas criando uma matriz l
        arquivo.close()
        if DeM:     #Caso esteja no segundo arquivo
            D = achaDeM(l,True)     #Encontra divisor
            M = achaDeM(l,False)        #Encontra a matriz de convolução
            return (D,M)
        return l

    except FileNotFoundError:
        print("Arquivo %s nao encontrado" %(num))


def achaDeM(arq,D):
    '''Função responsavel por retornar os valores do divisor e da matriz de convolução'''
    if D:
        return arq[0][0]        #Pega o divisor da matriz
    del arq[0]      #Apaga a posicao do divisor deixando so a matriz de convolução
    return arq


def achaMeN(img):
    '''Função responsavel por pegar e retornar os tamanhos m e n da matriz'''
    m = img[1][0]       #Pega o tamanho m da matriz
    n = img[1][1]       #Pega o tamanho n da matriz
    return (m,n)


def convolucao(imagem,m,n,D,M):
    '''Função responsavel pelo calculo da convolucao e retorno da matriz imagem ja convolucionada'''
    a = int(M[0][0])        #Atribuição dos valores da matriz nucluo a suas respectivas variaveis
    b = int(M[1][0])
    c = int(M[2][0])
    d = int(M[0][1])
    e = int(M[1][1])
    f = int(M[2][1])
    g = int(M[0][2])
    h = int(M[1][2])
    i = int(M[2][2])
    out = []
    for z in imagem:        #Cria copia da matriz principal para armazenar valores novos nela
        out.append(z[:])
    for x in range(n):
        for y in range(m):
            if x==0 or x==n-1 or y==0 or y==m-1:        #Ignora bordas da matriz imagem
                continue
            out[x][y] = ((a*int(imagem[x - 1][y - 1]))+(b*int(imagem[x][y - 1]))+(c*int(imagem[x + 1][y - 1]))+(d*int(imagem[x - 1][y]))+(e*int(imagem[x][y]))+(f*int(imagem[x + 1][y]))+(g*int(imagem[x - 1][y + 1]))+(h*int(imagem[x][y + 1]))+(i*int(imagem[x + 1][y + 1])))/D  # Formula de convolução
            if int(out[x][y]) > 255:        #Arredonda valores superiores para seus limites mais proximos
                out[x][y] = 255
            elif int(out[x][y]) < 0:
                out[x][y] = 0
            else:
                out[x][y] = int(out[x][y])      #Transfoma valores recebidos em float para inteiro
    return out


def saida(img):
    '''Função geradora da saida do programa em formato de uma nova matriz como especificado'''
    try:
        arquivo = open(sys.argv[1], mode='r', encoding='utf-8')     #Abre o arquivo novamente
        matriz = arquivo.readlines()        #Lê o arquivo inteiro
        arquivo.close()
        for i in range(3):
            print(matriz[i],end='')        #Mostra as 3 primeiras linhas(cabeçalho) da matriz
        for j in range(len(img)):
            for k in range(len(img[j])):
                print(img[j][k],end=' ')        #Mostra a nova matriz gerada
            print(" \n",end='')     #Acrescentando o \n no final de cada linha
    except FileNotFoundError:
        print("Arquivo 1 nao encontrado")


img = CarregaArq(1,False)
MeN = achaMeN(img)
m = int(MeN[0])
n = int(MeN[1])
for i in range(3):
    del img[0]
DeM = CarregaArq(2,True)
D = int(DeM[0])
M = DeM[1]
newmat = convolucao(img,m,n,D,M)
saida(newmat)