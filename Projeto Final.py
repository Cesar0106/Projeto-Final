#Bibliotecas importadas
import pygame  
import sys
import random

#Inicia o jogo
pygame.init()

#Criar relógio
clock=pygame.time.Clock()

x = 10 #posicao inicial x do jogador
y = 330  #posicao inicial y do jogador 
y_robo = 330  #posicao inicial y do robô
y_asteroide = 480  #posicao inicial y do asteroide
y_nave = 230  #posicao inicial y da nave
x_robo = 800  #posicao inicial x do robô
x_asteroide = 800  #posicao inicial x do asteroide
x_nave = 800  #posicao inicial x da nave
x_death = 800  #posicao inicial x do cometa
y_death = 420  #posicao inicial y do cometa

largura = 700
altura = 700

velocity = 20 #velocidade do jogador em pixels
velocity_enemies = 30 #velocidade geral dos inimigos

# Importando as imagens
carinha = pygame.image.load('carinha.gif')
trooper = pygame.image.load('robo.png')
asteroide = pygame.image.load('asteroid.png')
nave =  pygame.image.load('nave.png')
deathstar = pygame.image.load('deathstar.png')
fundo = pygame.image.load("fundo.jpg")
tela_inicio = pygame.image.load("inicio.jpg")
tela_fim = pygame.image.load("over.jpg")

#poe o audio no jogo
audio_do_jogo = pygame.mixer.Sound('audioJogo.ogg')
volume = audio_do_jogo.set_volume(0.4)

audio_colisao = pygame.mixer.Sound('impact_audio.wav')
volume_colusao = audio_colisao.set_volume(0.9)

#Definindo algumas cores
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

window = pygame.display.set_mode((largura, altura)) # tamanho da janela
pygame.display.set_caption('Invasores de Petrópolis') #nome que aparece na janela
controle  = 0
game = True
fimjogo = False
while game: # cria o jogo
    pygame.time.delay(50)
    while fimjogo:
        window.blit(tela_fim,(0,0))
        audio_colisao.play()
        pygame.display.update()
        for event in pygame.event.get(): #evento
            if event.type == pygame.QUIT:
                game = False #desliga o jogo
                fimjogo = False
                

    for event in pygame.event.get(): #evento
        if event.type == pygame.QUIT:
            game = False #desliga o jogo
            sys.exit()

    controle+= 1 #placar do jogo

    font = pygame.font.Font(pygame.font.get_default_font(), 25) # fonte para o texto do score (placar)
    texto = font.render('Pontuação: {0}'.format(controle), True, WHITE)

    movimentos = pygame.key.get_pressed() #movimentos impedem que o jogador ultrapasse as 2 linhas
    if movimentos[pygame.K_UP] and y >=220: 
        y -= velocity # subir
    if movimentos[pygame.K_LEFT] and x >= 0:
        x -= velocity # ir pra esquerda
    if movimentos[pygame.K_RIGHT] and x <= 600:
        x += velocity #ir pra direita
    if movimentos[pygame.K_DOWN] and y <=520:
        y += velocity # ir pra baixo

    if x + 30 > x_robo and y + 50 > y_robo and x < x_robo and y - 70 < y_robo:  #colisão com o robô
        fimjogo = True

    if x + 10 > x_asteroide and x - 10 < x_asteroide and y > y_asteroide:     #colisão com o asteroide
        fimjogo = True    

    if x + 10 > x_nave and y - 30 < y_nave:   #colisão com a nave espacial
        fimjogo = True

    if x + 10 > x_death and x - 10 < x_death and y + 25 > y_death and y - 25 < y_death: #colisão com o cometa
        fimjogo = True
#-----------------------------------------------------------------------------------------
 
    if x_robo <= -100:   
        x_robo = random.randint(800,2000) #stormtrooper chegando da direita

    if x_asteroide <= -100:
        x_asteroide = random.randint(800,2000) #asteroide chegando da direita

    if x_nave <= -100:
        x_nave = random.randint(800,4000) #nave chegando da direita

    if x_death <= -100:
        x_death = random.randint(800,1000)  #deathstar chegando da direita (com mais frequencia)


    x_robo -= velocity_enemies + random.randint(1,10) #velocidade aleatoria
    x_asteroide -= velocity_enemies + random.randint(1,10) #velocidade aleatoria
    x_nave -= velocity_enemies + 12 #velocidade definida (é a bola mais rápida)
    x_death -= velocity_enemies - 6 #velocidade do cometa é menor do que as outras

    #Põe os personagens no jogo
    window.fill ((BLUE))#Fundo azul
    window.blit(fundo,(0,0))
    window.blit(carinha,(x,y))      
    window.blit(trooper,(x_robo,y_robo))
    window.blit(asteroide,(x_asteroide,y_asteroide))
    window.blit(nave,(x_nave,y_nave))
    window.blit(deathstar,(x_death,y_death))
    window.blit(texto, (100, 100))

    #Põe o audio do jogo
    audio_do_jogo.play()

    pygame.draw.line(window,BLACK,[0,600],[800,600],5)   #linha 1
    pygame.draw.line(window,BLACK,[0,200],[800,200],5)   #linha 2
 
    pygame.display.update()


pygame.quit()
sys.exit()



