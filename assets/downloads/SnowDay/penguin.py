import pygame
import math
from snowball import Snowball
from bar import Charge_Bar, Health_Bar, Reload_Bar
from explosion import Explosion_Snowbomb
from damage_text import Game_Over

class Penguin(pygame.sprite.DirtySprite):
    """Main character the user plays"""
    collide_groups = None
    
    def __init__(self, x, y, all_sprites_group):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.image.load("images/penguin/penguin_S.png").convert_alpha() 
        self.snowball_type = 1
        self.reload_time = 100
        self.reload_max_time = 100
        self.vel = 4
        self.angle_vel = self.vel * (math.sqrt(2) / 2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = float(x)
        self.y = float(y)
        
        self.health = 30
        self.max_health = 30
        
        self.charge = 0.0
        self.max_charge = 100
        self.charge_bar = Charge_Bar((50, 665), self.max_charge, all_sprites_group)
        self.reload_bar = Reload_Bar((50, 695), self.reload_max_time, all_sprites_group)
        self.health_bar = Health_Bar((x, y), self.max_health, all_sprites_group)
        
        self.dirty = 1
        
    def update(self):
        #self.dirty = 1
        
        if self.health <= 0:
            self.collide_groups['penguins'].remove(self)
            self.collide_groups['all'].remove(self)
            self.collide_groups['all'].remove(self.health_bar)
            explosion = Explosion_Snowbomb(self.rect.x, self.rect.y, 10, False, False, False)
            explosion.collide_groups = self.collide_groups
            self.collide_groups['explosions'].add(explosion)
            self.collide_groups['all'].add(explosion)
            game_over = Game_Over((self.rect.x, self.rect.y), self.collide_groups['all'])
        
        self.health_bar.change(self.rect.x, self.rect.y - 7, self.health)
        self.reload_bar.change(self.reload_time)
        health_bar_x = self.rect.x
        health_bar_y = self.rect.y - self.rect.height / 2 - 3
        
    def move(self, up, down, left, right):
        #self.dirty = 1
        
        if up and right:
            self.image = pygame.image.load("images/penguin/penguin_NE.png").convert_alpha()
            self.x += self.angle_vel
            self.y -= self.angle_vel   
        elif down and right:
            self.image = pygame.image.load("images/penguin/penguin_SE.png").convert_alpha()
            self.x += self.angle_vel
            self.y += self.angle_vel
        elif down and left:
            self.image = pygame.image.load("images/penguin/penguin_SW.png").convert_alpha()
            self.x -= self.angle_vel
            self.y += self.angle_vel
        elif up and left:
            self.image = pygame.image.load("images/penguin/penguin_NW.png").convert_alpha()
            self.x -= self.angle_vel
            self.y -= self.angle_vel
        elif up:
            self.image = pygame.image.load("images/penguin/penguin_N.png").convert_alpha()
            self.y -= self.vel
        elif down:
            self.image = pygame.image.load("images/penguin/penguin_S.png").convert_alpha()
            self.y += self.vel
        elif left:
            self.image = pygame.image.load("images/penguin/penguin_W.png").convert_alpha()
            self.x -= self.vel  
        elif right:
            self.image = pygame.image.load("images/penguin/penguin_E.png").convert_alpha()
            self.x += self.vel
        self.collide_with_objects(up, down, left, right)
        self.collide_with_bounds()
        
    
    def collide_with_objects(self, up, down, left, right):
        """detects all collisions with the map"""
        self.rect.x = math.ceil(self.x)
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['trees'], False)
        for obstacle in obstacle_hit_list:
            if right:
                self.rect.right = obstacle.rect.left
                self.x = obstacle.rect.left - self.rect.width
            if left:
                self.rect.left = obstacle.rect.right
                self.x = obstacle.rect.right
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['invisible_walls'], False)
        for obstacle in obstacle_hit_list:
            if right:
                self.rect.right = obstacle.rect.left
                self.x = obstacle.rect.left - self.rect.width
            if left:
                self.rect.left = obstacle.rect.right
                self.x = obstacle.rect.right
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['icecubes'], False)
        for obstacle in obstacle_hit_list:
            if right:
                self.rect.right = obstacle.rect.left
                self.x = obstacle.rect.left - self.rect.width
            if left:
                self.rect.left = obstacle.rect.right
                self.x = obstacle.rect.right
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['igloowalls'], False)
        for obstacle in obstacle_hit_list:
            if right:
                self.rect.right = obstacle.rect.left
                self.x = obstacle.rect.left - self.rect.width
            if left:
                self.rect.left = obstacle.rect.right
                self.x = obstacle.rect.right
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['icewalls'], False)
        for obstacle in obstacle_hit_list:
            if right:
                self.rect.right = obstacle.rect.left
                self.x = obstacle.rect.left - self.rect.width
            if left:
                self.rect.left = obstacle.rect.right
                self.x = obstacle.rect.right
        self.rect.y = math.ceil(self.y)
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['trees'], False)
        for obstacle in obstacle_hit_list:       
            if down:
                self.rect.bottom = obstacle.rect.top
                self.y = obstacle.rect.top - self.rect.height
            if up:
                self.rect.top = obstacle.rect.bottom
                self.y = obstacle.rect.bottom
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['invisible_walls'], False)
        for obstacle in obstacle_hit_list:       
            if down:
                self.rect.bottom = obstacle.rect.top
                self.y = obstacle.rect.top - self.rect.height
            if up:
                self.rect.top = obstacle.rect.bottom
                self.y = obstacle.rect.bottom
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['icecubes'], False)
        for obstacle in obstacle_hit_list:       
            if down:
                self.rect.bottom = obstacle.rect.top
                self.y = obstacle.rect.top - self.rect.height
            if up:
                self.rect.top = obstacle.rect.bottom
                self.y = obstacle.rect.bottom
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['igloowalls'], False)
        for obstacle in obstacle_hit_list:       
            if down:
                self.rect.bottom = obstacle.rect.top
                self.y = obstacle.rect.top - self.rect.height
            if up:
                self.rect.top = obstacle.rect.bottom
                self.y = obstacle.rect.bottom
        obstacle_hit_list = pygame.sprite.spritecollide(self, self.collide_groups['icewalls'], False)
        for obstacle in obstacle_hit_list:       
            if down:
                self.rect.bottom = obstacle.rect.top
                self.y = obstacle.rect.top - self.rect.height
            if up:
                self.rect.top = obstacle.rect.bottom
                self.y = obstacle.rect.bottom 
        
    
    def collide_with_bounds(self):
        """Detects collision with the screen"""
        screen_height = 750
        screen_width = 1200
        if self.rect.y < 0:
            self.y = 0
            self.rect.top = 0
        if self.rect.y + self.rect.height > screen_height:
            self.y = screen_height - self.rect.height
            self.rect.bottom = screen_height
        if self.rect.x > screen_width - self.rect.width:
            self.x = screen_width - self.rect.width
            self.rect.right = screen_width
        if self.rect.x < 0:
            self.x = 0
            self.rect.left = 0
        
    def throw_snowball(self, mouse_pos, snowball_vel):
        """Throws either a snowball or snowbomb"""
        if self.snowball_type == 1:
            snowball = Snowball((self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2), mouse_pos, self.snowball_type)
            snowball.collide_groups = self.collide_groups
            snowball.change_vel(snowball_vel)
            self.collide_groups['snowballs'].add(snowball)
            self.collide_groups['all'].add(snowball)
        elif self.snowball_type == 2 and self.reload_time >= self.reload_max_time:
            self.reload_time = 0
            snowball = Snowball((self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2), mouse_pos, self.snowball_type)
            snowball.collide_groups = self.collide_groups
            self.collide_groups['snowballs'].add(snowball)
            self.collide_groups['all'].add(snowball)
    
    def change_snowball_type(self, type):
        """changes type of snowball
        1- snowball
        2- snowbomb
        """
        self.snowball_type = type
        if type == 2:
            self.reload_max_time = 100
    
    def update_reload(self):
        """Reloading snowbomb..."""
        if self.reload_time < self.reload_max_time:
            self.reload_time += 1   
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def charge_snowball(self, charge):
        """Charge snowball, the longer the mouse is held, the faster the ball"""
        if charge == 0.0:
            self.charge = 0.0
        else:
            self.charge += charge
        self.charge_bar.change(self.charge)
        
    def snowball_hit(self, damage):
        """Hurts penguin if hit by snowballs"""
        self.health -= damage    
    
    def get_cord_x(self):
        """gets x cord of penguin"""
        return self.rect.x + self.rect.width / 2
        
    def get_cord_y(self):
        """gets y cord of penguin"""
        return self.rect.y + self.rect.height / 2
        
        