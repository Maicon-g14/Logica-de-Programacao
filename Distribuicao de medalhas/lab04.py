#221329

Couro = float(input())
Cprata = float(input())
Cbronze = float(input())

#num de medalhas
ouro = 0;prata = 0;bronze = 0

maior_nota = 0
nota = 0

while nota != -1:
	nota = float(input())
	if nota > maior_nota:
		maior_nota = nota
	if nota >= Couro:
		ouro += 1
	elif nota >= Cprata:
		prata += 1
	elif nota >= Cbronze:
		bronze += 1

if ouro > 0:
	print("Medalha(s) de ouro: %i" % (ouro))
else:
	print("Nenhum participante recebeu medalha de ouro!")
if prata > 0:
	print("Medalha(s) de prata: %i" % (prata))
else:
	print("Nenhum participante recebeu medalha de prata!")
if bronze > 0:
	print("Medalha(s) de bronze: %i" % (bronze))
else:
	print("Nenhum participante recebeu medalha de bronze!")
print("Maior nota: %.1f" % (maior_nota))
