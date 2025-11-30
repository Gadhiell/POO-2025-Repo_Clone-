import pygame
import random
from settings import SCREEN_HEIGHT, SCREEN_WIDHT, BLACK, METEOR_FREQUENCY  
from settings import se





class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Nave VS Meteorito")
        self.clock =  pygame.time.Clock()
        
        
        self.all_sprites = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()
        
        self.player = Player()
        self.all_sprites.add(self.player)
        
    def run (self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                    #Generacion de meteoritos
                    if random.randint (1, METEOR_FREQUENCY) == 1:
                        meteor = Meteor()
                        self.all_sprites(meteor)
                        self.meteor.add(meteor)
                        
                        #Actualizacion de todas las posiciones
                        self.all_sprites.update()
                        
                        #Logica para corroborar colisiones
                        if pygame.sprite.spritecollide(self.player, self,meteor, False):
                            print ("Game Over")
                            running = False
                            
                            #Dibujando sprites
                            self.screen.fill(BLACK)
                            self.all_sprites.draw(self, Screen)