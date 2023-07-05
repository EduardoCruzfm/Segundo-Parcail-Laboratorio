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

nood_salta = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_salta\0.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_salta\1.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_salta\2.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_salta\3.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_salta\4.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_salta\5.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_salta\6.png")
              
              ]

nood_combo = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\0.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\1.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\2.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\3.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\4.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\5.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\6.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\7.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\8.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\9.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\10.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\11.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\12.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\13.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\14.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\15.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\16.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\17.png"),
                pygame.image.load(r"Segundo-Parcail-Laboratorio\Nood_combo\18.png")
               
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

# ---------------------Sub---------------------------------

sub_quieto = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_quieto\0.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_quieto\1.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_quieto\2.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_quieto\3.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_quieto\4.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_quieto\5.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_quieto\6.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_quieto\7.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_quieto\8.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_quieto\9.png")                          
              ]

sub_ataca = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_ataca\0.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_ataca\1.png"),           
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_ataca\2.png"),           
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_ataca\3.png"),           
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_ataca\4.png")         
              ]

sub_ataca_izquierda = girar_imagenes(sub_ataca,True,False)

sub_salta = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_salta\0.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_salta\1.png"),           
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_salta\2.png"),           
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Sub_salta\3.png")           
                   
              ]
#  ---------------------Cirax---------------------------------

cirax_quieto = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Cirax_quieto\0.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Cirax_quieto\1.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Cirax_quieto\2.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Cirax_quieto\3.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Cirax_quieto\4.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Cirax_quieto\5.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Cirax_quieto\6.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Cirax_quieto\7.png")
                                        
              ]

cirax_ataca = [pygame.image.load(r"Segundo-Parcail-Laboratorio\Cirax_ataca\0.png"),
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Cirax_ataca\1.png"),           
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Cirax_ataca\2.png"),           
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Cirax_ataca\3.png"),           
              pygame.image.load(r"Segundo-Parcail-Laboratorio\Cirax_ataca\4.png")        
              ]

cirax_ataca_izquierda = girar_imagenes(cirax_ataca,True,False)