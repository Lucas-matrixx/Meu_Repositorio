
'''
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
'''

import pygame
pygame.init()
tela = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Teste do Pygame")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()


import pygame
import time
import random

# Inicializar o pygame
pygame.init()

# Configurações do jogo
largura = 600
altura = 400
tamanho_celula = 20
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Tela do jogo
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

# Função do jogo
def jogo():
    fim_de_jogo = False
    sair = False

    x1 = largura / 2
    y1 = altura / 2
    delta_x = 0
    delta_y = 0

    velocidade = tamanho_celula
    cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura - tamanho_celula) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_celula) / 20.0) * 20.0

    relogio = pygame.time.Clock()

    while not sair:
        while fim_de_jogo:
            tela.fill(preto)
            fonte = pygame.font.SysFont(None, 35)
            mensagem = fonte.render('Fim de Jogo! Pressione C para Continuar ou Q para Sair.', True, branco)
            tela.blit(mensagem, [largura / 6, altura / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sair = True
                        fim_de_jogo = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    delta_x = -tamanho_celula
                    delta_y = 0
                elif event.key == pygame.K_RIGHT:
                    delta_x = tamanho_celula
                    delta_y = 0
                elif event.key == pygame.K_UP:
                    delta_x = 0
                    delta_y = -tamanho_celula
                elif event.key == pygame.K_DOWN:
                    delta_x = 0
                    delta_y = tamanho_celula

        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            fim_de_jogo = True

        x1 += delta_x
        y1 += delta_y
        tela.fill(preto)
        pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho_celula, tamanho_celula])
        corpo_cobra = []
        corpo_cobra.append(x1)
        corpo_cobra.append(y1)
        cobra.append(corpo_cobra)
        if len(cobra) > comprimento_cobra:
            del cobra[0]

        for bloco in cobra[:-1]:
            if bloco == corpo_cobra:
                fim_de_jogo = True

        for bloco in cobra:
            pygame.draw.rect(tela, azul, [bloco[0], bloco[1], tamanho_celula, tamanho_celula])

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_celula) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_celula) / 20.0) * 20.0
            comprimento_cobra += 1

        relogio.tick(15)

    pygame.quit()
    quit()

# Iniciar o jogo
jogo()


