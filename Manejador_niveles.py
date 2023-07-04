import pygame
from pygame.locals import*
from Nivel_Uno import NivelUno
from Nivel_Dos import NivelDos
from Nivel_Tres import NivelTres

class Manejador_niveles:
    def __init__(self, pantalla) -> None:
        self._slave = pantalla
        self.niveles = {"nivel_uno": NivelUno, "nivel_dos": NivelDos, "nivel_tres": NivelTres}

        self.nivel_uno = None  
        

    # def get_nivel(self,nombre_nivel):
    #     # NivelUno(pantalla) es lo mismo que 
    #     return self.niveles[nombre_nivel](self._slave)
    #     # Nos ayuda a instanciar los niveles

    def get_nivel_1(self):
        # NivelUno(pantalla) es lo mismo que 
        return self.niveles["nivel_uno"](self._slave)
    # def get_nivel_1(self):
    #     if self.nivel_uno is None:
    #         self.nivel_uno = self.niveles["nivel_uno"](self._slave)
    #     return self.nivel_uno
    
    
    def get_nivel_2(self):
        # NivelUno(pantalla) es lo mismo que 
        return self.niveles["nivel_dos"](self._slave)
    
    def get_nivel_3(self):
        # NivelUno(pantalla) es lo mismo que 
        return self.niveles["nivel_tres"](self._slave)

