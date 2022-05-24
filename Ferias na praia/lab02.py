#ra 221329

#Entrada das notas
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

#Entrada das ferias
ferias1 = input()
ferias2 = input()

#Entrada do 13o
dt1 = int(input())
dt2 = int(input())

#Entrada hotel+passagem
trivag = float(input())
passa = float(input())

if (nota1>=7) and (nota2>=7) and (nota3>=7):
	if (ferias1=='Sim') and (ferias2=='Sim'):
		if (dt1 < 11) or (dt2 < 11):
			if (trivag + passa <= 10000.00):
				print("SIM!!!")
			else:
				print("NAO. O valor total e muito alto.")
		else:
			print("NAO. Nenhum 13o salario foi liberado a tempo.")
	else:
		print("NAO. O casal nao esta de ferias.")		
else:
	print("NAO. As notas da Carla nao foram suficientes.")

