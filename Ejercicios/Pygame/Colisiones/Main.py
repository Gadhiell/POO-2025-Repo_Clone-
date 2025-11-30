import pygame
from Circulo_Chico import Circulo_Chico
from Circulo_Grande import Circulo_Grande

pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Colision Rectangular En Pygame")

background = (30,30,30)
color_colision (234, 63, 63) #Rojo

#instancias de los rectangulos
Chico = Rectangulo0 (200, 200, 100, 50)
Grande = Rectangulo1 (200, 200, 150, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    teclas = pygame.key.get_pressed_()
    
    pos_anterior_chico = rectangulo_chico.obtener_posicion ()
    pos_anterior_grande = rectangulo_grande.obtener_posicion ()
    
    rectangulo_chico.mover (teclas)      
    rectangulo_grande.mover (teclas)       
    if 
            
            
            
            Circulo_Chico.restablecer_posicion(*pos_anterior_chico)
            Circulo_Grande.restablecer_posicion(*pos_anterior_grande)
            Circulo_Chico.cambiar_color(color_colision)
            Circulo_Grande.cambiar_color(color_colision)
            
        ventana.fill(background)
        rectangulo_chico
        rectangulo_grande