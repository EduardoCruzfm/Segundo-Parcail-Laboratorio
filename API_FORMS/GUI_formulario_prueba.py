
import pygame
from pygame.locals import*
from API_FORMS.GUI_form import*
from API_FORMS.GUI_textbox import*
from API_FORMS.GUI_label import*
from API_FORMS.GUI_button import*
from API_FORMS.GUI_slider import*
from API_FORMS.GUI_button_image import*
from API_FORMS.GUI_form_menu_score import*
from API_FORMS.GUI_forms_menu_play import*
from Nivel_Base import*
import sqlite3


class FormPrueba(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border = "Black", border_size = -1, active = True)->None:
        super().__init__( screen, x, y, w, h, color_background, color_border , border_size , active)

        self.volumen = 0.2
        self.flag_play = True
        self.flag_sql = True
        

        pygame.mixer.init()

        ############ CONTROLES ######
        self.txtbox = TextBox(self._slave,x,y,100,50,150,30,"White","White","Red",(70,59,59),2,font= "Comic Sans",font_size=15,font_color="Black")
        self.btn_play = Button(self._slave,x,y,100,100,150,50,(70,59,59),"Blue",self.btn_play_click,"Nombre","Pausa",font="Verdana",font_size=15,font_color="White")
        self.label_volumen = Label(self._slave, 650, 190, 100, 50 ,"20%","Comic Sans",15,"White",r"Segundo-Parcail-Laboratorio\Menu\6.png" )
        self.slider_volumen = Slider(self._slave,x,y,100,200,500,15,self.volumen,(70,59,59),"White")
        self.btn_tabla = Button_Image(self._slave,x,y,375,100,50,50,r"Segundo-Parcail-Laboratorio\Menu\0.png",self.btn_tabla_click,"lala")
        # picture box 

        self.btn_jugar = Button_Image(self._slave,x,y,300,100,50,50,r"Segundo-Parcail-Laboratorio\Moneda_vida\2.png",self.btn_jugar_click,"a")
        ############

        # AGRERGARLOS A LA LISTA
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_jugar)

        

        pygame.mixer.music.load(r"Segundo-Parcail-Laboratorio\Musica\21_Kombat Temple.mp3")
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
       
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = (105,87,87)
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


    def btn_jugar_click(self,param):
        form_jugar = FormMenuPlay(screen=self._master,
                                  x= self._master.get_width() / 2 - 250,
                                  y= self._master.get_height() / 2 - 250,
                                  w= 500,
                                  h= 500,
                                  color_background= (220,0,220),
                                  color_border= (255,255,255),
                                  active= True,
                                  path_image= r"Segundo-Parcail-Laboratorio\Menu\0.png")
        
        print("Jugar")
        
        # CREAMOS BD
        if self.flag_sql == True:
            with sqlite3.connect("mi_base_de_datos.db") as conexion:
                # CREAR TABLA--------------------------
                try:
                    sentencia = 'create table Ranking (nombre text,score integer)'

                    conexion.execute(sentencia)
                    print("Tabla creada")
                except Exception as e:
                    print(f"Error en Base de datos {e}")
            self.flag_sql = False


        self.show_dialog(form_jugar)



    def btn_tabla_click(self,texto):

        # dic_score = [{"jugador" : f"{self.txtbox.get_text()}","Score":f"{slice}"},]
        
        nombre = self.txtbox.get_text()
        ultimo_score = []
        
        # ACCEDO AL ULTIMO SCORE
        archivo = open("score.txt","r")
        for linea in archivo:
            ultimo_score.append(linea)
        
        archivo.close()  
            
    
        
        # INSERTO EN BD
        with sqlite3.connect("mi_base_de_datos.db") as conexion:
            try:
                sentencia = ' insert into Ranking (nombre, score) values(?,?)'

                conexion.execute(sentencia,(nombre,ultimo_score[0]))

            except Exception as e:
                print(f"Error en Base de datos {e}")
        


        dic_score = []

        with sqlite3.connect("mi_base_de_datos.db") as conexion:
            try:
                
                sentencia = '''
                            select * from Ranking order by score desc limit 3
                            '''
                cursor = conexion.execute(sentencia)
                for fila in cursor:
                    # print(fila)

                    dic_score.append({"jugador" : f"{fila[0]}","Score":f"{fila[1]}"},)


                print("Tabla creada")
            except Exception as e:
                print(f"Error en Base de datos {e}")
        
        # print("EDU")
   
        form_puntaje = FormMenuScore(self._master,690,205,500,550,(220,0,220),"white",True,r"Segundo-Parcail-Laboratorio\Menu\0.png",dic_score,100,10,10)
        self.show_dialog(form_puntaje)