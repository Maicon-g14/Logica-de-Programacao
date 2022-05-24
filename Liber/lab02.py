#Programa de calculo do StarUber
#Maicon Gabriel de Oliveira, ra 221329

#Entrada de caracteres
vi = int(input())#Pagamento inicial
xi = int(input())#Coordenada X inicial
yi = int(input())#Coordenada Y inicial
xf = int(input())#Coordenada X final
yf = int(input())#Coordenada Y final
t = int(input())#Taxa por unidade de distancia
cd = int(input())#Valor do cupom de desconto
pr = int(input())#Pontuaçao do passageiro

#Processamento do Valor
if xf >= xi and yf >= yi:
    d = (xf - xi) + (yf - yi)#Calculo da distancia
    VC = vi + (d*t)#Calculo do valor da corrida
    VD = max(cd, (VC * pr/100))#Calculo do valor do desconto
    VF = VC - VD#Calculo do valor final

#Impressao de resultado
print("%.2f" % VF)
