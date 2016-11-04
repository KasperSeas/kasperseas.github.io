import pygame
import math

class Rock(pygame.sprite.DirtySprite):
    
    def __init__(self, position):
        pygame.sprite.DirtySprite.__init__(self)
        #self.image = pygame.image.load("images/environment/sd_rocks.png").convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        
        self.dirty = 1
       
    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect.x, self.rect.y)
    
class Icecube(pygame.sprite.DirtySprite):
    
    def __init__(self, position):
        pygame.sprite.DirtySprite.__init__(self)
        #self.image = pygame.image.load("images/environment/icecube.png").convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
       
    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect.x, self.rect.y)