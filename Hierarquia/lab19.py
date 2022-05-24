#Hierarquia
#Maicon Gabriel de Oliveira,ra 221329
#Usando recursividade, dada uma matriz que descreve a hierarquia de uma empresa, encontra-se e mostra a cadeia hierárquica relativa a um determinado funcionário.

def main():
    entrada1 = input()      #Entrada da primeira linha com numero de linhasXcolunas e superior a buscar
    entrada = entrada1.split(" ")
    lista = entra_loop(int(entrada[0]),[])      #Chama função de entrada de linhas subsequente e devolução de matriz

    resp = []
    acha1(lista[int(entrada[1])], 0, lista,resp)        #Chama função de procura de subordinados
    if resp == []:
        print(int(entrada[1]))
    else:
        print(int(entrada[1]), end=" ")  # Mostra numero do primeiro superior
    ordena(resp)        #Chama função de ordenação
    mostra(resp,0)      #Chama função de amostragem
    if resp != []:
        print(resp[-1])     #Exibe ultima posição

    #Colocar primeiro valor em lista para caso nao houver rasultados nao haver problema do espaço


def mostra(resp,aux):
    '''Recebe a lista de valores ordenada e mostra na tela por recursividade'''
    if aux >= len(resp)-1:      #Compara se a posição é valida e declara amostragem até o penultimo termo
        return
    else:
        print(resp[aux],end=" ")
        mostra(resp,aux+1)


def entra_loop(nEntra,lista):
    '''recursao para entrada de valores, recebe o numero de linhas, oferece a entrada e transforma valores em matriz'''
    if nEntra <= 0:     #Segundo o numero de linhas entrado, enquanto houverem linhas faltando a recursao continua
        return lista
    else:
        aux = input()
        linha = aux.split(" ")      #Separa numeros entrados no espaço entre eles
        lista.append(linha)
        return entra_loop(nEntra-1,lista)       #vai para proxima posição


def ordena(lista):        #lista,contador desde 0, contador desde 1
    '''Recebe a lista de subordinados e a ordena  antes de exibi-la'''
    for i in range(len(lista)):
        for j in range(len(lista)):         #Utilizando combinaçoes
            if lista[j] > lista[i]:         #Caso posição anterior for maior que posterior
                a,b =lista[i],lista[j]      #Inverte posiçoes
                lista[j]=a;                lista[i]=b


def acha1(lSup,pos,lista,resp):
    '''Recebendo a linha de um superior, busca por seus subordinados e exibe suas posiçoes'''
    if pos >= len(lSup):        #Se a posição buscada nao existir, retorna a posição atual
        return
    else:
        if lSup[pos] == '1':  # Se na posição atual houver relação subordinado
            resp.append(pos)
            acha1(lista[pos],0,lista,resp)
        acha1(lSup,pos+1,lista,resp)     #Senão repete a busca até acabar a linha


main()