import pygame
import math
from explosion import Explosion, Explosion_Snowbomb
from random import randint
import os
from damage_text import Damage_Text

class Snowball(pygame.sprite.DirtySprite):
    """
    Snowball of different types (regular or snowbomb)
    """
    collide_groups = None
    
    def __init__(self, start_pos, target_pos, type):
        pygame.sprite.DirtySprite.__init__(self)
        self.snowball_hit_sound = pygame.mixer.Sound('sounds/snowball_hit.ogg')
        if type == 1:
            __image_path = os.path.join(os.path.dirname(__file__),'images/weapons/snowball.png')
            self.type = 1
        elif type == 2:
            self.type = 2
            __image_path = os.path.join(os.path.dirname(__file__),'images/weapons/snowbomb.png')
        self.image = pygame.image.load(__image_path).convert_alpha()
        self.rect = self.image.get_rect()
        
        self.rect.x, self.rect.y = start_pos
        self.x, self.y = start_pos
        self.targetx, self.targety = target_pos
        
        self.vel = 10.0
        if type == 1:
            self.damage = 3
        elif type == 2:
            self.damage = 10
        self.crit_multiplier = 3
        self.crit_chance = 10
        
        self.dx = float(self.rect.x - self.targetx)
        self.dy = float(self.rect.y - self.targety)
        distance_c = float(math.sqrt(pow(self.dx, 2.0) + pow(self.dy, 2.0)))
                
        self.vx = self.dx / distance_c * self.vel
        self.vy = self.dy / distance_c * self.vel
        
        self.dirty = 1
       
    def update(self):
        self.dirty = 1
        self.x -= self.vx
        self.y -= self.vy
        self.rect.x = math.ceil(self.x)
        self.rect.y = math.ceil(self.y)
        self.collide_with_enemies()
        self.collide_with_bounds()
        self.collide_with_trees()
        self.collide_with_icewalls()
        self.collide_with_igloowalls()
    
    def collide_with_enemies(self):
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['enemies'], False)
        for enemy in obstacle_hit_list:
            self.snowball_hit_sound.play()
            crit_chance = randint(0, self.crit_chance)
            did_crit = False
            if crit_chance == 0:
                self.damage *= self.crit_multiplier
                did_crit = True
            
            
            damage_text = Damage_Text((self.rect.x, self.rect.y), self.damage, did_crit, self.collide_groups['all'])
            
            if self.type == 1:
                enemy.snowball_hit(self.damage)
                explosion = Explosion(self.rect.x, self.rect.y, self.damage, True, did_crit)
            elif self.type == 2:
                explosion = Explosion_Snowbomb(self.rect.x, self.rect.y, self.damage, True, did_crit, False)
            explosion.collide_groups = self.collide_groups
            explosion.collide_groups = self.collide_groups
            self.collide_groups['all'].add(explosion)
            self.collide_groups['explosions'].add(explosion)
            self.collide_groups['snowballs'].remove(self)
            self.collide_groups['all'].remove(self)
           
    def collide_with_trees(self):
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['trees'], False)
        for tree in obstacle_hit_list:
            self.snowball_hit_sound.play()
            did_crit = False
            if self.type == 1:
                explosion = Explosion(self.rect.x, self.rect.y, self.damage, True, did_crit)
            elif self.type == 2:
                explosion = Explosion_Snowbomb(self.rect.x, self.rect.y, self.damage, True, did_crit, False)
            explosion.collide_groups = self.collide_groups
            self.collide_groups['all'].add(explosion)
            self.collide_groups['explosions'].add(explosion)
            self.collide_groups['snowballs'].remove(self)
            self.collide_groups['all'].remove(self)
   
    def collide_with_icewalls(self):
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['icewalls'], False)
        for obstacle in obstacle_hit_list:
            self.snowball_hit_sound.play()
            did_crit = False
            if self.type == 1:
                explosion = Explosion(self.rect.x, self.rect.y, self.damage, True, did_crit)
            elif self.type == 2:
                explosion = Explosion_Snowbomb(self.rect.x, self.rect.y, self.damage, True, did_crit, False)
            explosion.collide_groups = self.collide_groups
            self.collide_groups['all'].add(explosion)
            self.collide_groups['explosions'].add(explosion)
            self.collide_groups['snowballs'].remove(self)
            self.collide_groups['all'].remove(self)
    
    def collide_with_igloowalls(self):
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['igloowalls'], False)
        for obstacle in obstacle_hit_list:
            self.snowball_hit_sound.play()
            did_crit = False
            if self.type == 1:
                explosion = Explosion(self.rect.x, self.rect.y, self.damage, True, did_crit)
            elif self.type == 2:
                explosion = Explosion_Snowbomb(self.rect.x, self.rect.y, self.damage, True, did_crit, False)
            explosion.collide_groups = self.collide_groups
            self.collide_groups['all'].add(explosion)
            self.collide_groups['explosions'].add(explosion)
            self.collide_groups['snowballs'].remove(self)
            self.collide_groups['all'].remove(self)
    
    def collide_with_bounds(self):
        screen_height = 750
        screen_width = 1200
        if self.rect.y + self.rect.height < 0:
            self.collide_groups['snowballs'].remove(self)
            self.collide_groups['all'].remove(self)
        if self.rect.y > screen_height:
            self.collide_groups['snowballs'].remove(self)
            self.collide_groups['all'].remove(self)
        
        if self.rect.x > screen_width:
            self.collide_groups['snowballs'].remove(self)
            self.collide_groups['all'].remove(self)
            
        if self.rect.x + self.rect.width < 0:
            self.collide_groups['snowballs'].remove(self)
            self.collide_groups['all'].remove(self)
            
                
    def change_vel(self, vel):
        self.vel += vel / 2
        distance_c = float(math.sqrt(pow(self.dx, 2.0) + pow(self.dy, 2.0)))
        self.vx = self.dx / distance_c * self.vel
        self.vy = self.dy / distance_c * self.vel
    
