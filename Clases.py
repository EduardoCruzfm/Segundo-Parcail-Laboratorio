import pygame
from configuraciones import reescalar_imagen, obtener_rectangulos
from Clase_proyectil import*
from configuracion_item_trampa import*

class Personaje:
    def __init__(self,tamaño,animaciones,posicion_inicial,velocidad)->None:
        # CONFECCION DEL PERSONAJE
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        # GRAVEDAD
        self.gravedad = 1
        self.potencia_salto = -20
        self.limite_velocidad_caida = 20
        self.esta_saltando = False
        # ANIMACIONES
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        # RECTANGULOS
        # tomamos cualquier animacion para obtener el ractangulo
        # rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        self.rectangulo = self.animaciones["quieto"][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        # OBTENGO TODOS LOS LADOS DEL RECTANGULO CREADO, APARTI DE UNA ANIMACION DE UNA DE LAS LISTAS
        self.lados = obtener_rectangulos(self.rectangulo)
        # MOVIMIENTO
        self.velocidad = velocidad  #DESPLACAMIENTO EN X
        self.desplazamiento_y = 0   #DESPLAZAMIENTO EN Y
        # GROUP
        self.lista_sombrero = pygame.sprite.Group()
        self.sombrero_ataque = ""
        self._lista = [tamaño,animaciones,posicion_inicial,velocidad]


    def __getitem__(self,index)-> str:
        return self._lista[index]

    def reescalar_animaciones(self):
        # POR CADA CLAVE EN EL DICCIONARIO
        for clave in self.animaciones:
            # self.animaciones[clave] ES CADA LISTA EN EL DICCIONARIO: QUIETO,SALTA....
            reescalar_imagen(self.animaciones[clave], self.ancho, self.alto)


    def animar(self,pantalla,que_animacio:str):
        animacion = self.animaciones[que_animacio]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos],self.lados["main"])
        self.contador_pasos += 1


    def mover(self,velocidad):
        # izquierda y derecha
        # MUEVO A TODOS LOS LADOS
        for lado in self.lados:
            self.lados[lado].x += velocidad 

    def update(self,pantalla,lista_plataformas):
        match self.que_hace:
            case "derecha":
                if not self.esta_saltando:
                    self.animar(pantalla,"camina_derecha")
                self.mover(self.velocidad)
            case "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla,"camina_izquierda")
                self.mover(self.velocidad * -1)
            case "salta":
                if not self.esta_saltando:
                    self.animar(pantalla,"salta")
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    sonido_sombrero = pygame.mixer.Sound(r"Segundo-Parcail-Laboratorio\Musica\sfx_KL_fat1_poseL.wav")
                    sonido_sombrero.set_volume(0.2)
                    canal = pygame.mixer.find_channel()
                    canal.play(sonido_sombrero)
            case "gira_ataca":
                if not self.esta_saltando:
                    self.animar(pantalla,"gira_ataca")

            case "quieto":
                if not self.esta_saltando:
              
                    self.animar(pantalla,"quieto")
            case "quieto":#-------------------------
                if not self.esta_saltando:
                    self.animar(pantalla,"quieto")

            case "sombrero":
                if not self.esta_saltando:
                    self.animar(pantalla,"sombrero_ataca")
                    self.sombrero()
                    
                    sonido_sombrero = pygame.mixer.Sound(r"Segundo-Parcail-Laboratorio\Musica\sfx_KL_charselect_hat_catch.wav")
                    sonido_sombrero.set_volume(0.2)
                    canal = pygame.mixer.find_channel()
                    canal.play(sonido_sombrero)

       
        self.aplicar_gravedad(pantalla,lista_plataformas)
            

    def aplicar_gravedad(self,pantalla,lista_plataformas):
        # salto y caida y ....
        if self.esta_saltando:
            self.animar(pantalla,"salta")

            # SUBIDA
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            
            #  BAJADA [SERIA PUEDO SEGUIR CALLENDO?]
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                # CAE A UN PIXEL DE GRAVEDAD
                self.desplazamiento_y += self.gravedad

        # COLICION-------------falta un for

        for piso in lista_plataformas:
            if self.lados["bottom"].colliderect(piso.plataforma_lados["top"]):
                # PARA QUE DEJE DE DESENDER EN EL EJE Y
                self.desplazamiento_y = 0
                # CAMBIAMOS EL ESTADO COMFIRMANDO QUE DEJO DE SALTAR
                self.esta_saltando = False
                # POSICIONAR EL BOTTOM DEL PERSONAJE EN EÑ TOP DEL PISO
                self.lados["main"].bottom = piso.plataforma_lados["main"].top + 5
                break
            #------programar si algo me choca o un ataque de colicion
                
            else:
                self.esta_saltando = True 

            
        # colicon de enemigo  y personaje

    def sombrero(self):
        
        self.sombrero_ataque = Sombrero(r"Segundo-Parcail-Laboratorio\Sombrero\3.png",(30,30),(self.rectangulo),20)
        self.lista_sombrero.add(self.sombrero_ataque)

       
        

       
