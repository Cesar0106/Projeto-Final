#Bibliotecas importadas
import pygame  
import sys
import random

#Inicia o jogo
pygame.init()

#Criar relógio
clock=pygame.time.Clock()
class inicio:
    def __init__(self, a,b,c,d,e,f,g,h,i,j):
        self.x = a  #posicao inicial x do jogador 
        self.y = b  #posicao inicial y do jogador 
        self.y_robo = c  #posicao inicial y do robô
        self.y_asteroide = d  #posicao inicial y do asteroideinicio.
        self.y_nave = e  #posicao inicial y da nave
        self.x_robo = f  #posicao inicial x do robô
        self.x_asteroide = g  #posicao inicial x do asteroide
        self.x_nave = h  #posicao inicial x da nave
        self.x_death = i  #posicao inicial x do cometa
        self.y_death = j  #posicao inicial y do cometa

inicio= inicio(10,330,330,480,230,800,800,800,800,420)
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
#audio_do_jogo = pygame.mixer.Sound('audioJogo.ogg')
#volume = audio_do_jogo.set_volume(0.4)

#audio_colisao = pygame.mixer.Sound('impact_audio.wav')
#volume_colusao = audio_colisao.set_volume(0.9)

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
        #audio_colisao.play()
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
    if movimentos[pygame.K_UP] and inicio.y >=220: 
        inicio.y -= velocity # subir
    if movimentos[pygame.K_LEFT] and inicio.x >= 0:
       inicio. x -= velocity # ir pra esquerda
    if movimentos[pygame.K_RIGHT] and inicio.x <= 600:
       inicio. x += velocity #ir pra direita
    if movimentos[pygame.K_DOWN] and inicio.y <=520:
        inicio.y += velocity # ir pra baixo

    if inicio.x + 30 > inicio.x_robo and inicio.y + 50 > inicio.y_robo and inicio.x < inicio.x_robo and inicio.y - 70 < inicio.y_robo:  #colisão com o robô
        fimjogo = True

    if inicio.x + 10 > inicio.x_asteroide and inicio.x - 10 < inicio.x_asteroide and inicio.y > inicio.y_asteroide:     #colisão com o asteroide
        fimjogo = True    

    if inicio.x + 10 > inicio.x_nave and inicio.y - 30 < inicio.y_nave:   #colisão com a nave espacial
        fimjogo = True

    if inicio.x + 10 > inicio.x_death and inicio.x - 10 < inicio.x_death and inicio.y + 25 > inicio.y_death and inicio.y - 25 < inicio.y_death: #colisão com o cometa
        fimjogo = True
#-----------------------------------------------------------------------------------------
 
    if inicio.x_robo <= -100:   
        inicio.x_robo = random.randint(800,2000) #stormtrooper chegando da direita

    if inicio.x_asteroide <= -100:
        inicio.x_asteroide = random.randint(800,2000) #asteroide chegando da direita

    if inicio.x_nave <= -100:
        inicio.x_nave = random.randint(800,4000) #nave chegando da direita

    if inicio.x_death <= -100:
       inicio.x_death = random.randint(800,1000)  #deathstar chegando da direita (com mais frequencia)


    inicio.x_robo -= velocity_enemies + random.randint(1,10) #velocidade aleatoria
    inicio.x_asteroide -= velocity_enemies + random.randint(1,10) #velocidade aleatoria
    inicio.x_nave -= velocity_enemies + 12 #velocidade definida (é a bola mais rápida)
    inicio.x_death -= velocity_enemies - 6 #velocidade do cometa é menor do que as outras

    #Põe os personagens no jogo
    window.fill ((BLUE))#Fundo azul
    window.blit(fundo,(0,0))
    window.blit(carinha,(inicio.x,inicio.y))      
    window.blit(trooper,(inicio.x_robo,inicio.y_robo))
    window.blit(asteroide,(inicio.x_asteroide,inicio.y_asteroide))
    window.blit(nave,(inicio.x_nave,inicio.y_nave))
    window.blit(deathstar,(inicio.x_death,inicio.y_death))
    window.blit(texto, (100, 100))

    #Põe o audio do jogo
    #audio_do_jogo.play()

    pygame.draw.line(window,BLACK,[0,600],[800,600],5)   #linha 1
    pygame.draw.line(window,BLACK,[0,200],[800,200],5)   #linha 2
 
    pygame.display.update()


pygame.quit()
sys.exit()



