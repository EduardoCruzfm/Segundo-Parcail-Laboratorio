import pygame

########################################################################## FileNotFoundError

def reescalar_imagen(lista_imagenes:list,W:int,H:int)->None: #-------------> W;H puede ser un solo parametro = tamaño:tupla

    for i  in range(len(lista_imagenes)):
        # ESCALAMOS CADA IMAGEN DE LA LISTA AL TAMAÑO QUE LE PASEMOS
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i],(W,H))


def girar_imagenes(lista_original:list,flip_x:bool,flip_y:bool)->list:

    lista_girada = []
    for imagen in lista_original:
        # EL METODO FLIP DA VUELTA CUALQUIER SUPEFICIE QUE LE PASE
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

def obtener_rectangulos(pricipal)->dict:
    diccionario = {}
    diccionario["main"] = pricipal
    #                                   IZQUIERDA    ,     TOP    ,     ANCHO      , ALTO        
    diccionario["bottom"] = pygame.Rect(pricipal.left,pricipal.bottom - 10,pricipal.width,10)
    diccionario["right"] = pygame.Rect(pricipal.right - 10,pricipal.top,10,pricipal.height)
    diccionario["left"] = pygame.Rect(pricipal.left ,pricipal.top,5,pricipal.height)
    diccionario["top"] = pygame.Rect(pricipal.left ,pricipal.top,pricipal.width,10)
    return diccionario


##########################################################################

# DEFINIMOS LOS FOTOGRAMAS:

# QUIETO
personaje_quieto = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Quieto\0.png"),
                    pygame.image.load(r"Segundo-Parcail-Laboratorio\Quieto\1.png"),
                    pygame.image.load(r"Segundo-Parcail-Laboratorio\Quieto\2.png"),
                    pygame.image.load(r"Segundo-Parcail-Laboratorio\Quieto\3.png"),
                    pygame.image.load(r"Segundo-Parcail-Laboratorio\Quieto\4.png"),
                    pygame.image.load(r"Segundo-Parcail-Laboratorio\Quieto\5.png"),
                    pygame.image.load(r"Segundo-Parcail-Laboratorio\Quieto\6.png")
                    
                    ]

personaje_quieto_izquierda = girar_imagenes(personaje_quieto,True,False)


# CAMINA
personaje_camina = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Camina_Adelante\0.png"),
                    pygame.image.load(r"Segundo-Parcail-Laboratorio\Camina_Adelante\1.png"),
                    pygame.image.load(r"Segundo-Parcail-Laboratorio\Camina_Adelante\2.png"),
                    pygame.image.load(r"Segundo-Parcail-Laboratorio\Camina_Adelante\3.png"),
                    pygame.image.load(r"Segundo-Parcail-Laboratorio\Camina_Adelante\4.png"),
                    pygame.image.load(r"Segundo-Parcail-Laboratorio\Camina_Adelante\5.png")
                    ]

personaje_camina_izquiera = girar_imagenes(personaje_camina,True,False)


# SALTA
personaje_salta = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Salta\0.png"),
                   pygame.image.load(r"Segundo-Parcail-Laboratorio\Salta\1.png"),
                   pygame.image.load(r"Segundo-Parcail-Laboratorio\Salta\2.png"),
                   pygame.image.load(r"Segundo-Parcail-Laboratorio\Salta\3.png"),
                   pygame.image.load(r"Segundo-Parcail-Laboratorio\Salta\4.png"),
                   pygame.image.load(r"Segundo-Parcail-Laboratorio\Salta\5.png"),
                   pygame.image.load(r"Segundo-Parcail-Laboratorio\Salta\6.png"),
                   pygame.image.load(r"Segundo-Parcail-Laboratorio\Salta\7.png"),
                   pygame.image.load(r"Segundo-Parcail-Laboratorio\Salta\8.png"),
                   pygame.image.load(r"Segundo-Parcail-Laboratorio\Salta\9.png"),
                   
                   ]

personaje_salta_izquierda = girar_imagenes(personaje_salta,True,False)

personaje_gira_ataque = [pygame.image.load(r"Segundo-Parcail-Laboratorio\gira_ataque\0.png"),
                         pygame.image.load(r"Segundo-Parcail-Laboratorio\gira_ataque\1.png"),
                         pygame.image.load(r"Segundo-Parcail-Laboratorio\gira_ataque\2.png"),
                         pygame.image.load(r"Segundo-Parcail-Laboratorio\gira_ataque\3.png")
                    ]

personaje_sombrero = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Ataque_sombrero\0.png"),
                      pygame.image.load(r"Segundo-Parcail-Laboratorio\Ataque_sombrero\1.png")
                                        
                    ]