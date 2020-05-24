import pygame  
import sys
import random
pygame.init()

relogio = pygame.time.Clock()


x = 10 #posicao do x em pixel
y = 330 #posicao do y em pixel 
y_inimigos = 330
x_basquete = 800
x_tenis = 800
x_futame = 800

velocity = 10 #velocidade em pixels
velocity_enemies = 15

bola_futebol = pygame.image.load('bolafut.jpg')
bola_basquete = pygame.image.load('bolabasquete.png')
bola_tenis = pygame.image.load('bolatenis.jpg')
bola_futame =  pygame.image.load('bolafutame.jpg')
sol = pygame.image.load('sol.png')
arvore = pygame.image.load('arvore.png')
grama = pygame.image.load('grama.jpg')

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

window = pygame.display.set_mode((700, 700)) # tamanho da janela
pygame.display.set_caption('Joguinho das bolinhas') #nome que aparece na janela

game = True
while True: # cria o jogo
    pygame.time.delay(50)
    for event in pygame.event.get(): #evento
        if event.type == pygame.QUIT:
            game = False #desliga o jogo
            sys.exit()

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP] and y >=220: 
        y -= velocity # subir
    if comandos[pygame.K_LEFT] and x >= 0:
        x -= velocity # ir pra esquerda
    if comandos[pygame.K_RIGHT] and x <= 600:
        x += velocity #ir pra direita
    if comandos[pygame.K_DOWN] and y <=520:
        y += velocity # ir pra baixo

    if x_basquete <= -100 and x_tenis <= -100 and x_futame <= -100:
        x_basquete = random.randint(800,2000) #bola de basquete aparece da direita para esquerda
        x_tenis = random.randint(800,2000) #bola de tenis aparece da direita para esquerda
        x_futame = random.randint(800,4000) #bola de futamericano aparece da direita para esquerda

    x_basquete -= velocity_enemies + random.randint(1,10) #velocidade aleatoria
    x_tenis -= velocity_enemies + random.randint(1,10) #velocidade aleatoria
    x_futame -= velocity_enemies + 12 #velocidade definida (é a bola mais rápida)

    window.fill ((WHITE)) #janela azul

    window.blit(bola_futebol,(x,y))      
    window.blit(bola_basquete,(x_basquete,y_inimigos))
    window.blit(bola_tenis,(x_tenis,y_inimigos + 150))
    window.blit(bola_futame,(x_futame,y_inimigos - 100))
    window.blit(sol,(550,0))
    window.blit(arvore,(500,500))
    window.blit(arvore,(100,500))
    window.blit(grama,(0,600))

    pygame.draw.line(window,BLACK,[0,600],[800,600],5)   #linha 1
    pygame.draw.line(window,BLACK,[0,200],[800,200],5)   #linha 2
 
    pygame.display.update()
    relogio.tick(40)

pygame.quit()
sys.exit()



