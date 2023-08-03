import pygame as pg
import random

# Cores do jogo
branco = (255, 255, 255)
preto = (0,0,0)

# Setup da tela do jogo
window = pg.display.set_mode((1000, 600))

# Iniciando fonte do jogo
pg.font.init()
# Escolhendo uma fonte e tamanho
font = pg.font.SysFont('Courier New', 50)
font_rb = pg.font.SysFont('Courier New', 30)

palavras = ['PARALELEPIPEDO', 'ORNITORRINCO', 'APARTAMENTO', 'XICARA DE CHA', 'INSPER', 'GIULIA', 'PEDRO', 'GUILHERME']

# Cria som de explosão
pg.mixer.init()
explosao2_fx = pg.mixer.Sound("explosion2.wav")
explosao2_fx.set_volume(0.25)

tentativas_de_letras = [' ', '-']
palavra_escolhida = ''
palavra_camuflada = ''
end_game = True
chance = 0
letra = ''
click_last_status = False

def Desenho_da_Forca(window, chance):
    pg.draw.rect(window, branco, (0, 0, 1000, 600))
    pg.draw.line(window, preto, (100, 500), (100, 100), 10)
    pg.draw.line(window, preto, (50, 500), (150, 500), 10)
    pg.draw.line(window, preto, (100, 100), (300, 100), 10)
    pg.draw.line(window, preto, (300, 100), (300, 150), 10)
    if chance >= 1:
        pg.draw.circle(window,preto,(300,200),50,10)
    if chance >= 2:
        pg.draw.line(window,preto,(300,250),(300,350),10)
    if chance >= 3:
        pg.draw.line(window,preto,(300,260),(225,350),10)
    if chance >= 4:
        pg.draw.line(window,preto,(300,260),(375,350),10)
    if chance >= 5:
        pg.draw.line(window,preto,(300,350),(375,450),10)
    if chance >= 6:
        pg.draw.line(window,preto,(300,350),(225,450),10)

def Desenho_restart_buttom(window):
    pg.draw.rect(window,preto,(700,100,200,65))
    texto = font_rb.render('Restart',True,branco)
    window.blit(texto,(740,120))

def Sorteando_Palavra(palavras,palavra_escolhida,end_game):
    if end_game == True:
        palavra_n = random.randint(0,len(palavras)-1)
        palavra_escolhida = palavras[palavra_n]
        end_game = False
    return palavra_escolhida,end_game

def Camuflando_Palavra (palavra_escolhida, palavra_camuflada, tentativas_de_letras):
    palavra_camuflada = palavra_escolhida
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n:n+1] not in tentativas_de_letras:
            palavra_camuflada = palavra_camuflada.replace(palavra_camuflada[n], '#')
    return palavra_camuflada 

def Tentando_uma_letra(tentativas_de_letras, palavra_escolhida, letra, chance):
    if letra not in tentativas_de_letras:
        tentativas_de_letras.append(letra)
        if letra not in palavra_escolhida:
            chance += 1
        elif letra in tentativas_de_letras:
            pass
    return tentativas_de_letras, chance

def Palavra_do_jogo(window, palavra_camuflada):
    palavra = font.render(palavra_camuflada, True, preto)
    window.blit(palavra, (200, 500))

def Restart_do_jogo(palavra_camuflada, end_game, chance, letra, tentativas_de_letras, click_last_status, click, x, y):
    count = 0
    limite = len(palavra_camuflada)
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n] != '#':
            count += 1
    if click_last_status == False and click[0] == True:
        if x >= 700 and x <= 900 and y >= 100 and y <= 165:
            tentativas_de_letras = [' ', '-']
            end_game = True
            chance = 0
            letra = ' '
    return end_game, chance, tentativas_de_letras, letra
iniciar = True
while iniciar:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            iniciar = False
    iniate = pg.display.set_mode((1000, 600))
    pg.draw.rect(iniate, branco, (0, 0, 1000, 600))
    texto = font_rb.render('Objetivo: Adivinhar uma palavra ou frase antes de um boneco ser desenhado na forca',True,branco)
    iniate.blit(texto,(100,75))
    texto = font_rb.render('Regras: O adversário escolhe a palavra e desenha espaços em branco para cada letra.',True,branco)
    iniate.blit(texto,(100,150))
    texto = font_rb.render('Acertos: Letras corretas são preenchidas nas posições corretas.',True,branco)
    iniate.blit(texto,(100,225))
    texto = font_rb.render('Erros: Letras erradas são listadas e uma parte do boneco enforcado é desenhada.',True,branco)
    iniate.blit(texto,(100,300))
    texto = font_rb.render('Vitória: O jogador ganha se adivinhar a palavra antes do boneco estar completo.',True,branco)
    iniate.blit(texto,(100,375))
    texto = font_rb.render('Derrota: O jogador perde se o boneco estiver desenhado antes da palavra ser adivinhada.',True,branco)
    iniate.blit(texto,(100,450))
    texto = font_rb.render('Aperte ENTER para começar!',True,branco)
    iniate.blit(texto,(100,525))
    pg.display.update()
   
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            letra = str(pg.key.name(event.key)).upper()
            print(letra)
    
    #declarando variavel do mouse 
    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]

    #declarando variavel do click
    click = pg.mouse.get_pressed()

    # Jogo
    Desenho_da_Forca(window,chance)
    Desenho_restart_buttom(window)
    palavra_escolhida,end_game = Sorteando_Palavra(palavras,palavra_escolhida,end_game)
    palavra_camuflada = Camuflando_Palavra (palavra_escolhida, palavra_camuflada, tentativas_de_letras)
    tentativas_de_letras, chance = Tentando_uma_letra(tentativas_de_letras, palavra_escolhida, letra, chance)
    Palavra_do_jogo(window, palavra_camuflada)
    end_game, chance, tentativas_de_letras, letra = Restart_do_jogo(palavra_camuflada, end_game, chance, letra, tentativas_de_letras, click_last_status, click, mouse_position_x, mouse_position_y)
    
    if chance >= 6:
        print ('PERDEU!')
        explosao2_fx.play()
        texto = font_rb.render('Você perdeu!',True,preto)
        window.blit(texto,(550,300))
        texto = font_rb.render('Aperte restart para tentar novamente',True,preto)
        window.blit(texto,(350,350))
    elif '#' not in palavra_camuflada:
        print ('GANHOU!')
        texto = font_rb.render('Você ganhou!',True,preto)
        window.blit(texto,(550,300))
    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False
    pg.display.update()

