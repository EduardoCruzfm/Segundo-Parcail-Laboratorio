import pygame
from Clase_enemigo import*


class Nood(Enemigo):
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad) -> None:
        super().__init__(tamaño, animaciones, posicion_inicial, velocidad)

        # NOOD
        self.ataque = pygame.sprite.Group()
        self.cuchillos = ""

    
    def proyectil(self,velocidad=30):
        self.cuchillos = Sombrero(r"Segundo-Parcail-Laboratorio\Ataque_Shao_kanh\0.png",(50,50),(self.rectangulo),velocidad)
        self.ataque.add(self.cuchillos)

    def sonido(self):
        sonido_sombrero = pygame.mixer.Sound(r"Segundo-Parcail-Laboratorio\Musica\mk2-00842.mp3")
        sonido_sombrero.set_volume(0.2)
        canal = pygame.mixer.find_channel()
        canal.play(sonido_sombrero)