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

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            letra = str(pg.key.name(event.key)).upper()
            print(letra)

    # Jogo
    Desenho_da_Forca(window, chance)

    pg.display.update()
