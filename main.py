import pygame,sys
from configuraciones import * 
from pygame.locals import *
from Clases import Personaje
from modo import*
from Clases_plataforma import Plataforma

####################################################################

def actualizar_pantalla(pantalla, un_personaje:Personaje, fondo, lados_piso,lista_plataformas):
    pantalla.blit(fondo,(0,0))
    # PLATAFORMAS


    for plataforma in lista_plataformas:
        pantalla.blit(plataforma.imagen,(plataforma.rectangulo_plataforma))
        # pantalla.blit(plataforma.imagen,(plataforma.rectangulo_plataforma.x , plataforma.rectangulo_plataforma.y))

    un_personaje.update(pantalla,lista_plataformas)
    # un_personaje.update(lados_piso,lista_plataformas)


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
plataforma_uno = Plataforma(r"Segundo-Parcail-Laboratorio\TP_Juego\fondo_2\w.png",1200,50,(100,735))
plataforma_dos = Plataforma(r"Segundo-Parcail-Laboratorio\TP_Juego\fondo_2\w.png",200,50,(1300,650))
plataforma_tres = Plataforma(r"Segundo-Parcail-Laboratorio\TP_Juego\fondo_2\w.png",200,50,(1000,500))


# LISTA DE PLATAFORMAS
# lista_plataformas = [lados_plataforma,plataforma_dos.plataforma_lados,lados_plataforma_3]
lista_plataformas = [plataforma_uno,plataforma_dos,plataforma_tres]


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
    PANTALLA.blit(fondo,(0,0))
    actualizar_pantalla(PANTALLA,mi_personaje,fondo, lados_piso,lista_plataformas)

    # SI get_modo() ESTA EN TRUE ->
    if get_mode():

        for lado in lados_piso:
            pygame.draw.rect(PANTALLA,"Orange",lados_piso[lado],2)

        for plataforma in lista_plataformas:
            for lado in plataforma.plataforma_lados:
                pygame.draw.rect(PANTALLA,"Blue",plataforma.plataforma_lados[lado],2)


        for lado in mi_personaje.lados:
            pygame.draw.rect(PANTALLA,"Red",mi_personaje.lados[lado],2)
    
    pygame.display.update()