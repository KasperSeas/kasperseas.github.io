import pygame
import math

class Tree_Stump(pygame.sprite.Sprite):
    
    def __init__(self, position, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/environment/tree_stump.png").convert_alpha()
        self.rect = pygame.Rect(0,0,60,60)
        self.rect.move_ip(0, 30)
        self.rect.x = position[0]
        self.rect.y = position[1]
    
    
    