import pygame
from Clase_enemigo import*


class Sub(Enemigo):
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad) -> None:
        super().__init__(tamaño, animaciones, posicion_inicial, velocidad)

        # SUB
        self.ataque = pygame.sprite.Group()
        self.hielo = ""

    
    def proyectil(self,velocidad=30):
        self.hielo = Sombrero(r"Segundo-Parcail-Laboratorio\Sub_ataca\5.png",(50,50),(self.rectangulo),velocidad)
        self.ataque.add(self.hielo)

    def sonido(self):
        sonido_sombrero = pygame.mixer.Sound(r"Segundo-Parcail-Laboratorio\Musica\Sub_Zero_Freeze_Sound_Effect.mp3")
        sonido_sombrero.set_volume(0.2)
        canal = pygame.mixer.find_channel()
        canal.play(sonido_sombrero)