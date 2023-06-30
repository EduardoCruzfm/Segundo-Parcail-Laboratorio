import pygame
from Clase_item import*

class Trampa(Item):
    def __init__(self, tamaño, animaciones, posicion_inicial) -> None:
        super().__init__(tamaño, animaciones, posicion_inicial)