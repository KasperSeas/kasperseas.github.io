import pygame
import math

class Health_Bar(pygame.sprite.DirtySprite):
    """Health bar of the penguins"""
    def __init__(self, position, max_health, all_sprites_group):
        pygame.sprite.DirtySprite.__init__(self)
        all_sprites_group.add(self)
        self.image = pygame.Surface([30, 5])
        self.image.fill(pygame.Color(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.health = max_health
        self.max_health = max_health
        
        self.dirty = 1
        
    def update(self):
        self.dirty = 1
        surf = pygame.Surface([self.max_health, 5])
        surf.fill(pygame.Color(250,0,0))
        surf2 = pygame.Surface([self.health, 5])
        surf2.fill(pygame.Color(0,250,0))
        surf.blit(surf2, (0,0))
        self.image = surf
    
    def change(self, x, y, health):
        self.rect.x = x
        self.rect.y = y
        self.health = health

class Charge_Bar(pygame.sprite.DirtySprite):
    
    def __init__(self, position, max_charge, all_sprites_group):
        pygame.sprite.DirtySprite.__init__(self)
        all_sprites_group.add(self)
        self.image = pygame.Surface([30, 5])
        self.image.fill(pygame.Color(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.charge = 0
        self.max_charge = max_charge
        
        self.dirty = 1
        
    def update(self):
        self.dirty = 1
        surf = pygame.Surface([self.max_charge, 20])
        surf.fill(pygame.Color(0, 0, 0))
        surf2 = pygame.Surface([self.charge, 20])
        surf2.fill(pygame.Color(0,200,50))
        surf.blit(surf2, (0,0))
        self.image = surf
    
    def change(self,charge):
        
        self.charge = charge

class Reload_Bar(pygame.sprite.DirtySprite):
    
    def __init__(self, position, max_reload, all_sprites_group):
        pygame.sprite.DirtySprite.__init__(self)
        all_sprites_group.add(self)
        self.image = pygame.Surface([30, 10])
        self.image.fill(pygame.Color(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.reload = 0
        self.max_reload = max_reload
        
        self.dirty = 1
        
    def update(self):
        self.dirty = 1
        surf = pygame.Surface([self.max_reload, 20])
        surf.fill(pygame.Color(0,0,0))
        surf2 = pygame.Surface([self.reload, 20])
        surf2.fill(pygame.Color(0,200,50))
        surf.blit(surf2, (0,0))
        self.image = surf
    
    def change(self, reload):
        self.reload = reload
        