import pygame
class Circulo_Chico:
    def __init__ (self, x, y, ancho, alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 1
        self.color (0, 255, 000)
        
    def dibujar (Self, ventana):
        pygame.draw.circle(ventana, self.color, self.rect)
        
    def mover (Self, teclas):
        move_x = 0
        move_y = 0
        
        if teclas [pygame.K_a]:
            move_x = -1
        if teclas [pygame.K_a]:
            move_x = 1
        if teclas [pygame.K_w]:
            move_y = -1
        if teclas [pygame.K_s]:
            move_y = -1
            