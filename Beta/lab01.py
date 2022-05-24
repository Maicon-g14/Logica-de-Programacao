# O programa deve receber distancia e angulo entre duas cidades do globo e imprimir sua circunferencia em estadios e quilometros
#Maicon Gabriel de Oliveira, ra 221329

#Entrada de algoritmos
D = float(input("")) #distancia em estadios
A = float(input(""))#angulo em graus

#Calculo de algoritmos
Ce = (360*D)/A#calculo da circunferencia
Ckm = (Ce*176.4)/1000#transformaçao em quilometros

#Saida de algoritmos
print("%.1f" % Ce)#Saida da circunferencia em estadios
print("%.1F" % Ckm)#Saida da circunferencia em quilometros
