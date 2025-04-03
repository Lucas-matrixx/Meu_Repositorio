

nomepet = 'sufutus'
print(nomepet)
print(type(nomepet))

#Faça um programa em Python que converta dólares em reais.
dolar = float(input('Qual o valor em dolares?').replace(',','.'))
reais = dolar * 5.65
print(f'O valor convertido é de R$ {reais:.2f}')

#Faça um programa que calcule a área de um retângulo e seu perímetro com base em seus dois lados.
area = float(input('qual o valor do lado1? '))
area2 = float(input('qual o valor do lado2? '))
perimetro = 2 * (area * area2)
print(f'A medida do perimetro é {perimetro:.0f}M²')

#Faça um programa que converta a temperatura de graus Celsius para graus Fahrenheit.
index = float(input('Qual a temperatura em graus Celsius? ').replace(',','.'))
convert = (9/5 * index) + 32
print('A temperatura de ',index,f'°C equivale a {convert:.1f} °F')

#Faça um programa que converta a temperatura de graus Fahrenheit para graus Celsius.
ffahrein = float(input('Qual a temperatura em Fahrenheit? ').replace(',','.'))
result = 5/9 * (fahrein-32)
print(f'A temperatura de {fahrein:.1f}°f',f'é igual a {result:.1f}°C')

#Crie um programa que leia um número e diga se ele é positivo ou negativo.
number = float(input('Qual numero deseja verificar? '))
if number >= o:
    print('esse numero é positivo')
else:
    print('esse numero é negativo')

#Crie um programa que leia um número e diga se ele é positivo ou negativo.
number = float(input('Qual numero deseja verificar? ').replace(',','.'))
if number > 0:
    print('esse numero é positivo')
elif number == 0:
    print('Calma moreno, o numero 0 é não é nenhum dos dois')
else:
    print('Esse numero é negativo')

#Crie um programa que leia um número inteiro e diga se ele é par ou ímpar.
num = float(input('Qual numero deseja verificar? '))
if num % 2 == 0:
    print("Esse numero é par")
else:
    print('Esse numero é impar')

#Escreva um programa que calcule e mostre as raízes reais de uma equação de segundo grau (a.x² + b.x + c = 0), com base nos valores de a, b e c.
ax = float(input('Qual o valor de A '))
bx = float(input('Qual o valor de B '))
cx = float(input('Qual o valor de C '))

delta = cx**2 - 4*ax*cx
if ax == 0:
    print('Error404 | Ax deve ter um valor difernete de 0')
elif delta > 0:
    x1 = (-b+delta**0.5) / (2*ax)
    x2 = (-b+delta**0.5) / (2*ax)
    print('As raizes são', x1,'e',x2)
elif delta == 0:
    x1 = -b/(2*ax)
    print('A raiz é',x1)
else:
    print('nao tem raizes reais')
    