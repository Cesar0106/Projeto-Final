#Bibliotecas importadas
import pygame  
import sys
import random

#Inicia o jogo
pygame.init()

#Criar relógio
clock=pygame.time.Clock()

x = 10 #posicao do x em pixel
y = 330 #posicao do y em pixel 
y_robo = 330
y_asteroide = 480
y_nave = 230
x_robo = 800
x_asteroide = 800
x_nave = 800


velocity = 10 #velocidade em pixels
velocity_enemies = 15

# Importando as imagens
carinha = pygame.image.load('carinha.gif')
trooper = pygame.image.load('robo.png')
asteroide = pygame.image.load('asteroid.png')
nave =  pygame.image.load('nave.png')
fundo = pygame.image.load("fundo.jpg")
tela_inicio = pygame.image.load("inicio.jpg")
tela_fim = pygame.image.load("over.jpg")


#Definindo as cores
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)


window = pygame.display.set_mode((700, 700)) # tamanho da janela
pygame.display.set_caption('Invasores de Petrópolis') #nome que aparece na janela
controle  = 0
game = True
while True: # cria o jogo
    pygame.time.delay(50)
    for event in pygame.event.get(): #evento
        if event.type == pygame.QUIT:
            game = False #desliga o jogo
            sys.exit()

        

    controle+=1
    

    movimentos = pygame.key.get_pressed()
    if movimentos[pygame.K_UP] and y >=220: 
        y -= velocity # subir
    if movimentos[pygame.K_LEFT] and x >= 0:
        x -= velocity # ir pra esquerda
    if movimentos[pygame.K_RIGHT] and x <= 600:
        x += velocity #ir pra direita
    if movimentos[pygame.K_DOWN] and y <=520:
        y += velocity # ir pra baixo

    if x + 30 > x_robo and x - 30 < x_robo and y - 30 > y_robo and y + 20 < y_robo:
        x = 900
    #if x + 10 > x_asteroide and x - 10 < x_asteroide and y > y_asteroide:    
        #x = 2000       
    #if x + 10 > x_nave and y - 30 < y_nave:   
        #x = 2000
        
        

    if x_robo <= -100:   
        x_robo = random.randint(800,2000) #stormtrooper chegando da direita

    if x_asteroide <= -100:
        x_asteroide = random.randint(800,2000) #asteroide chegando da direita

    if x_nave <= -100:
        x_nave = random.randint(800,4000) #nave chegando da direita

    x_robo -= velocity_enemies + random.randint(1,10) #velocidade aleatoria
    x_asteroide -= velocity_enemies + random.randint(1,10) #velocidade aleatoria
    x_nave -= velocity_enemies + 12 #velocidade definida (é a bola mais rápida)

    window.fill ((BLUE))#Fundo azul
    window.blit(fundo,(0,0))
    window.blit(carinha,(x,y))      
    window.blit(trooper,(x_robo,y_robo))
    window.blit(asteroide,(x_asteroide,y_asteroide))
    window.blit(nave,(x_nave,y_nave))

    pygame.draw.line(window,BLACK,[0,600],[800,600],5)   #linha 1
    pygame.draw.line(window,BLACK,[0,200],[800,200],5)   #linha 2
 
    pygame.display.update()


pygame.quit()
sys.exit()



