#Laboratório de conjuntos
#Uma biblioteca de funções em Python para realizar operações sobre conjuntos de números naturais,entra-se com a operação desejada e seus numeros e se obtem a operação pronta.
#Maicon Gabriel de Oliveira, ra 221329


#!/usr/bin/env python3
#unido = []
# Funcao: pertence
#
# Parametros:
#   conj: vetor contendo o conjunto de entrada
#    num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se num pertence a conj e False caso contrario
#
def pertence(conj, num): #dado um vetor e um numero, retorna se ele pertence ou nao ao vetor
    for i in conj:
        if i == num:
            return True
    return False

# Funcao: contido
#
# Parametros:
#   conj1: vetor contendo um conjunto de entrada
#   conj2: vetor contendo um conjunto de entrada
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#
def contido(conj1, conj2):
    if len(conj2) >= len(conj1):                     #Verificar se conjuntos iguais podem se aplicar em continencia
        for i in conj1:     #Para cada elemento do menor conjunto
            esta_la = False     #É pré-definido que nao esta contido
            for j in range((len(conj2))):   #Para todas as posiçoes do maior conjunto
                if i == conj2[j]:       #Testa-se se o numero ja é existente
                    esta_la = True      #Existindo define-se que sim
            if not esta_la:     #Caso aquele numero do conjunto menor nao pertença ao maior o conjunto nao pode estar contido no outro
                return False
        return True     #Senao existindo todos volta True
    return False

# Funcoes: adicao e subtracao
#
# Parametros:
#   conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
def adicao(conj, num):  #adiciona o numero se ja nao estiver no vetor
    if conj == []:
        conj.append(num)
        return
    for i in conj:
        if i == num:
            return
    conj.append(num)
    return

def subtracao(conj, num):   #subtrai o numero dado do vetor se este estiver la
    if conj == []:
        return
    for i in conj:
        if i == num:
            conj.remove(num)
            return
    return

# Funcoes: uniao, intersecao e diferenca
#
# Parametros:
#     conj1: vetor contendo o conjunto de entrada do primeiro operando
#     conj2: vetor contendo o conjunto de entrada do segundo operando
#
# Retorno:
#   Vetor contendo o conjunto de saida/resultado da operacao
#
def uniao(conj1, conj2):    #une dois vetores ignorando numeros repetidos
    unido = []
    if unido == []:
        if conj1 != []:
            unido.append(conj1[0])
        elif conj2 != []:
            unido.append(conj2[0])
    ignora_repetidos(conj1,unido)
    ignora_repetidos(conj2,unido)
    return unido

def ignora_repetidos(conj,unido):   #Função que define se um nnumero ja e ou nao contido no vetor dado
    for i in conj:
        k = unido.index(i) if i in unido else -1
        if k == -1:
            unido.append(i)

def intersecao(conj1, conj2):   #Compara e retorna mesmos valores contidos em ambos os vetores se existirem
    nao_ta = []
    for i in conj2:
        for j in conj1:
            if i == j:
                if nao_ta == []:
                    nao_ta.append(i)
                else:
                    for k in nao_ta:
                        if k == i:
                            break
                    nao_ta.append(i)
    return nao_ta


def diferenca(conj1, conj2):    #Compara e se existir retorna os valores diferentes entre os vetores dados
    ja_ta = []
    for i in conj1:
        esta_la = False
        for j in conj2:
            if i == j:
                esta_la = True
                break
        if not esta_la:
            ja_ta.append(i)
    return ja_ta

def uniao_disjunta(conj1, conj2):   #Retorna valores nao contidos em ambos os vetores quando comparados entre sí
    novo_conj = []
    d1 = diferenca(conj1,conj2)
    d2 = diferenca(conj2,conj1)
    if d1 != []:
        for i in d1:
            k = d2.index(i) if i in d2 else -1
            if k == -1:
                novo_conj.append(i)
    else:
        for i in d2:
            k = d1.index(i) if i in d1 else -1
            if k == -1:
                novo_conj.append(i)
    return novo_conj