#ra221329

n = int(input())
lista = []

hasht = 0
emotic = 0

for i in range(n):
	entra = input()
	if entra.isdigit() or (entra[1:].isdigit() and entra[0] == "-"):
		print(entra)
	elif entra.isalpha():
		print(entra)
	else:
		if entra[0] == "#" and (entra[1:].isdigit() or entra[1:].isalpha()):
			hasht += 1
		else:
			emotic += 1

if hasht == 1:
	print("1 hashtag foi removida.")
elif hasht > 1:
	print(hasht,"hashtags foram removidas.")
if emotic == 1:
	print("1 emoticon foi removido.")
elif emotic > 1:
	print(emotic,"emoticons foram removidos.")
