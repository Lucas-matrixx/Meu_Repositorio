raio = float(input("qual o o numero do raio? "))
circuferencia = "{:.1f}".format ((2*3.14)*raio)
print("a circuferencia do circulo é", circuferencia)
area = "{:.1f}".format  (3.14 * raio**2)
print ("e sua area é ", area)


dfumad = int(input("há quantos anos voce fuma? "))
qcigar = int(input("quantos cigarros voce fuma pro dia "))
oinff = dfumad * 365 * qcigar
entrr = oinff * 10
perdd = "{:.0f}".format (entrr / 60 / 24)
print ("voce morreu",perdd,"dias da sua vida")

# Solicitando ao usuário a quantidade de cigarros fumados por dia
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))

# Solicitando ao usuário h5á quantos anos ele fuma
anos_fumando = int(input("Há quantos anos você fuma? "))

# Calculando o total de cigarros fumados
total_cigarros = cigarros_por_dia * anos_fumando * 365

# Calculando a redução de tempo de vida (10 minutos por cigarro)
minutos_perdidos = total_cigarros * 10

# Convertendo os minutos perdidos em dias (1440 minutos em um dia)
dias_perdidos = minutos_perdidos / 1440

print(f"O tempo de vida perdido é de aproximadamente {dias_perdidos:.0f} dias.")


a = float(input("valor de A "))
b = float(input("valor de B "))
c = float(input("valor de C "))

delta = b**2 - 4*a*c
if a == 0:
  print ("não se trata de uma equação de segundo grau")
elif delta > 0:
  x1 = (-b+delta**0,5) / (2/a)
  x2 = (-b-delta**0,5) / (2/a)
  print("as raizes são", x1, "e", x2)
elif delta == 0:
  x1 =-b/ (2*a)
  print("a unica raiz é", x1)
else:
  print("não tem raizes reais")
