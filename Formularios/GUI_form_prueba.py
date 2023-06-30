import pygame
from pygame.locals import*

from GUI_button import*
from GUI_slider import*
from GUI_textbox import*
from GUI_label import*
from GUI_form import*
from GUI_button_image import*
from GUI_form_menu_score import*


class FormPrueba(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border = "Black", border_size = -1, active = True)->None:
        super().__init__( screen, x, y, w, h, color_background, color_border , border_size , active)

        self.volumen = 0.2
        self.flag_play = True

        pygame.mixer.init()

        ############ CONTROLES ######
        self.txtbox = TextBox(self._slave,x,y,50,50,150,30,"Gray","White","Red","Blue",2,font= "Comic Sans",font_size=15,font_color="Black")
        self.btn_play = Button(self._slave,x,y,100,100,150,50,"Red","Blue",self.btn_play_click,"Nombre","Pausa",font="Verdana",font_size=15,font_color="White")
        self.label_volumen = Label(self._slave, 650, 190, 100, 50 ,"20%","Comic Sans",15,"White",r"TP_Juego\Menu\6.png" )
        self.slider_volumen = Slider(self._slave,x,y,100,200,500,15,self.volumen,"Blue","White")
        self.btn_tabla = Button_Image(self._slave,x,y,255,100,50,50,r"TP_Juego\Menu\0.png",self.btn_tabla_click,"lala")
 
        ############

        # AGRERGARLOS A LA LISTA
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)

        

        pygame.mixer.music.load("musica_de_fondo")

        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.render()

    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()

                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
            self.upadte_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)


    def render(self):
        self._slave.fill(self._color_background)


    def btn_play_click(self,texto):
        # nombre = self.txtbox.get_text()
        # print(nombre)
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "Cyan"
            self.btn_play._font_color = "Red"
            self.btn_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Red"
            self.btn_play._font_color = "White"
            self.btn_play.set_text("Pause")

        self.flag_play = not self.flag_play

    def upadte_volumen(self,lista_eventos):
        self.volumen = self.slider_volumen.value
        # self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)


    def btn_tabla_click(self,texto):
        dic_score = [{"jugador" : "Gio","Score":1000},
                     {"jugador" : "Fausto","Score":900},
                     {"jugador" : "Gonza","Score":750}
                     ]
        

        form_puntaje = FormMenuScore(self._master,250,25,500,550,(220,0,220),"white",True,"ventana.png",dic_score,100,10,10)
        self.show_dialog(form_puntaje)