import pygame

class Cronometro:
    def __init__(self,tiempo_inicial) -> None:
        self.tiempo_acendente = tiempo_inicial
        self.minutos = 0
        self.fuente = pygame.font.SysFont("Forte",40)
        # self.relog = pygame.time.Clock()
        self.tiempo_actual = pygame.time.get_ticks()
        self.detenido = False

    def actualizar(self):
        if self.detenido == False:
            tiempo_trasncurrido = pygame.time.get_ticks() - self.tiempo_actual
            if tiempo_trasncurrido >= 1000:
                self.tiempo_actual = pygame.time.get_ticks()
                self.tiempo_acendente += 1

            if self.tiempo_acendente == 60:
                self.tiempo_acendente = 0
                self.minutos += 1


    def mostrar_tiempo(self,pantalla):
        cronometro = self.fuente.render(f"0{self.minutos} : {str(self.tiempo_acendente)}",False,"White")
        pantalla.blit(cronometro,(1500,6))

    def __str__(self) -> str:
        return f"{self.tiempo_acendente}"