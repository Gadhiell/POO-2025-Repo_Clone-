import pygame
import random
from settings import SCREEN_WIDHT, SCREEN_HEIGHT, METEOR_SPEED

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (15, 15), 15)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDHT - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += METEOR_SPEED

        # Si el meteorito sale de la pantalla, se elimina
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()