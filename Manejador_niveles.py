import pygame
from pygame.locals import*
from Nivel_Uno import NivelUno
from Nivel_Dos import NivelDos
from Nivel_Tres import NivelTres

class Manejador_niveles:
    def __init__(self, pantalla) -> None:
        self._slave = pantalla
        self.niveles = {"nivel_uno": NivelUno, "nivel_dos": NivelDos, "nivel_tres": NivelTres}


    def get_nivel(self,nombre_nivel):
        # NivelUno(pantalla) es lo mismo que 
        return self.niveles[nombre_nivel](self._slave)
        # Nos ayuda a instanciar los niveles

