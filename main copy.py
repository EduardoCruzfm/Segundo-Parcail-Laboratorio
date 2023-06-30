import pygame,sys
from configuraciones import * 
from pygame.locals import *
from Clases import Personaje
from modo import*
from Clases_plataforma import Plataforma

####################################################################

def actualizar_pantalla(pantalla, un_personaje:Personaje, fondo, lados_piso,fondo_plataforma ,lista_plataformas):
    pantalla.blit(fondo,(0,0))
    # PLATAFORMAS
    for plataforma in lista_plataformas:
        # pantalla.blit(plataforma,(lista_plataformas["main"].x,lista_plataformas["main"].y))
        pantalla.blit(fondo_plataforma,(plataforma["main"].x,plataforma["main"].y))

    un_personaje.update(pantalla,lados_piso)


####################################################################
# PANTALLA
W, H = 1900,900
TAMAÑO_PANTALLA = (W,H)
FPS = 18
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
RELOG = pygame.time.Clock()

fondo = pygame.image.load(r"Segundo-Parcail-Laboratorio\TP_Juego\Fondo\0.png")
fondo = pygame.transform.scale(fondo,TAMAÑO_PANTALLA)

# INICIAMOS PYGAME
pygame.init()

# PERSONAJE            x       y
posicion_inicial = (H/2 - 300,650)
tamaño = (75,85)

diccionario_animaciones = {}
diccionario_animaciones["quieto"] = personaje_quieto
diccionario_animaciones["salta"] = personaje_salta
diccionario_animaciones["camina_derecha"] = personaje_camina
diccionario_animaciones["camina_izquierda"] = personaje_camina_izquiera
diccionario_animaciones["gira_ataca"] = personaje_gira_ataque


mi_personaje = Personaje(tamaño,diccionario_animaciones,posicion_inicial,10)

# PISO
piso = pygame.Rect(0,0,W,20)
piso.top = mi_personaje.lados["main"].bottom

lados_piso = obtener_rectangulos(piso)


# PLATAFORMA
plataforna = pygame.image.load(r"Segundo-Parcail-Laboratorio\TP_Juego\Fondo\1.png")
plataforna = pygame.transform.scale(plataforna,(100,55))
rectangulo_plataforma = plataforna.get_rect()
rectangulo_plataforma.x = 100
rectangulo_plataforma.y = 735

lados_plataforma = obtener_rectangulos(rectangulo_plataforma)

# PLATAFORMA 3
# plataforna_3 = pygame.image.load(r"TP_Juego\Fondo\1.png")
# plataforna = pygame.transform.scale(plataforna,(300,55))
# rectangulo_plataforma_3 = plataforna.get_rect()
# rectangulo_plataforma_3.x = 900
# rectangulo_plataforma_3.y = 735
# lados_plataforma_3 = obtener_rectangulos(rectangulo_plataforma_3)


# PLATAFORMA 2
plataforma_dos = Plataforma(r"Segundo-Parcail-Laboratorio\TP_Juego\fondo_2\w.png",200,50,(400,600))


# LISTA DE PLATAFORMAS
# lista_plataformas = [lados_plataforma,plataforma_dos.plataforma_lados,lados_plataforma_3]
lista_plataformas = [lados_plataforma,plataforma_dos.plataforma_lados]


# ---- MUSICA ----
# CARGAR EL ARCHIVO DE MUSICA
pygame.mixer.music.load(r"Segundo-Parcail-Laboratorio\TP_Juego\Musica\13 Grave Yard.mp3")
# -1 LO REPRODUCE EN BUCLE
pygame.mixer.music.play(-1) 
# VOLUMEN 0 a 1, EL 1 ES EL MAXIMO       
pygame.mixer.music.set_volume(0.1)


flag = True

while flag:
    RELOG.tick(FPS)
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
                
                

    keys = pygame.key.get_pressed()

    # TECLAS
    if keys[pygame.K_RIGHT] and mi_personaje.lados["main"].x < W - mi_personaje.velocidad - mi_personaje.ancho :
        mi_personaje.que_hace = "derecha"

    elif keys[pygame.K_LEFT] and mi_personaje.lados["main"].x > 0:
        mi_personaje.que_hace = "izquierda"

    elif keys[pygame.K_UP]:
        mi_personaje.que_hace = "salta"

    elif keys[pygame.K_x]:
        mi_personaje.que_hace = "gira_ataca"
       
    else: 
        mi_personaje.que_hace = "quieto"

    # MUESTRO EL FONDO EN EL X=0 , Y=0
    # PANTALLA.blit(fondo,(0,0))
    actualizar_pantalla(PANTALLA,mi_personaje,fondo, lados_piso,plataforna,lista_plataformas)

    # SI get_modo() ESTA EN TRUE ->
    if get_mode():
        for lado in lados_piso:
            pygame.draw.rect(PANTALLA,"Orange",lados_piso[lado],2)

        for lado in mi_personaje.lados:
            pygame.draw.rect(PANTALLA,"Blue",mi_personaje.lados[lado],2)
            
        for lado in lados_plataforma:
            pygame.draw.rect(PANTALLA,"Red",lados_plataforma[lado],2)
        
        # for lado in lados_plataforma_3:
        #     pygame.draw.rect(PANTALLA,"Red",lados_plataforma_3[lado],2)

        for lado in plataforma_dos.plataforma_lados:
            pygame.draw.rect(PANTALLA,"Green",plataforma_dos.plataforma_lados[lado],2)
    
    pygame.display.update()