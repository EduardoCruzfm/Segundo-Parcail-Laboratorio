import pygame
import time
from modo import*
import random
import json
from Class_cronometro import Cronometro


# trae un paramero poder y meterlo en cada enemigo
class Nivel:
    def __init__(self,pantalla,personaje_principal,lista_plataformas,imagen_fondo,lista_item,lista_trampa,sombrero,segundos,lista_enemigo) -> None:
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
        #LISTA ENEMIGO
        self.lista_enemigos = lista_enemigo
        # ITEMS / TRAMPAS
        self.items = lista_item
        self.trampas = lista_trampa
        # PROYECTIL
        self.sombrero = sombrero
        # CAMBIA LOS SEGUNDOS DE LOS EVENTOS
        self.segundos_1 = segundos
        # EVENTO POR TIEMPO 1
        self.timer_event = pygame.USEREVENT + 0
        pygame.time.set_timer(self.timer_event, self.segundos_1)
        # EVENTO POR TIEMPO 2
        self.timer_event_moviento_enemigo = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event_moviento_enemigo, 3000)
         # VIDAS
        self.vidas_jugador = 3
        self.vidas_enemigo = 7
        self.vidas_enemigo_dos = 6
        # PUNTOS
        self.puntos_jugador = 0
        # CRONOMETRO
        self.auxiliar = 1
        self.tiempo = Cronometro(0)
        # FLAG MENSAJE FINAL
        self.flag_msj_final = True
        # JSON
        self.dic_data = {}
        
  
    def update(self,lista_eventos)->None:
        '''
        Brief: Actualiza la pantalla en cada iteracion llamando a todos los atributos

        Parameters:
            self -> Instancia de la clase
            lista_eventos -> Utilizada para escuchar distintos tipos de eventos
        '''

        for evento in lista_eventos:  
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
                
            if evento.type == self.timer_event_moviento_enemigo:            
                self.numero_aleatorio = random.randint(1, 2)
    
                # MOVIMIENTO ALEATORIO
                match self.numero_aleatorio:
                    case 1:
                        self.lista_enemigos[0].que_hace = "ataca_derecha"
                        self.lista_enemigos[0].mover_x(90)
                        self.lista_enemigos[1].que_hace = "quieto"
                    case 2 :
                        self.lista_enemigos[0].que_hace = "ataca"
                        self.lista_enemigos[0].mover_x(-90)
                  
                        self.lista_enemigos[1].que_hace = "quieto"

            # CADA 5 SEG DISPARO
            if evento.type == self.timer_event:
                print("Disparo")
                self.lista_enemigos[0].que_hace = "quieto"
                self.lista_enemigos[1].que_hace = "ataca_derecha"
                # self.enemigo.que_hace = "ataca"---------------------------> para el nivel ma complejo
                self.lista_enemigos[0].burbuja()
                self.lista_enemigos[1].scorpion()

        # LLAMADA
        self.leer_inputs()
        self.actualizar_pantalla()
        self.dibujar_rectantulos()
        self.colicion_sombrero_enemigo(self._slave) 
        self.score(self._slave)
        self.colicion_trampas_vida(self.items,self.trampas)
        self.colicon_burbuja_jugador()
        self.puntos(self._slave)
        self.guardar_partida()
        self.tiempo.mostrar_tiempo(self._slave)
        self.tiempo.actualizar()


    def actualizar_pantalla(self)->None:
        '''
        Brief: Actualiza la pantalla de las plataformas, items, trampas e instancias de parametro de
                    de tipo Class

        Parameters:
            self -> Instancia de la clase
            
        '''

        self._slave.blit(self.img_fondo,(0,0))
        
        # PLATAFORMAS
        for plataforma in self.plataformas:
            self._slave.blit(plataforma.imagen,(plataforma.rectangulo_plataforma))
            # pantalla.blit(plataforma.imagen,(plataforma.rectangulo_plataforma.x , plataforma.rectangulo_plataforma.y))

        # ITEMS
        for item in self.items:
            item.update(self._slave)

        # TRAMPA
        for trampa in self.trampas:
            trampa.update(self._slave)

        # KUNG LAO
        self.jugador.update(self._slave,self.plataformas)
        self.jugador.lista_sombrero.update()
        self.jugador.lista_sombrero.draw(self._slave)
        # ENEMIGO PRICIPAL
        self.lista_enemigos[0].update(self._slave,self.plataformas)
        self.lista_enemigos[0].lista_burbuja.update()
        self.lista_enemigos[0].lista_burbuja.draw(self._slave)
        # ENEMIGO OBSTACULO
        self.lista_enemigos[1].update(self._slave,self.plataformas)
        self.lista_enemigos[1].lista_lanza.update()
        self.lista_enemigos[1].lista_lanza.draw(self._slave)
        
    # INPUTS
    def leer_inputs(self)->None:
        '''
        Brief: Lee el evento de 'keys = pygame.key.get_pressed()', cambiando la cadena str
                que determianara una nueva accion
        Parameters:
            self -> Instancia de la clase     
        '''
        
        # ESCUCHAR EVENTO DE TECLAS
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.jugador.lados["main"].x < self._slave.get_width() - self.jugador.velocidad - self.jugador.ancho:
            self.jugador.que_hace = "derecha"

        elif keys[pygame.K_LEFT] and self.jugador.lados["main"].x > 0:
            self.jugador.que_hace = "izquierda"

        elif keys[pygame.K_UP]:
            self.jugador.que_hace = "salta"

        elif keys[pygame.K_x]:
            self.jugador.que_hace = "gira_ataca"

        elif keys[pygame.K_s]:
            self.jugador.que_hace = "sombrero"
        
        else: 
            self.jugador.que_hace = "quieto"

    
    # MOSTRAR MODO DEBUG
    def dibujar_rectantulos(self)->None:
        '''
        Brief: Lee el esatdo de 'get_mode()', si es True muestra el modo DEBUG mostrando todos los rectangulos
                obtenidos de la superficie, en caso contrario no los muestra
        Parameters:
            self -> Instancia de la clase     
        '''
        if get_mode():
            try:
                # PLATAFOMAS
                for plataforma in self.plataformas:
                    for lado in plataforma.plataforma_lados:
                        pygame.draw.rect(self._slave,"Blue",plataforma.plataforma_lados[lado],2)

                # JUGADOR
                for lado in self.jugador.lados:
                    pygame.draw.rect(self._slave,"Green",self.jugador.lados[lado],2)

                # ENEMIGO
                for lado in self.lista_enemigos[0].lados:
                    pygame.draw.rect(self._slave,"Red",self.lista_enemigos[0].lados[lado],2)

                # ENEMIGO_DOS
                for lado in self.lista_enemigos[1].lados:
                    pygame.draw.rect(self._slave,"Yellow",self.lista_enemigos[1].lados[lado],2)
                
                # ITEMS
                for item in self.items:
                    for lado in item.lados:
                        pygame.draw.rect(self._slave,"Green",item.lados[lado],2)

                # TRAMPA
                for trampa in self.trampas:
                    for lado in trampa.lados:
                        pygame.draw.rect(self._slave,"Orange",trampa.lados[lado],2)

            except IndexError as e:
                print(f"Error en el indice: -> {e}")

    # COLICION DE PROYECTIL CON ENEMIGO
    def colicion_sombrero_enemigo(self,pantalla):
        '''
        Brief: Verifica las coliciones entre jugador y enemigo modificando las vidas y la puntuacion

        Parameters:
            self -> Instancia de la clase     
            pantalla -> Donde se va a blitear los cambios actualizados     
        '''

        try:
            # SI COLICONA EL ENEMIGO CON EL JUGADOR
            if self.lista_enemigos[0].lados["right"].colliderect(self.jugador.lados["top"]):
                print("CHOQUE JUGADOR - ENEMOGO")
                self.vidas_jugador -= 1

            if self.vidas_enemigo < 0:
                self.vidas_enemigo = 0
                
            # SI COLICIONA EL ATAQUE DEL JUGADOR CON EL ENEMIGO
            for sombrero in self.jugador.lista_sombrero:        
                if self.lista_enemigos[0].lados["left"].colliderect(sombrero.rect):
                    print("COLICIONO EL SOMBRERO")
                    self.vidas_enemigo -= 0.5
                    self.puntos_jugador += 200
                    sombrero.eliminar()

            # SI COLICIONA EL ATAQUE DEL JUGADOR_DOS CON EL ENEMIGO
            for sombrero in self.jugador.lista_sombrero:        
                if self.lista_enemigos[1].lados["left"].colliderect(sombrero.rect):
                    print("COLICIONO EL SOMBRERO")
                    self.vidas_enemigo_dos -= 0.5
                    self.puntos_jugador += 200
                    sombrero.eliminar()
            
            # MENSAJE DE QUE GANA EL JUAGDOR
            if self.vidas_enemigo == 0 :
                fuente = pygame.font.SysFont("Forte",160)
                ganaste = fuente.render(f"YOU WIN",False,"Red")
                pantalla.blit(ganaste,(600,400))
                self.segundos_1 += 9000
                

            # MENSAJE DE QUE GANA EL JUAGDOR
            if self.vidas_jugador == 0:
                fuente = pygame.font.SysFont("Forte",160)
                ganaste = fuente.render(f"GAME OVER",False,"Red")
                pantalla.blit(ganaste,(600,400))
                self.numero_aleatorio = 0
                
                # menu------------------------------------------------------------------

        except IndexError as e:
                print(f"Error en el indice: -> {e}")        


    # COLICION DE ATAQUE ENEIMGO A JUGADOR
    def colicon_burbuja_jugador(self):
        '''
        Brief: Verifica las coliciones entre ataque de enemigo contra el jugador modificando 
                solamente la vida del jugador.
                Verifica si el jugador sobre pasa el eje y, ubicandolo en una posicopn superion en el eje y

        Parameters:
            self -> Instancia de la clase     
        '''

        try :
            # SI COLICIONA EL ATAQUE DEL ENEMIGO CON EL JUGADOR
            for burbuja in self.lista_enemigos[0].lista_burbuja:        
                if self.jugador.lados["left"].colliderect(burbuja.rect):
                    print("Una vuda menos")
                    self.vidas_jugador -= 0.5
                    burbuja.eliminar()

            # SI COLICIONA EL ATAQUE DEL ENEMIGO_DOS CON EL JUGADOR
            for lanza in self.lista_enemigos[1].lista_lanza:        
                if self.jugador.lados["left"].colliderect(lanza.rect):
                    print("Una vuda menos")
                    self.vidas_jugador -= 0.5
                    lanza.eliminar()


            # SI CAE "SI SOBREPASA LA PANTALLA EN ELE EJE Y"
            if self.jugador.rectangulo.y > 900:

                self.vidas_jugador -= 0.5

                for lado in self.jugador.lados:
                    self.jugador.lados[lado].y = 550
                    
                self.jugador.lados["top"].y = 580
                self.jugador.lados["left"].y = 580
                self.jugador.lados["right"].y = 580
                self.jugador.lados["bottom"].y = 650
            
        except AttributeError as e:
            print(f"Error en atributos: -> {e}  en funcion colicon_burbuja_jugador()")
            


    # COLICIONES MAS O MENOS VIDA
    def colicion_trampas_vida(self,lista_items,lista_trampas):
        '''
        Brief: Verifica las coliciones entre items y trampas modificando sumando o restando vidas,
        la puntuacion solo incrementa

        Parameters:
            self -> Instancia de la clase     
            lista_items -> lista a iterar para verifar su colicion. "Suma vidas"    
            lista_trampas -> lista a iterar para verifar su colicion. "Restando vidas"   
        '''
        try:
            # COLICION CON MONEDA
            for item in lista_items:
                if self.jugador.lados["bottom"].colliderect(item.lados["main"]):
                    print("CHAU MONEDA")
                    item.que_hace = "desaparce"
                    item.mover()
                    self.vidas_jugador += 1
                    self.puntos_jugador += 100

            # COLICIOON CON TRAMPA
            for trampa in lista_trampas:
                if self.jugador.lados["right"].colliderect(trampa.lados["right"]):
                    print("CHOQUE TRAMPA")
                    self.vidas_jugador -= 1

            if self.vidas_jugador < 0:
                self.vidas_jugador = 0
        except AttributeError as e:
            print(f"Error en atributos: -> {e}  en funcion colicion_trampas_vida()")
    
    # MARCADOR DE VIDA 
    def score(self,pantalla)->None:
        '''
        Brief: Muestra las vidas del jugador y del enemigo actualizados

        Parameters:
            self -> Instancia de la clase     
            pantalla -> Donde se va a blitear los cambios actualizados    
        '''
        fuente = pygame.font.SysFont("Forte",40)
        puntuacion = fuente.render(f"Kung Lao {self.vidas_jugador} ~ Enemigo {self.vidas_enemigo}",False,"White")
        pantalla.blit(puntuacion,(700,6))


    # PUNTOS
    def puntos(self,pantalla):
        '''
        Brief: Muestra los puntos acumulados del jugador actualizados

        Parameters:
            self -> Instancia de la clase     
            pantalla -> Donde se va a blitear los cambios actualizados    
        '''
        fuente = pygame.font.SysFont("Forte",30)
        puntuacion = fuente.render(f"Puntos: {self.puntos_jugador}",False,"White")
        pantalla.blit(puntuacion,(200,6))

    # GUARDAR EN TXT
    def guardar_partida(self):
        '''
        Brief: Guarda en un archivio la ultima puntucion del jugado

        Parameters:
            self -> Instancia de la clase   
        '''
        if self.vidas_enemigo == 0 or self.vidas_jugador == 0:
            with open("score.txt","w") as archivo:
                 archivo.write(str(self.puntos_jugador))
            
            self.dic_data["Posicion Jugador"] = self.jugador[2]
            self.dic_data["Vidas_jugador"] = self.vidas_jugador
            self.dic_data["Posicion Enemigo"] = self.lista_enemigos[0][2]
            self.dic_data["Vidas_Enemigo"] = self.vidas_enemigo
            # self.dic_data["Plataformas"] = self.plataformas
            # self.dic_data["Proyectil"] = self.sombrero.rect
            self.dic_data["Score"] = self.puntos_jugador
            self.dic_data["Cronometro"] = self.tiempo.__str__()
            self.dic_data["Items"] = {"trampa_uno"}
            # self.dic_data["Trampas"] = self.trampas

            self.guaradar_json()
    
    def guaradar_json(self):
        with open('data.json', 'w') as file:

            json.dump(self.dic_data, file, indent=4, ensure_ascii=False )