import pygame
from pygame.locals import*

from GUI_button import* 
# NO se instancia la base jerarquia
class Form(Widget):
    def __init__(self,screen,x,y,w,h,color_background,color_border="Black",borde_size=-1,active=True):
        super().__init__(self,screen,x,y,w,h,color_background,color_border,borde_size)
        self._slave = pygame.Surface((w,h)) 
        self._slave_rect = self._slave.get_rect() 
        self. _slave_rect.x = x
        self. _slave_rect.y = y
        self.active = active 
        self.lista_widgets = [] 
        self.hijo = None
        self.dialog_result = None 
        self.padre = None

    def show_dialog(self,formulario):
        self.hijo = formulario
        self.hijo.padre = self

    def end_dialog(self):
        self.dialog_result = "Ok"
        self.close()

    def close(self):
        self.active = False

    def verificar_dialog_result(self):
        return self.hijo == None or self.hijo.dialog_result != None
    
    def render(self):
        pass

    def update(self, lista_eventos):
        pass