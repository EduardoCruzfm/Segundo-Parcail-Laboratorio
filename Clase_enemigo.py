import pygame
from Clases import*
from Clase_proyectil import*

class Enemigo(Personaje):
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad) -> None:
        super().__init__(tamaño, animaciones, posicion_inicial, velocidad)
        # SHAO
        self.ataque = pygame.sprite.Group()
        self.burbuja_verde = ""
       
        
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
                    self.animar(pantalla,"camina_derecha")
                    # self.sonido()
            case "quieto":
                    self.animar(pantalla,"quieto")
                
            case "ataca_derecha":
                  self.animar(pantalla,"gira_ataca")
                  

        self.aplicar_gravedad(pantalla,lista_plataformas)
        self.limites_x_enemigo()


    def proyectil(self,velocidad=30):
        self.burbuja_verde = Sombrero(r"Segundo-Parcail-Laboratorio\Ataque_Shao_kanh\0.png",(30,30),(self.rectangulo),velocidad)
        self.ataque.add(self.burbuja_verde)

    

    def mover_x(self,velocidad):
         
         for lado in self.lados:
            self.lados[lado].x += velocidad 

    def limites_x_enemigo(self):
        if self.rectangulo.x > 1600:
            self.mover_x(-100)

        if self.rectangulo.x < 100:
            self.mover_x(100)

    def sonido(self):
        sonido_sombrero = pygame.mixer.Sound(r"Segundo-Parcail-Laboratorio\Musica\sfx_KL_dive_kick_whsh01.wav")
        sonido_sombrero.set_volume(0.2)
        canal = pygame.mixer.find_channel()
        canal.play(sonido_sombrero)