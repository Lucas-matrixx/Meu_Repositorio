#Faça um algoritmo que mostre a tabuada de um número qualquer digitado pelo usuário.
number = int(input('Qual tabuada voce quer visualizar '))
i = 0

while i!=9:
    i = i+1
    result = number * i
    print(number,'x',i,'=',result)

for i in range(1,10):
    print(number,'x',i,'=',number*i)

#Crie um programa que some todos os números inteiros de 1 a 100 e mostre o resultado da soma na tela:
i=0
for y in range (1,101):
    i=i+y
print(i)

#Crie um programa que calcule e mostre na tela o valor da expressão: 2 + 4 + 6 + 8 + ... 998 + 1000 (= 250500)
index = 0
for i in range(2,1001,2):
    index = index +i
    
print(index)