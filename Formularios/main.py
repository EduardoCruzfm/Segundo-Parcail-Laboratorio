import pygame,sys
from pygame.locals import*
from GUI_form_prueba import*

pygame.init()

WIDTH = 1200
HEIGTH = 600
FPS = 60

RELOJ = pygame.time.Clock()
pantalla = pygame.display.set_mode((WIDTH,HEIGTH))

form_prueba = FormPrueba(pantalla,200,100,900,350,"Gold","Magenta",5,True)

while True:
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    pantalla.fill("Black")

    form_prueba.update(evento)
    pygame.display.flip()