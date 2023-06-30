import pygame
from configuraciones import obtener_rectangulos

class Sombrero(pygame.sprite.Sprite):
    def __init__(self,image,tamaño,posicion,velocidad) -> None:
        super().__init__()
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(self.ancho,self.alto))
        self.rect = self.image.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        self.lados_s = obtener_rectangulos(self.rect)
        self.velocidad = velocidad



    def update(self)->None:
        # print("H")
        self.rect.x += self.velocidad

        if self.rect.right > 1900:
            self.kill()


    def update_enemigo(self)->None:
        
        self.rect.x -= self.velocidad

        if self.rect.left < 1900:
            self.kill()
        
    def eliminar(self)->None:
        self.kill()
        