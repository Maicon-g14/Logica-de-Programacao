#Programa de calculo de media
#Maicon Gabriel de Oliveira, ra 221329

#entrada de notas
p1 = float(input())
p2 = float(input())
ml = float(input())

#calculo da media ponderada
mp  = ((2*p1)+(3*p2))/5
#calculo da media preliminar
mpre = ((3*mp)+(2*ml))/5
#calculo da media antes do exame
if mp<5 or ml<5:
    m = min(mpre,4.9)
else:
    m = mpre
#calculo da nota final
if m>=2.5 and m<5:
    e = float(input())#caso necessario entra-se a nota do exame
    f = min(5.0,(m+e)/2)
else:
    f = m

#saida de resultados
print("%.1f" % mp)
print("%.1f" % mpre)
print("%.1f" % m)
print("%.1f" % f)
