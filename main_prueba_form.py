import pygame,sys
from pygame.locals import *
from API_FORMS.GUI_formulario_prueba import*


# PANTALLA
W, H = 1900,900
TAMAÑO_PANTALLA = (W,H)
FPS = 15

# INICIAMOS PYGAME
pygame.init()
pygame.display.set_caption("Parcial II")


RELOG = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)

# ---- MUSICA ----
# CARGAR EL ARCHIVO DE MUSICA
# pygame.mixer.music.load(r"TP_Juego\Musica\13 Grave Yard.mp3")
# # -1 LO REPRODUCE EN BUCLE
# pygame.mixer.music.play(-1) 
# # VOLUMEN 0 a 1, EL 1 ES EL MAXIMO       
# pygame.mixer.music.set_volume(0.1)

# nivel_actual = NivelUno(PANTALLA)
form_prueba = FormPrueba(PANTALLA,500,300,900,350,"Gray","Red",5,True)

flag = True
auxiliar = 1
while flag:
    RELOG.tick(FPS)
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    

    PANTALLA.fill("Black")
    # nivel_actual.update(lista_eventos) 
    
    form_prueba.update(lista_eventos)
    
    pygame.display.update()