import pygame
import math

class Invisible_Wall(pygame.sprite.DirtySprite):
    """
    Invisible barriers that the penguins can't pass
    """
    def __init__(self, position, screen):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.Surface([30, 30])
        self.image.fill(pygame.Color(0,0,0))
        self.image.set_colorkey(pygame.Color(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.dirty = 1
    
    