import pygame,sys
from pygame.locals import *
from API_FORMS.GUI_formulario_prueba import*


def inciar_juego()->None:
    '''
        Brief: Inicializa el juego
   
    '''

    try:
        # PANTALLA
        W, H = 1900,900
        TAMAÑO_PANTALLA = (W,H)
        FPS = 15

        # INICIAMOS PYGAME
        pygame.init()
        pygame.display.set_caption("Parcial II")

        # ---- ICONO ----
        icono = pygame.image.load(r"Segundo-Parcail-Laboratorio\Moneda_vida\2.png")
        pygame.display.set_icon(icono)


        RELOG = pygame.time.Clock()
        PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)

        form_prueba = FormPrueba(PANTALLA,500,300,900,350,(70,6,6),(171,1,1),5,True)

        flag = True
        while flag:
            RELOG.tick(FPS)
            lista_eventos = pygame.event.get()

            for evento in lista_eventos:
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            PANTALLA.fill("Black")
            
            form_prueba.update(lista_eventos)
            
            pygame.display.update()

    except ModuleNotFoundError as e:
        print(f"Error en el modulo: tipo de error -> {e}")

    except Exception as e:
        print(f"Error analizar {e}")
    finally:
        print("PARCIAL 2")
    

inciar_juego()