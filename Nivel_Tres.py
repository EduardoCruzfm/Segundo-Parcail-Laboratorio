import pygame
from pygame.locals import*
from Clases import*
from configuraciones import*
from configuraciones_enemigo import*
from Clases_plataforma import*
from Nivel_Base import*
from Clase_enemigo import Enemigo
from configuracion_item_trampa import*
from Clase_item import Item
from Clase_trampa import Trampa
from banderas import*

class NivelTres(Nivel):
    def __init__(self, pantalla: pygame.Surface) -> None:
        

        # PANTALLA
        W = pantalla.get_width()
        H = pantalla.get_height()

        # FONDO
        fondo = pygame.image.load(r"Segundo-Parcail-Laboratorio\Fondo\3.jpg")
        fondo = pygame.transform.scale(fondo,(W,H))

        # PERSONAJE            x       y
        posicion_inicial = (1650,500)
        tamaño = (75,85)

        diccionario_animaciones = {}
        diccionario_animaciones["quieto"] = personaje_quieto
        diccionario_animaciones["quieto_izq"] = personaje_sombrero_izquierda
        diccionario_animaciones["salta"] = personaje_salta
        diccionario_animaciones["camina_derecha"] = personaje_camina
        diccionario_animaciones["camina_izquierda"] = personaje_camina_izquiera
        diccionario_animaciones["gira_ataca"] = personaje_gira_ataque
        diccionario_animaciones["sombrero_ataca"] = personaje_sombrero

        mi_personaje = Personaje(tamaño,diccionario_animaciones,posicion_inicial,10)
        sombrero = mi_personaje.sombrero_ataque
        
        #ENEMIGO
        posicion_inicial_enemigo = (1500,150)
        
       
        diccionario_animaciones_enemigo = {}
        diccionario_animaciones_enemigo["quieto"] = enemigo_quieto_izquierda
        diccionario_animaciones_enemigo["gira_ataca"] = enemigo_camina_izquierda
        diccionario_animaciones_enemigo["salta"] = personaje_salta
        diccionario_animaciones_enemigo["camina_derecha"] = enemigo_ataca
        diccionario_animaciones_enemigo["camina_izquierda"] = enemigo_ataca_izquieda

        mi_enemigo = Enemigo(tamaño,diccionario_animaciones_enemigo,posicion_inicial_enemigo,40)

        #ENEMIGO OBSTACULO
        posicion_inicial_enemigo_obstaculo = (160,310)
        tamaño_dos = (100,95)
        diccionario_animaciones_enemigo_obstaculo = {}
        diccionario_animaciones_enemigo_obstaculo["quieto"] = motaro_quieto
        diccionario_animaciones_enemigo_obstaculo["gira_ataca"] = scorpion_ataca
        diccionario_animaciones_enemigo_obstaculo["salta"] = motaro_ataca
        diccionario_animaciones_enemigo_obstaculo["camina_derecha"] = motaro_ataca
        diccionario_animaciones_enemigo_obstaculo["camina_izquierda"] = motaro_ataca

        mi_enemigo_obstaculo = Enemigo(tamaño_dos,diccionario_animaciones_enemigo_obstaculo,posicion_inicial_enemigo_obstaculo,10)

        lista_enemigos = [mi_enemigo,mi_enemigo_obstaculo]

        # PLATAFORMA
        plataforma_uno = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\5.jpg",1200,50,(200,735))
        plataforma_dos = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\5.jpg",200,50,(1600,650))
        plataforma_tres = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\5.jpg",200,50,(1100,500))
        plataforma_cuatro = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\5.jpg",1700,20,(90,220))
        plataforma_cinco = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\5.jpg",200,50,(600,400))
        plataforma_seis = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\5.jpg",200,50,(100,400))

        # LISTA DE PLATAFORMAS
        # lista_plataformas = [lados_plataforma,plataforma_dos.plataforma_lados,lados_plataforma_3]
        lista_plataformas = [plataforma_uno,plataforma_dos,plataforma_tres,plataforma_cuatro,plataforma_cinco,plataforma_seis]

        # ITEM
        diccionario_animaciones_item = {}
        diccionario_animaciones_item["gira"] = item

        moneda = Item((30,30),diccionario_animaciones_item,(1100,450))
        moneda_dos = Item((30,30),diccionario_animaciones_item,(1600,550))
       

        lista_items = [moneda,moneda_dos]

        # TRAMPA
        diccionario_animaciones_trampa = {}
        diccionario_animaciones_trampa["gira"] = trampa

        trampa_uno = Trampa((50,50),diccionario_animaciones_trampa,(900,150))
        trampa_dos = Trampa((50,50),diccionario_animaciones_trampa,(1000,350))

        lista_trampa = [trampa_uno,trampa_dos]

        segundos_1 = 900
        super().__init__(pantalla, mi_personaje, lista_plataformas, fondo ,lista_items,lista_trampa,sombrero,segundos_1,lista_enemigos)

    def update(self, lista_eventos) -> None:
    
        self.bandera()
        return super().update(lista_eventos)    


    def bandera(self):

        if self.vidas_enemigo < 0:
            crear_bandera("bandera_3","true")