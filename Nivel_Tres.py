import pygame
from pygame.locals import*
from Clases import*
from configuraciones import*
from configuraciones_enemigo import*
from Clases_plataforma import*
from Nivel_Base import*
from Clase_enemigo import Enemigo
from Clase_sub import*
from Clase_scorpion import*
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
        posicion_inicial = (1700,500)
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

        #ENEMIGO MOTARO
        posicion_inicial_enemigo_obstaculo = (160,310)
        tamaño_dos = (100,95)
        diccionario_animaciones_enemigo_obstaculo = {}
        diccionario_animaciones_enemigo_obstaculo["quieto"] = motaro_quieto
        diccionario_animaciones_enemigo_obstaculo["gira_ataca"] = scorpion_ataca
        diccionario_animaciones_enemigo_obstaculo["salta"] = motaro_ataca
        diccionario_animaciones_enemigo_obstaculo["camina_derecha"] = motaro_ataca
        diccionario_animaciones_enemigo_obstaculo["camina_izquierda"] = motaro_ataca

        mi_enemigo_obstaculo = Enemigo(tamaño_dos,diccionario_animaciones_enemigo_obstaculo,posicion_inicial_enemigo_obstaculo,10)


        #ENEMIGO OBSTACULO SUB
        posicion_inicial_enemigo_obstaculo = (650,650)

        diccionario_animaciones_enemigo_obstaculo_2 = {}
        diccionario_animaciones_enemigo_obstaculo_2["quieto"] = sub_quieto
        diccionario_animaciones_enemigo_obstaculo_2["gira_ataca"] = sub_ataca
        diccionario_animaciones_enemigo_obstaculo_2["salta"] = sub_salta
        diccionario_animaciones_enemigo_obstaculo_2["camina_derecha"] = sub_ataca
        diccionario_animaciones_enemigo_obstaculo_2["camina_izquierda"] = sub_ataca_izquierda

        mi_enemigo_obstaculo_2 = Sub(tamaño,diccionario_animaciones_enemigo_obstaculo_2,posicion_inicial_enemigo_obstaculo,10)


         #ENEMIGO OBSTACULO ESCORPON
        posicion_inicial_enemigo_obstaculo = (60,700)
        
        diccionario_animaciones_enemigo_obstaculo_3 = {}
        diccionario_animaciones_enemigo_obstaculo_3["quieto"] = scorpion_quieto
        diccionario_animaciones_enemigo_obstaculo_3["gira_ataca"] = scorpion_ataca
        diccionario_animaciones_enemigo_obstaculo_3["salta"] = scorpion_ataca
        diccionario_animaciones_enemigo_obstaculo_3["camina_derecha"] = scorpion_ataca
        diccionario_animaciones_enemigo_obstaculo_3["camina_izquierda"] = scorpion_ataca

        mi_enemigo_obstaculo_3 = Escorpion(tamaño,diccionario_animaciones_enemigo_obstaculo_3,posicion_inicial_enemigo_obstaculo,10)

        lista_enemigos = [mi_enemigo,mi_enemigo_obstaculo,mi_enemigo_obstaculo_2,mi_enemigo_obstaculo_3]






        # PLATAFORMA
        plataforma_uno = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\5.jpg",1100,50,(0,835))
        plataforma_dos = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\5.jpg",200,50,(1700,700))
        plataforma_tres = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\5.jpg",200,50,(1200,600))
        plataforma_cuatro = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\5.jpg",1700,20,(90,220))
        plataforma_cinco = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\5.jpg",300,50,(700,450))
        plataforma_seis = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\5.jpg",200,50,(100,400))
        plataforma_siete = Plataforma(r"Segundo-Parcail-Laboratorio\Fondo\5.jpg",100,50,(1450,835))

        # LISTA DE PLATAFORMAS
        # lista_plataformas = [lados_plataforma,plataforma_dos.plataforma_lados,lados_plataforma_3]
        lista_plataformas = [plataforma_uno,plataforma_dos,plataforma_tres,plataforma_cuatro,plataforma_cinco,plataforma_seis,plataforma_siete]

        # ITEM
        diccionario_animaciones_item = {}
        diccionario_animaciones_item["gira"] = item

        moneda = Item((30,30),diccionario_animaciones_item,(1100,450))
        moneda_dos = Item((30,30),diccionario_animaciones_item,(1480,800))
       

        lista_items = [moneda,moneda_dos]

        # TRAMPA
        diccionario_animaciones_trampa = {}
        diccionario_animaciones_trampa["gira"] = trampa

        trampa_uno = Trampa((50,50),diccionario_animaciones_trampa,(900,150))
        trampa_dos = Trampa((50,50),diccionario_animaciones_trampa,(1000,350))

        lista_trampa = [trampa_uno,trampa_dos]

        segundos_1 = 900
        super().__init__(pantalla, mi_personaje, lista_plataformas, fondo ,lista_items,lista_trampa,sombrero,segundos_1,lista_enemigos)

            # EVENTO POR TIEMPO N3
        self.timer_nivel_3 = pygame.USEREVENT + 5
        pygame.time.set_timer(self.timer_nivel_3, 1500)
        self.vidas_enemigo_tres = 5
        self.vidas_enemigo_cero_3 = True
        self.bandera_timer_3 = True


    def update(self, lista_eventos) -> None:
        self.bandera()
        self.moviento_aleatorio(lista_eventos)
        self.vidas_enemigos()
        self.verificar_y()
        return super().update(lista_eventos)    



    def moviento_aleatorio(self,lista_eventos):
        if self.bandera_timer_3:

            for evento in lista_eventos:   
                if evento.type == self.timer_nivel_3:   
                    aleatorio = random.randint(1,4)
                    match aleatorio:

                        case 1:
                            for enemigo in self.lista_enemigos[2:]:
                                enemigo.mover_x(-100)
                                enemigo.proyectil(-20)
                                enemigo.sonido()
                        case 2:
                            for enemigo in self.lista_enemigos[2:]:
                                enemigo.mover_x(120)
                                enemigo.proyectil(40)
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
                        case 5:
                            for enemigo in self.lista_enemigos[1:]:
                                enemigo.que_hace = "quieto"

                

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

            if self.vidas_jugador == 0 or self.vidas_enemigo == 0:
                self.bandera_timer_3 = False


            if self.vidas_enemigo_tres == 0 and self.vidas_enemigo_cero_3:
                self.vidas_enemigo_cero_3 = False
                enemigo_eliminado = self.lista_enemigos.pop(1)


    def bandera(self):

        if self.vidas_enemigo < 0:
            crear_bandera("bandera_3","true")

    def verificar_y(self):

        for enemigo in self.lista_enemigos[1:]:
            if enemigo.rectangulo.y > 900:

                for lado in enemigo.lados:
                  enemigo.lados[lado].y = 550
                  enemigo.lados[lado].x = 500
                        
                enemigo.lados["top"].y = 580
                enemigo.lados["left"].y = 580
                enemigo.lados["right"].y = 580
                enemigo.lados["bottom"].y = 650
