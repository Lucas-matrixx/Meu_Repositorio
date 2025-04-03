#Faça um algoritmo que mostre a tabuada de um número qualquer digitado pelo usuário.
number = int(input('Qual tabuada voce quer visualizar '))
i = 0

while i!=9:
    i = i+1
    result = number * i
    print(number,'x',i,'=',result)


print('feito com for')
for i in range(1,10):
    print(number,'x',i,'=',number*i)

