import pygame

class Explosion(pygame.sprite.DirtySprite):
    """Snowball explosion"""
    collide_groups = None

    PURPLE = pygame.Color(170, 0, 150)
    ORANGE = pygame.Color(236, 133, 86)
    
    def __init__(self, x, y, damage, show_damage, did_crit):
        pygame.sprite.DirtySprite.__init__(self)
        self.sheet = pygame.image.load('images/effects/snowball_hit.png')
        self.width = 40
        self.height = 40
        self.numImages = 6
        self.curImage = 0
        self.images = []
        for i in range(0, self.numImages):
            self.sheet.set_clip(pygame.Rect(i % 6 * self.width, i / 6 * self.height, self.width, self.height))
            clip = self.sheet.subsurface(self.sheet.get_clip())
            self.images.append(clip)
            #self.images.append(pygame.transform.chop(self.image, (i % 6 * self.width, i / 6 * self.height, self.width, self.height)))
        self.sheet.set_clip(pygame.Rect(0, 0, self.width, self.height))
        clip = self.sheet.subsurface(self.sheet.get_clip())
        self.image = clip
        self.rect = self.image.get_rect()
        
        self.rect.x = x - self.width / 2
        self.rect.y = y - self.height / 2
        
        #self.text_y = self.y
        self.explosion_damage = damage
        self.did_crit = did_crit
        self.show_damage = show_damage
        self.dirty = 1
        
    
    def update(self):
        self.dirty = 1
        if self.curImage >= self.numImages - 1:
            self.collide_groups['explosions'].remove(self)
            self.collide_groups['all'].remove(self)
        else:
            self.curImage += 1
            self.image = self.images[self.curImage]
            
    
    def draw(self, screen):
        PURPLE = pygame.Color(170, 0, 150)
        ORANGE = pygame.Color(230, 170, 50)
        
        self.curImage % 6
        
        if self.did_crit:
            font = pygame.font.SysFont('ariel', 30, False, False)
            text_to_draw1 = font.render(str(self.explosion_damage), True, ORANGE)
        else:
            font = pygame.font.SysFont('ariel', 20, False, False)
            text_to_draw1 = font.render(str(self.explosion_damage), True, PURPLE)
            self.text_y -= 2
        if self.show_damage:
            screen.blit(text_to_draw1, (self.x, self.text_y))
        screen.blit(self.images, (self.x, self.y), (self.curImage % 6 * self.width, self.curImage / 6 * self.height, self.width, self.height))
            
            
            
            
            
class Explosion_Snowbomb(pygame.sprite.DirtySprite):
    """Snowbomb explosion"""
    collide_groups = None

    PURPLE = pygame.Color(170, 0, 150)
    ORANGE = pygame.Color(236, 133, 86)
    
    def __init__(self, x, y, damage, show_damage, did_crit, enemy_did_throw):
        pygame.sprite.DirtySprite.__init__(self)
        pygame.mixer.Sound('sounds/blast.ogg').play()
        self.sheet = pygame.image.load('images/effects/ice_hit.png')
        self.width = 200
        self.height = 200
        self.numImages = 10
        self.curImage = 0
        self.images = []
        for i in range(0, self.numImages):
            self.sheet.set_clip(pygame.Rect(i % 5 * self.width, i / 5 * self.height, self.width, self.height))
            clip = self.sheet.subsurface(self.sheet.get_clip())
            self.images.append(clip)
            #self.images.append(pygame.transform.chop(self.image, (i % 6 * self.width, i / 6 * self.height, self.width, self.height)))
        self.sheet.set_clip(pygame.Rect(0, 0, self.width, self.height))
        clip = self.sheet.subsurface(self.sheet.get_clip())
        self.image = clip
        self.rect = self.image.get_rect()
        
        self.rect.x = x - self.width / 2
        self.rect.y = y - self.height / 2
        
        #self.text_y = self.y
        self.damage = damage
        self.damage_per_frame = self.damage / self.numImages
        self.did_crit = did_crit
        self.show_damage = show_damage
        
        self.enemy_did_throw = enemy_did_throw
        
        self.dirty = 1
  
    def update(self):
        self.dirty = 1
        
        if self.enemy_did_throw:
            obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['penguins'], False)
        else:
            obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['enemies'], False)
        for obstacle in obstacle_hit_list:
            obstacle.snowball_hit(self.damage_per_frame)
        if self.curImage >= self.numImages - 1:
            self.collide_groups['explosions'].remove(self)
            self.collide_groups['all'].remove(self)
        else:
            self.curImage += 1
            self.image = self.images[self.curImage]
            
    
    def draw(self, screen):
        PURPLE = pygame.Color(170, 0, 150)
        ORANGE = pygame.Color(230, 170, 50)
        
        self.curImage % 6
        
        if self.did_crit:
            font = pygame.font.SysFont('ariel', 30, False, False)
            text_to_draw1 = font.render(str(self.explosion_damage), True, ORANGE)
        else:
            font = pygame.font.SysFont('ariel', 20, False, False)
            text_to_draw1 = font.render(str(self.explosion_damage), True, PURPLE)
            self.text_y -= 2
        if self.show_damage:
            screen.blit(text_to_draw1, (self.x, self.text_y))
        screen.blit(self.images, (self.x, self.y), (self.curImage % 6 * self.width, self.curImage / 6 * self.height, self.width, self.height))
           
            
            
            

class Explosion_Enemy(pygame.sprite.DirtySprite):

    
    collide_groups = None

    PURPLE = pygame.Color(170, 0, 150)
    ORANGE = pygame.Color(236, 133, 86)
    
    def __init__(self, x, y):
        pygame.sprite.DirtySprite.__init__(self)
        pygame.mixer.Sound('sounds/blast.ogg').play()
        self.sheet = pygame.image.load('images/effects/ice_hit.png')
        self.width = 200
        self.height = 200
        self.numImages = 10
        self.curImage = 0
        self.images = []
        for i in range(0, self.numImages):
            self.sheet.set_clip(pygame.Rect(i % 5 * self.width, i / 5 * self.height, self.width, self.height))
            clip = self.sheet.subsurface(self.sheet.get_clip())
            self.images.append(clip)
        self.sheet.set_clip(pygame.Rect(0, 0, self.width, self.height))
        clip = self.sheet.subsurface(self.sheet.get_clip())
        self.image = clip
        self.rect = self.image.get_rect()
        
        self.rect.x = x - self.width / 2
        self.rect.y = y - self.height / 2
        
        self.dirty = 1
        
    
    def update(self):
        self.dirty = 1
        if self.curImage >= self.numImages - 1:
            self.collide_groups['explosions'].remove(self)
            self.collide_groups['all'].remove(self)
        else:
            self.curImage += 1
            self.image = self.images[self.curImage]
            
    
    def draw(self, screen):
        PURPLE = pygame.Color(170, 0, 150)
        ORANGE = pygame.Color(230, 170, 50)
        
        self.curImage % 6
        
        if self.did_crit:
            font = pygame.font.SysFont('ariel', 30, False, False)
            text_to_draw1 = font.render(str(self.explosion_damage), True, ORANGE)
        else:
            font = pygame.font.SysFont('ariel', 20, False, False)
            text_to_draw1 = font.render(str(self.explosion_damage), True, PURPLE)
            self.text_y -= 2
        if self.show_damage:
            screen.blit(text_to_draw1, (self.x, self.text_y))
        screen.blit(self.images, (self.x, self.y), (self.curImage % 6 * self.width, self.curImage / 6 * self.height, self.width, self.height))
           
            