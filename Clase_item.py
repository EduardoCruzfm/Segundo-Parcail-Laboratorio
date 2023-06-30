import pygame
from configuraciones import reescalar_imagen, obtener_rectangulos

class Item:
    def __init__(self,tamaño,animaciones,posicion_inicial) -> None:
        # CONFECCION DEL ITEM
        self.ancho = tamaño[0]
        self.alto = tamaño[1]

        # ANIMACIONES
        self.contador_pasos = 0
        self.que_hace = "gira"
        self.animaciones = animaciones
        self.reescalar_animaciones()

        # RECTANGULOS
        rectangulo = self.animaciones["gira"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]

        self.lados = obtener_rectangulos(rectangulo)
      

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

    def mover(self):
        # izquierda y derecha
        # MUEVO A TODOS LOS LADOS
        for lado in self.lados:
            self.lados[lado].y += 40


    def update(self,pantalla):
            
        match self.que_hace:
            case "gira":
                self.animar(pantalla,"gira")

            case "desaparce":
                pass
            
                
            
                
           
