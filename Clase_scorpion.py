import pygame
from Clase_enemigo import*


class Escorpion(Enemigo):
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad) -> None:
        super().__init__(tamaño, animaciones, posicion_inicial, velocidad)

        # SCORPION
        self.ataque = pygame.sprite.Group()
        self.lanza = ""

    
    def proyectil(self):
        self.lanza = Sombrero(r"Segundo-Parcail-Laboratorio\Scorpion_ataqua\4.png",(200,30),(self.rectangulo),30)
        self.ataque.add(self.lanza)

    def sonido(self):
        sonido_sombrero = pygame.mixer.Sound(r"Segundo-Parcail-Laboratorio\Musica\scorpion-get-over-here.mp3")
        sonido_sombrero.set_volume(0.2)
        canal = pygame.mixer.find_channel()
        canal.play(sonido_sombrero)