############################################################-    

class Enemy_Snowball(pygame.sprite.DirtySprite):
    """Snowball the a enemy penguin throws"""
    collide_groups = None
    
    def __init__(self, start_pos, target_pos, type):
        pygame.sprite.DirtySprite.__init__(self)
        self.snowball_hit_sound = pygame.mixer.Sound('snowball_hit.ogg')
        if type == 1:
            __image_path = os.path.join(os.path.dirname(__file__),'images/weapons/snowball.png')
            self.type = 1
        elif type == 2:
            self.type = 2
            __image_path = os.path.join(os.path.dirname(__file__),'images/weapons/snowbomb.png')
        self.image = pygame.image.load(__image_path).convert_alpha()
        self.rect = self.image.get_rect()
        
        self.rect.x, self.rect.y = start_pos
        self.x, self.y = start_pos
        self.targetx, self.targety = target_pos
        
        self.vel = 10.0
        if type == 1:
            self.damage = 1
        elif type == 2:
            self.damage = 10
        self.crit_multiplier = 3
        self.crit_chance = 10
        
        self.dx = float(self.rect.x - self.targetx)
        self.dy = float(self.rect.y - self.targety)
        distance_c = float(math.sqrt(pow(self.dx, 2.0) + pow(self.dy, 2.0)))
                
        self.vx = self.dx / distance_c * self.vel
        self.vy = self.dy / distance_c * self.vel
        
        self.dirty = 1
       
    def update(self):
        self.dirty = 1
        self.x -= self.vx
        self.y -= self.vy
        self.rect.x = math.ceil(self.x)
        self.rect.y = math.ceil(self.y)
        self.collide_with_enemies()
        self.collide_with_bounds()
        self.collide_with_trees()
        self.collide_with_icewalls()
        self.collide_with_igloowalls()
    
    def collide_with_enemies(self):
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['penguins'], False)
        for enemy in obstacle_hit_list:
            self.snowball_hit_sound.play()
            crit_chance = randint(0, self.crit_chance)
            did_crit = False
            if crit_chance == 0:
                self.damage *= self.crit_multiplier
                did_crit = True
        
            if self.type == 1:
                enemy.snowball_hit(self.damage)
                explosion = Explosion(self.rect.x, self.rect.y, self.damage, True, did_crit)
            elif self.type == 2:
                explosion = Explosion_Snowbomb(self.rect.x, self.rect.y, self.damage, True, did_crit, True)
            explosion.collide_groups = self.collide_groups
            explosion.collide_groups = self.collide_groups
            self.collide_groups['all'].add(explosion)
            self.collide_groups['explosions'].add(explosion)
            self.collide_groups['snowballs'].remove(self)
            self.collide_groups['all'].remove(self)
           
    def collide_with_trees(self):
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['trees'], False)
        for tree in obstacle_hit_list:
            #self.snowball_hit_sound.play()
            did_crit = False
            if self.type == 1:
                explosion = Explosion(self.rect.x, self.rect.y, self.damage, True, did_crit)
            elif self.type == 2:
                explosion = Explosion_Snowbomb(self.rect.x, self.rect.y, self.damage, True, did_crit, True)
            explosion.collide_groups = self.collide_groups
            self.collide_groups['all'].add(explosion)
            self.collide_groups['explosions'].add(explosion)
            self.collide_groups['snowballs'].remove(self)
            self.collide_groups['all'].remove(self)
            
    def collide_with_icewalls(self):
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['icewalls'], False)
        
        for obstacle in obstacle_hit_list:
            #self.snowball_hit_sound.play()
            did_crit = False
            if self.type == 1:
                explosion = Explosion(self.rect.x, self.rect.y, self.damage, True, did_crit)
            elif self.type == 2:
                explosion = Explosion_Snowbomb(self.rect.x, self.rect.y, self.damage, True, did_crit, True)
            explosion.collide_groups = self.collide_groups
            self.collide_groups['all'].add(explosion)
            self.collide_groups['explosions'].add(explosion)
            self.collide_groups['snowballs'].remove(self)
            self.collide_groups['all'].remove(self)
    
    def collide_with_igloowalls(self):
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['igloowalls'], False)
        for obstacle in obstacle_hit_list:
            #self.snowball_hit_sound.play()
            did_crit = False
            if self.type == 1:
                explosion = Explosion(self.rect.x, self.rect.y, self.damage, True, did_crit)
            elif self.type == 2:
                explosion = Explosion_Snowbomb(self.rect.x, self.rect.y, self.damage, True, did_crit, True)
                explosion.collide_groups = self.collide_groups
            explosion.collide_groups = self.collide_groups
            self.collide_groups['all'].add(explosion)
            self.collide_groups['explosions'].add(explosion)
            self.collide_groups['snowballs'].remove(self)
            self.collide_groups['all'].remove(self)
    
    def collide_with_bounds(self):
        screen_height = 750
        screen_width = 1200
        if self.rect.y + self.rect.height < 0:
            self.collide_groups['snowballs'].remove(self)
            self.collide_groups['all'].remove(self)
        if self.rect.y > screen_height:
            self.collide_groups['snowballs'].remove(self)
            self.collide_groups['all'].remove(self)
        
        if self.rect.x > screen_width:
            self.collide_groups['snowballs'].remove(self)
            self.collide_groups['all'].remove(self)
            
        if self.rect.x + self.rect.width < 0:
            self.collide_groups['snowballs'].remove(self)
            self.collide_groups['all'].remove(self)
            
                
    def change_vel(self, vel):
        self.vel = vel / 2.0
        distance_c = float(math.sqrt(pow(self.dx, 2.0) + pow(self.dy, 2.0)))
        self.vx = self.dx / distance_c * self.vel
        self.vy = self.dy / distance_c * self.vel
    