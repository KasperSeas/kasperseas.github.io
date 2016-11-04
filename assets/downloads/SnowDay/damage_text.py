import pygame
import math

class Damage_Text(pygame.sprite.DirtySprite):
    """Show how much damage was done"""
    def __init__(self, position, damage, did_crit, all_sprites_group):
        pygame.sprite.DirtySprite.__init__(self)
        
        PURPLE = pygame.Color(170, 0, 150)
        ORANGE = pygame.Color(230, 170, 50)
        
        self.did_crit = did_crit
        
        if did_crit:
            font = pygame.font.SysFont('ariel', 30, False, False)
            text_to_draw1 = font.render(str(damage), True, ORANGE)
        else:
            font = pygame.font.SysFont('ariel', 20, False, False)
            text_to_draw1 = font.render(str(damage), True, PURPLE)
            
        
        self.image = text_to_draw1
        self.rect = self.image.get_rect()
        
        self.all_group = all_sprites_group
        all_sprites_group.add(self)

        self.rect.x = position[0]
        self.rect.y = position[1]

        self.counter = 0

        self.dirty = 1
        
    def update(self):
        self.dirty = 1
        if self.did_crit:
            None
        else: 
            self.rect.y -= 2
        self.counter += 1
        if self.counter == 30:
            self.all_group.remove(self)

class Win(pygame.sprite.DirtySprite):
    
    def __init__(self, position):
        pygame.sprite.DirtySprite.__init__(self)
        
        BLUE = pygame.Color(0, 200, 200)
    
        font = pygame.font.SysFont('ariel', 30, False, False)
        text_to_draw1 = font.render("You Win!", True, BLUE)

        self.image = text_to_draw1
        self.rect = self.image.get_rect()

        self.rect.x = position[0]
        self.rect.y = position[1]

        self.counter = 0

        self.dirty = 1
        
    def update(self):
        self.dirty = 1
        BLUE = pygame.Color(0, 200, 200)
        if self.counter < 70:
            font = pygame.font.SysFont('ariel', 30 + self.counter, False, False)
            text_to_draw1 = font.render("You Win!", True, BLUE)
            self.image = text_to_draw1
        
        self.counter += 1
        
class Game_Over(pygame.sprite.DirtySprite):
    
    def __init__(self, position, all_sprites_group):
        pygame.sprite.DirtySprite.__init__(self)
        
        PURPLE = pygame.Color(170, 0, 150)
        ORANGE = pygame.Color(230, 170, 50)
    
        font = pygame.font.SysFont('ariel', 30, False, False)
        text_to_draw1 = font.render("GAME OVER", True, ORANGE)

        self.image = text_to_draw1
        self.rect = self.image.get_rect()
        
        self.all_group = all_sprites_group
        all_sprites_group.add(self)

        self.rect.x = position[0]
        self.rect.y = position[1]

        self.counter = 0

        self.dirty = 1
        
    def update(self):
        self.dirty = 1
        ORANGE = pygame.Color(230, 170, 50)
        if self.counter < 40:
            font = pygame.font.SysFont('ariel', 30 + self.counter, False, False)
            text_to_draw1 = font.render("GAME OVER", True, ORANGE)
            self.image = text_to_draw1
        
        self.counter += 1
        
        
class Target(pygame.sprite.DirtySprite):
    
    def __init__(self, position):
        pygame.sprite.DirtySprite.__init__(self)
        
        self.image = pygame.image.load("images/interface/target.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

        self.dirty = 1
        
    def update(self):
        self.dirty = 1

    def change_pos(self, position):
        self.rect.x = position[0]
        self.rect.y = position[1]
        
  
  
  