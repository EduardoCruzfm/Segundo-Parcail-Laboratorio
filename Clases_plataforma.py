import pygame
from configuraciones import obtener_rectangulos

class Plataforma:
    def __init__(self,ruta_imagen,W,H,posicion)->None:
        self.ancho = W
        self.alto = H
        self.imagen = pygame.image.load(ruta_imagen)
        self.imagen = pygame.transform.scale(self.imagen,(self.ancho, self.alto)) 

        self.rectangulo_plataforma = self.imagen.get_rect()
        self.rectangulo_plataforma.x = posicion[0]
        self.rectangulo_plataforma.y = posicion[1]

        self.plataforma_lados = obtener_rectangulos(self.rectangulo_plataforma)
      

