import pygame
from Clases import*
from Clase_proyectil import*

class Enemigo(Personaje):
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad) -> None:
        super().__init__(tamaño, animaciones, posicion_inicial, velocidad)
        # SHAO
        self.lista_burbuja = pygame.sprite.Group()
        self.burbuja_verde = ""
        # SCORPION
        self.lista_lanza = pygame.sprite.Group()
        self.lanza = ""
        # NOOD
        self.lista_cuchillo = pygame.sprite.Group()
        self.cuchillos = ""



    def animar(self,pantalla,que_animacio:str):
        animacion = self.animaciones[que_animacio]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos],self.lados["main"])
        self.contador_pasos += 1


    def update(self,pantalla,lista_plataformas):
        match self.que_hace:

            case "ataca":     
                    self.animar(pantalla,"gira_ataca")
                    # self.burbuja()

            case "quieto":
                    self.animar(pantalla,"quieto")
                
            case "ataca_derecha":
                  self.animar(pantalla,"camina_derecha")
                  

        self.aplicar_gravedad(pantalla,lista_plataformas)
        self.limites_x_enemigo()


    def burbuja(self):
        self.burbuja_verde = Sombrero(r"Segundo-Parcail-Laboratorio\Ataque_Shao_kanh\0.png",(30,30),(self.rectangulo),-30)
        self.lista_burbuja.add(self.burbuja_verde)

    def scorpion(self):
        self.lanza = Sombrero(r"Segundo-Parcail-Laboratorio\Scorpion_ataqua\4.png",(200,30),(self.rectangulo),30)
        self.lista_lanza.add(self.lanza)

    def cuchillo(self):
        self.cuchillos = Sombrero(r"Segundo-Parcail-Laboratorio\Nood_ataca\7.png",(200,30),(self.rectangulo),30)
        self.lista_cuchillo.add(self.cuchillos)

    def mover_x(self,velocidad):
         
         for lado in self.lados:
            self.lados[lado].x += velocidad 

    def limites_x_enemigo(self):
        if self.rectangulo.x > 1600:
            self.mover_x(-100)

        if self.rectangulo.x < 100:
            self.mover_x(100)