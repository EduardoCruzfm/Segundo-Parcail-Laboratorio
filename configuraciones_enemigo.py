import pygame
from configuraciones import reescalar_imagen,obtener_rectangulos,girar_imagenes

#--------------------------Shao_Kahn------------------------------------

enemigo_quieto = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Shao_Kahn_quieto\0.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Shao_Kahn_quieto\1.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Shao_Kahn_quieto\2.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Shao_Kahn_quieto\3.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Shao_Kahn_quieto\3.png")                  
                  ]

enemigo_quieto_izquierda = girar_imagenes(enemigo_quieto,True,False)

enemigo_camina = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Shao_kahn_camina\0.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Shao_kahn_camina\1.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Shao_kahn_camina\2.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Shao_kahn_camina\3.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Shao_kahn_camina\4.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Shao_kahn_camina\5.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Shao_kahn_camina\6.png")
                ]

enemigo_camina_izquierda = girar_imagenes(enemigo_camina,True,False)

enemigo_ataca = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Shao_Kahn_ataca\0.png"),
                 pygame.image.load(r"Segundo-Parcail-Laboratorio\Shao_Kahn_ataca\1.png"),  
                 pygame.image.load(r"Segundo-Parcail-Laboratorio\Shao_Kahn_ataca\2.png"), 
                 pygame.image.load(r"Segundo-Parcail-Laboratorio\Shao_Kahn_ataca\3.png"),  
                 pygame.image.load(r"Segundo-Parcail-Laboratorio\Shao_Kahn_ataca\4.png")  
                ]

enemigo_ataca_izquieda = girar_imagenes(enemigo_ataca,True,False)

# ---------------------Scorpion---------------------------------

scorpion_quieto = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Scorpion_quieto\0.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Scorpion_quieto\1.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Scorpion_quieto\2.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Scorpion_quieto\3.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Scorpion_quieto\4.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Scorpion_quieto\5.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Scorpion_quieto\6.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Scorpion_quieto\7.png")
                                   
                  ]

scorpion_ataca = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Scorpion_ataqua\0.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Scorpion_ataqua\1.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Scorpion_ataqua\2.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Scorpion_ataqua\3.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Scorpion_ataqua\4.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Scorpion_ataqua\6.png"),
                  pygame.image.load(r"Segundo-Parcail-Laboratorio\Scorpion_ataqua\7.png")
                                   
                  ]
# ---------------------Nood---------------------------------

nood_quieto = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_quieto\0.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_quieto\1.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_quieto\2.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_quieto\3.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_quieto\4.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_quieto\5.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_quieto\6.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_quieto\7.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_quieto\8.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_quieto\9.png")                   
                  ]

nood_ataca = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_ataca\0.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_ataca\1.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_ataca\2.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_ataca\3.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_ataca\4.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_ataca\5.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_ataca\6.png")
              ]

# ---------------------Motaro---------------------------------

motaro_quieto = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Motaro_quieto\0.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Motaro_quieto\1.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Motaro_quieto\2.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Motaro_quieto\3.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Motaro_quieto\4.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Motaro_quieto\5.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Motaro_quieto\6.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Motaro_quieto\7.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Motaro_quieto\8.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Motaro_quieto\9.png")             
              ]

motaro_ataca = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Motaro_ataca\0.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Motaro_ataca\1.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Motaro_ataca\2.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Motaro_ataca\3.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Motaro_ataca\4.png")            
              ]

motaro_quieto_izquieda = girar_imagenes(motaro_quieto,True,False)
motaro_ataca_izquieda = girar_imagenes(motaro_ataca,True,False)