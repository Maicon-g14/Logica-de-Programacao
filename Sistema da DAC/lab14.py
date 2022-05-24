#Sistema da DAC
#Sistema de gerenciamento de turmas da DAC capaz de realizar operações como impressão, ordenação, inclusão, remoção e busca de alunos matriculados em cada turma.
#Maicon Gabriel de Oliveira, 221329



def Imprimir(listaRA):
    '''deve imprimir a lista de RAs de alunos matriculados em seu estado atual'''
    if listaRA != []:   #so imprime caso houver valores na lista
        for i in range(len(listaRA)):
            print(listaRA[i],end=" ")
        print()
    return


def Ocrescente(listaRA):
    '''orderna RAs dos alunos em ordem crescente'''
    listaRA.sort()
    return


def Odecrescente(listaRA):
    '''ordena RAs dos alunos em ordem decrescente'''
    listaRA.sort(reverse=True)
    return


def BuscaBinaria(entrada,listaRA):
    '''A busca binária deve imprimir o índice de busca para cada passo do algoritmo e o índice final, caso o RA tenha sido encontrado ou uma mensagem de erro, caso contrário. Se a lista não estiver ordenada ao realizar a busca, uma mensagem de erro deve ser impressa.'''
    lista_temp = listaRA[:] #atribui a nova lista para verificar se esta ordenada
    lista_temp.sort()
    ord_cres = Compara_listas(lista_temp, listaRA)
    lista_temp.sort(reverse=True)
    ord_decres = Compara_listas(lista_temp, listaRA)
    if not ord_cres and not ord_decres:
        print("Vetor nao ordenado!")
        return
    elif ord_cres: #Caso a ordenação seja crescente
        i = 0
        f = len(listaRA)-1
        while i <= f:
            meio = (i+f)//2
            print(meio, end=" ")
            if listaRA[meio] == entrada[0]:
                print()
                print("%d esta na posicao: %d" % (entrada[0], meio))
                return
            elif listaRA[meio] > entrada[0]:
                f = meio - 1
            else:
                i = meio + 1
    elif ord_decres:    #Caso a ordenação seja decrescente
        i = 0
        f = len(listaRA) - 1
        while i <= f:
            meio = (i + f) // 2
            print(meio, end=" ")
            if listaRA[meio] == entrada[0]:
                print()
                print("%d esta na posicao: %d" % (entrada[0], meio))
                return
            elif listaRA[meio] > entrada[0]:
                i = meio + 1
            else:
                f = meio - 1
    print()
    print("%d nao esta na lista!" % (entrada[0]))
    return



def Inserir(entrada,listaRA):
    '''A inserção deve ser feita de modo que a ordenação seja mantida, ou seja, se a lista tiver sido ordenada antes da inserção, o valor inserido deve ficar na posição correta e a lista deve ser atualizada. Se a lista não tiver sido ordenada antes da inserção, o aluno é inserido ao final da lista. Caso o limite máximo de alunos seja atingido (150 alunos), uma mensagem de erro deve ser impressa ao invés de inserir o aluno na turma. Caso o aluno a ser inserido já esteja matriculado na turma, uma mensagem deve ser impressa.'''
    lista_temp = listaRA[:] #atribui a nova lista para verificar se esta ordenada
    lista_temp.sort()
    ord_cres = Compara_listas(lista_temp,listaRA)
    lista_temp.sort(reverse=True)
    ord_decres = Compara_listas(lista_temp,listaRA)
    Na_lista = Busca(listaRA, entrada)
    if len(listaRA) >= 150:
        print("Limite de vagas excedido!")
    elif Na_lista is not None:
        print("Aluno ja matriculado na turma!")
    elif not ord_cres and ord_decres and len(listaRA) < 150:
        x = entrada[0]
        listaRA.append(x)
        listaRA.sort(reverse=True)
    elif ord_cres and not ord_decres and len(listaRA) < 150:
        x = entrada[0]
        listaRA.append(x)
        listaRA.sort()
    elif not ord_cres and not ord_decres and len(listaRA) < 150:
        x = entrada[0]
        listaRA.append(x)

    return



def Remover(entrada,listaRA):
    '''A remoção não pode ser realizada se não tiver alunos matriculados na disciplina, assim, uma mensagem de erro deve ser impressa. Caso o aluno não esteja matriculado na disciplina, também deve-se imprimir uma mensagem de erro.'''
    if listaRA == []:
        print("Nao ha alunos cadastrados na turma!")
        return
    busca = Busca(listaRA,entrada)
    if busca is None:
        print("Aluno nao matriculado na turma!")
        return
    listaRA.remove(listaRA[busca])
    return


def Compara_listas(lista_temp,listaRA):
    '''Compara caracteres de uma lista dada com outra retornando True se são iguais ou False caso nao seja a mesma ordenação'''
    for i in range(len(lista_temp)):
        if lista_temp[i] != listaRA[i]:
            return False
    return True


def Busca(listaRA,entrada):
    '''Busca objeto dado em outra lista, caso nao aja retorna None, senao a posição do objeto'''
    for i in range(len(listaRA)):
        if listaRA[i] == entrada[0]:
            return i
    return None

def prep_lista(entrada,letra):
    '''ao receber entrada com letra da função correspondente, essa função retira essa letra'''
    entrada.remove(letra)
    entrada = [int(i) for i in entrada]
    return entrada


def main():
    Entra_RA = True
    listaRA = []
    while len(listaRA) < 151:
       entra = input()
       entrada = [str(i) for i in entra.split()]
       if Entra_RA and entrada[0] != "p" and entrada[0] != "c" and entrada[0] != "d" and entrada[0] != "b" and entrada[0] != "i" and entrada[0] != "r" and entrada[0] != "s":
           listaRA = [int(i) for i in entra.split()]
           Entra_RA = False
           continue

       elif entrada[0] == "s":
           break

       elif entrada[0] == "p":
           Imprimir(listaRA)

       elif entrada[0] == "c":
           Ocrescente(listaRA)

       elif entrada[0] == "d":
           Odecrescente(listaRA)

       elif entrada[0] == "b":
           entrada = prep_lista(entrada, "b")
           BuscaBinaria(entrada,listaRA)

       elif entrada[0] == "i":
           entrada = prep_lista(entrada, "i")
           Inserir(entrada,listaRA)

       elif entrada[0] == "r":
           entrada = prep_lista(entrada, "r")
           Remover(entrada,listaRA)


main()