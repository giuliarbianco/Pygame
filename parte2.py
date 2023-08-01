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

palavras = ['PARALELEPIPEDO', 'ORNITORRINCO', 'APARTAMENTO', 'XICARA DE CHA']



tentativas_de_letra = ['', '-']
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



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            letra = str(pg.key.name(event.key)).upper()
            print(letra)

    # Jogo
    Desenho_da_Forca(window,6)
    Desenho_restart_buttom(window)
    palavra_escolhida,end_game= Sorteando_Palavra(palavras,palavra_escolhida,end_game)
    

    pg.display.update()

### PARTE 2
# partes do boneco

