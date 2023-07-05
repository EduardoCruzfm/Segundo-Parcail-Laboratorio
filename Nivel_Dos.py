import pygame
from pygame.locals import*
from Clases import*
from configuraciones import*
from configuraciones_enemigo import*
from Clases_plataforma import*
from Nivel_Base import*
from Clase_enemigo import Enemigo
from Clase_cirax import*
from Clase_nood import*
from Clase_sub import*
from configuracion_item_trampa import*
from Clase_item import Item
from Clase_trampa import Trampa
from banderas import*
import random

class NivelDos(Nivel):
    def __init__(self, pantalla: pygame.Surface) -> None:
        

        # PANTALLA
        W = pantalla.get_width()
        H = pantalla.get_height()

        # FONDO
        fondo = pygame.image.load(r"Segundo-Parcail-Laboratorio\Fondo\2.jpg")
        fondo = pygame.transform.scale(fondo,(W,H))

        # PERSONAJE            x       y
        posicion_inicial = (H/2 - 300,650)
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
        posicion_inicial_enemigo = (150,150)
       
        diccionario_animaciones_enemigo = {}
        diccionario_animaciones_enemigo["quieto"] = cirax_quieto
        diccionario_animaciones_enemigo["gira_ataca"] = cirax_quieto
        diccionario_animaciones_enemigo["salta"] = cirax_quieto
        diccionario_animaciones_enemigo["camina_derecha"] = cirax_ataca
        diccionario_animaciones_enemigo["camina_izquierda"] = cirax_ataca_izquierda

        mi_enemigo = Cirax(tamaño,diccionario_animaciones_enemigo,posicion_inicial_enemigo,40)

        #ENEMIGO OBSTACULO
        posicion_inicial_enemigo_obstaculo = (160,310)

        diccionario_animaciones_enemigo_obstaculo = {}
        diccionario_animaciones_enemigo_obstaculo["quieto"] = nood_quieto
        diccionario_animaciones_enemigo_obstaculo["gira_ataca"] = nood_ataca
        diccionario_animaciones_enemigo_obstaculo["salta"] = nood_salta
        diccionario_animaciones_enemigo_obstaculo["camina_derecha"] = nood_combo
        diccionario_animaciones_enemigo_obstaculo["camina_izquierda"] = nood_ataca

        mi_enemigo_obstaculo = Nood(tamaño,diccionario_animaciones_enemigo_obstaculo,posicion_inicial_enemigo_obstaculo,10)



        #ENEMIGO OBSTACULO_DOS
        posicion_inicial_enemigo_obstaculo = (1300,650)

        diccionario_animaciones_enemigo_obstaculo_2 = {}
        diccionario_animaciones_enemigo_obstaculo_2["quieto"] = sub_quieto
        diccionario_animaciones_enemigo_obstaculo_2["gira_ataca"] = sub_ataca
        diccionario_animaciones_enemigo_obstaculo_2["salta"] = sub_salta
        diccionario_animaciones_enemigo_obstaculo_2["camina_derecha"] = sub_ataca
        diccionario_animaciones_enemigo_obstaculo_2["camina_izquierda"] = sub_ataca_izquierda

        mi_enemigo_obstaculo_2 = Sub(tamaño,diccionario_animaciones_enemigo_obstaculo_2,posicion_inicial_enemigo_obstaculo,10)

        lista_enemigos = [mi_enemigo,mi_enemigo_obstaculo,mi_enemigo_obstaculo_2]


        # PLATAFORMA
        plataforma_uno = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\4.jpg",400,50,(90,835))
        plataforma_siete = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\4.jpg",1200,50,(630,835))
        plataforma_dos = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\4.jpg",100,400,(900,700))
        plataforma_tres = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\4.jpg",200,50,(800,500))
        plataforma_cuatro = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\4.jpg",1800,20,(50,220))
        plataforma_cinco = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\4.jpg",200,50,(1250,500))
        plataforma_seis = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\4.jpg",200,50,(100 ,400))
        plataforma_ocho = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\4.jpg",600,50,(500,835))
        plataforma_nueve = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\4.jpg",300,50,(1700,350))

        # LISTA DE PLATAFORMAS
        lista_plataformas = [plataforma_uno,plataforma_dos,plataforma_tres,plataforma_cuatro,plataforma_cinco,plataforma_seis,plataforma_siete,plataforma_ocho,plataforma_nueve]

        # ITEM
        diccionario_animaciones_item = {}
        diccionario_animaciones_item["gira"] = item

        moneda = Item((30,30),diccionario_animaciones_item,(800,810))
        moneda_dos = Item((30,30),diccionario_animaciones_item,(450,610))
        moneda_tres = Item((30,30),diccionario_animaciones_item,(1600,550))
       
        lista_items = [moneda,moneda_dos,moneda_tres]

        # TRAMPA
        diccionario_animaciones_trampa = {}
        diccionario_animaciones_trampa["gira"] = trampa

        trampa_uno = Trampa((50,50),diccionario_animaciones_trampa,(1000,150))
        trampa_dos = Trampa((50,50),diccionario_animaciones_trampa,(900,350))

        lista_trampa = [trampa_uno,trampa_dos]

        segundos_3 = 2500

        super().__init__(pantalla, mi_personaje, lista_plataformas, fondo ,lista_items,lista_trampa,sombrero,segundos_3,lista_enemigos)

        # EVENTO POR TIEMPO N2
        self.timer_nivel_2 = pygame.USEREVENT + 3
        pygame.time.set_timer(self.timer_nivel_2, 2000)
        self.vidas_enemigo_tres = 5
        self.vidas_enemigo_cero_2 = True


    def update(self, lista_eventos) -> None:
        self.bandera()
        self.moviento_aleatorio(lista_eventos)
        self.vidas_enemigos()
        return super().update(lista_eventos)    


    def bandera(self):
        if self.vidas_enemigo < 0:
            crear_bandera("bandera_2","true") 

    def moviento_aleatorio(self,lista_eventos):

        for evento in lista_eventos:   
            if evento.type == self.timer_nivel_2:   
                aleatorio = random.randint(1,4)
                match aleatorio:

                    case 1:
                        for enemigo in self.lista_enemigos[2:]:
                            enemigo.mover_x(-100)
                            enemigo.proyectil(-20)
                            enemigo.sonido()
                    case 2:
                        for enemigo in self.lista_enemigos[2:]:
                            enemigo.mover_x(100)
                            enemigo.proyectil()
                            enemigo.sonido()
                    case 3:
                        for enemigo in self.lista_enemigos[1:2]:
                            enemigo.mover_x(-100)
                            enemigo.proyectil(-20)
                            enemigo.sonido()
                    case 4:
                        for enemigo in self.lista_enemigos[1:2]:
                            enemigo.mover_x(100)
                            enemigo.proyectil()
                            enemigo.sonido()

                

    def vidas_enemigos(self):
        # SI COLICIONA EL ATAQUE DEL JUGADOR CON EL ENEMIGO
            for sombrero in self.jugador.lista_sombrero: 
                for enemigo in self.lista_enemigos[2:]:
                    if enemigo.lados["left"].colliderect(sombrero.rect):
                        print("COLICIONO EL SOMBRERO")
                        # self.vidas_enemigo -= 0.5
                        self.vidas_enemigo_tres -= 0.5
                        self.puntos_jugador += 200
                        sombrero.eliminar()

                        
            if self.vidas_enemigo_tres == 0 and self.vidas_enemigo_cero_2:
                self.vidas_enemigo_cero_2 = False
                enemigo_eliminado = self.lista_enemigos.pop(1)

            # MENSAJE DE QUE GANA EL JUAGDOR
            # if self.vidas_enemigo == 0 :
            #     # self._slave.fill(NEGRO)
            #     fuente = pygame.font.SysFont("Forte",160)
            #     nivel = fuente.render(f"Nivel III Desbloqueado",False,"Red")
            #     self._slave.blit(nivel,(600,800))
                
                        