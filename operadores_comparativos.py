#"Esse programa permite lhe dizer se o valor digitado é positivo ou negativo"
print ("Esse programa permite lhe dizer se o valor digitado é positivo ou negativo")
a = float(input('Qual numero deseja verificar? ').replace(',', '.'))

if a > 0:
    print ('Esse numero é positivo')
elif a == 0:
    print ("Esse numero é neutro")   
else:
    print ('Esse numero é negativo')

             
#'Esse programa verifica se o numero indicado é par ou impar'
print ('Esse programa verifica se o numero indicado é par ou impar')
numero = float(input("Qual numero deseja verificar? "))
result = numero % 2

if result == 1:
    print("Esse numero é impar")
else:
    print('Esse numero é par')   


# 'Esse programa verifica se um ano indicado é bissexto'
print('Esse programa verifica se um ano indicado é bissexto')
a = int(input("Qual ano desejas verificar? "))


if a % 400 == 0:
    print ("O ano é bissexto")
elif a % 4 == 0 and a % 100 != 0:
    print('O ano é bissexto')
else:
    print (' O ano não é bissexto')


# 'Esse programa compreende e responde uma equação de segundo grau 5'

a = float(input('Qual o valor de A? '))
b = float(input('Qual o valor de B? '))
c = float(input('Qual o valor de C? '))

delta = b**2 - 4*a*c

if a == 0:
    print("o valor de A deve ser diferente de 0 para ser considerado uma equação de segundo grau")
elif a != 0:
    x = (-b + (delta**0.5)) / 2*a
    y = (-b - (delta**0.5)) / 2*a
    print ('o valor das raizes são',x,y)
else:
    print('a equação não possui valores reais')

