#ra 221329

#Entra num Int multiplo de 5
entrada_full = int(input())	
entrada = entrada_full / 100

#100 reais
num_notas = entrada // 100
print(int(num_notas), "nota(s) de R$ 100,00.")
total = num_notas*100

#50 reais
resto = entrada % 100
num_notas = resto // 50
print(int(num_notas), "nota(s) de R$ 50,00.")
total = ((num_notas*50) + total) 

#20 reais
resto = resto % 50
num_notas = resto // 20
print(int(num_notas), "nota(s) de R$ 20,00.")
total = ((num_notas*20) + total) 

#10 reais
resto = resto % 20
num_notas = resto // 10
print(int(num_notas), "nota(s) de R$ 10,00.")
total = ((num_notas*10) + total) 

#5 reais
resto = resto % 10
num_notas = resto // 5
print(int(num_notas), "nota(s) de R$ 5,00.")
total = ((num_notas*5) + total) 

#2 reais
resto = resto % 5
num_notas = resto // 2
print(int(num_notas), "nota(s) de R$ 2,00.")
total = ((num_notas*2) + total) 

#1 real
resto = resto % 2
num_notas = resto // 1
print(int(num_notas), "moeda(s) de R$ 1,00.")
total = ((num_notas*1) + total) 

entrada = (entrada_full - (total*100))
#print(entrada)

#50 centavos
resto = entrada
num_notas = resto // 50
print(int(num_notas), "moeda(s) de R$ 0,50.")

#25 centavos
resto = resto % 50
num_notas = resto // 25
print(int(num_notas), "moeda(s) de R$ 0,25.")

#10 centavos
resto = resto % 25
num_notas = resto // 10
print(int(num_notas), "moeda(s) de R$ 0,10.")

#5 centavos
resto = resto % 10
num_notas = resto // 5
print(int(num_notas), "moeda(s) de R$ 0,05.")

