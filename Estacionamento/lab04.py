#Programa de controle de entrada e saida de estacionamento
#Maicon Gabriel de Oliveira, ra 221329

#Entrada de dados
c = int(input())#espaço total do estacionamento

n = 1
c0 = c #armazena valor da capacidade inicial

while n!=0:
    n = int(input())#entrada de veiculos
    
    if n>c or c-n>c0:

        #saida de recusa na falta de capacidade
        print("Veiculo muito grande! Capacidade restante:", c)

    else:
        c1 = c #armazena capacidade dentro do looping
        c = c - n #subtrai quantidade de carros da capacidade total

        if c1>c:

            #saida caso haja capacidade
            print("Seja bem-vindo! Capacidade restante:", c)

        elif c1<c:

            #saida da saida de automoveis
            print("Volte sempre! Capacidade restante:", c)


        

    
