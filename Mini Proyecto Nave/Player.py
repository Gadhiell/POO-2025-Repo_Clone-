import Player
from settings import SCREEN_WIDHT, SCREEN_HEIGHT, PLAYER_SPEED #settings no tiene clases,asi que se tiene que invocar las variables globales a ocupar

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #atributos de la nave
        self.image = pygame.Surface((50, 50),pygame)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDHT // 2 #Aparece a la mitad de la pantalla
        self.rect.bottom =  SCREEN_HEIGHT - 10
        
        #Dibujar Triangulo
        pygame.draw.polygon(self.image, (0,0,255) [(25,0),(0,50),(50,50)])
        
        def update (self):
            kets = pygame.ket.get_pressed()
            
        #Teclas ocupadas
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGT]:
            self.rect.x += PLAYER_SPEED
            
        #
        if self.rect.left < 0
        self.rect.left = 0
        if self
            