import pygame
from Clase_enemigo import*


class Nood(Enemigo):
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad) -> None:
        super().__init__(tamaño, animaciones, posicion_inicial, velocidad)

        # NOOD
        self.ataque = pygame.sprite.Group()
        self.cuchillos = ""

    
    def proyectil(self):
        self.cuchillos = Sombrero(r"Segundo-Parcail-Laboratorio\Nood_ataca\7.png",(50,10),(self.rectangulo),30)
        self.ataque.add(self.cuchillos)