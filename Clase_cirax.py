import pygame
from Clase_enemigo import*


class Cirax(Enemigo):
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad) -> None:
        super().__init__(tamaño, animaciones, posicion_inicial, velocidad)

        # NOOD
        self.ataque = pygame.sprite.Group()
        self.nube_blanca = ""

    
    def proyectil(self,velocidad=30):
        self.nube_blanca = Sombrero(r"Segundo-Parcail-Laboratorio\Cirax_ataca\5.png",(50,30),(self.rectangulo),velocidad)
        self.ataque.add(self.nube_blanca)

    def sonido(self):
        sonido_sombrero = pygame.mixer.Sound(r"Segundo-Parcail-Laboratorio\Musica\mk3-07015.mp3")
        sonido_sombrero.set_volume(0.2)
        canal = pygame.mixer.find_channel()
        canal.play(sonido_sombrero)