import pygame
from random import randint
import math
from explosion import Explosion_Enemy
from bar import Health_Bar
from snowball import Enemy_Snowball

class Enemy(pygame.sprite.DirtySprite):
    """ The Enemy Penguins that throw snowballs at you"""
    
    collide_groups = None
    
    def __init__(self, x, y, all_sprites_group):
        pygame.sprite.DirtySprite.__init__(self)
        self.throw_sound = pygame.mixer.Sound('sounds/throw2.ogg')
        self.image = pygame.image.load("images/penguin/blue_penguin_S.png").convert_alpha() 
        self.dir = 0
        self.health = 30
        self.max_health = 30
        self.vel = 4
        self.angle_vel = self.vel * (math.sqrt(2) / 2)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.health_bar = Health_Bar((x, y), self.max_health, all_sprites_group)
        
        self.dirty = 1
        
    def snowball_hit(self, damage):
        self.health -= damage
        
    def update(self):
        self.dirty = 1
    
        if self.health <= 0:
            self.collide_groups['enemies'].remove(self)
            self.collide_groups['all'].remove(self)
            self.collide_groups['all'].remove(self.health_bar)
            explosion = Explosion_Enemy(self.rect.x, self.rect.y)
            explosion.collide_groups = self.collide_groups
            self.collide_groups['explosions'].add(explosion)
            self.collide_groups['all'].add(explosion)
        
        self.health_bar.change(self.rect.x, self.rect.y - 7, self.health)
        health_bar_x = self.rect.x
        health_bar_y = self.rect.y - self.rect.height / 2 - 3

        up = False
        down = False
        left = False
        right = False
        randNum = randint(0,8)
        if randNum == 0:
            self.dir = randint(0,8)
        if self.dir == 0:
            up = False
            down = False
            left = False
            right = False
        elif self.dir == 1:
            up = True
            down = False
            left = True
            right = False
        elif self.dir == 2:
            up = True
            down = False
            left = False
            right = False
        elif self.dir == 3:
            up = True
            down = False
            left = False
            right = True
        elif self.dir == 4:
            up = False
            down = False
            left = True
            right = False
        elif self.dir == 5:
            up = False
            down = False
            left = False
            right = True
        elif self.dir == 6:
            up = False
            down = True
            left = True
            right = False
        elif self.dir == 7:
            up = False
            down = True
            left = False
            right = True
        elif self.dir == 8:
            up = False
            down = True
            left = False
            right = True
        self.move(up, down, left, right)
        
        randThrow = randint(0,50)
        if randThrow == 0:
            self.throw_snowball(20.0)
    
    def move(self, up, down, left, right):
        self.dirty = 1
        if up and right:
            self.image = pygame.image.load("images/penguin/blue_penguin_NE.png").convert_alpha()
            self.x += self.angle_vel
            self.y -= self.angle_vel   
        elif down and right:
            self.image = pygame.image.load("images/penguin/blue_penguin_SE.png").convert_alpha()
            self.x += self.angle_vel
            self.y += self.angle_vel
        elif down and left:
            self.image = pygame.image.load("images/penguin/blue_penguin_SW.png").convert_alpha()
            self.x -= self.angle_vel
            self.y += self.angle_vel
        elif up and left:
            self.image = pygame.image.load("images/penguin/blue_penguin_NW.png").convert_alpha()
            self.x -= self.angle_vel
            self.y -= self.angle_vel
        elif up:
            self.image = pygame.image.load("images/penguin/blue_penguin_N.png").convert_alpha()
            self.y -= self.vel
        elif down:
            self.image = pygame.image.load("images/penguin/blue_penguin_S.png").convert_alpha()
            self.y += self.vel
        elif left:
            self.image = pygame.image.load("images/penguin/blue_penguin_W.png").convert_alpha()
            self.x -= self.vel  
        elif right:
            self.image = pygame.image.load("images/penguin/blue_penguin_E.png").convert_alpha()
            self.x += self.vel
        self.collide_with_objects(up, down, left, right)
        self.collide_with_bounds()
        
        
    def collide_with_objects(self, up, down, left, right):
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
    
    def throw_snowball(self, snowball_vel):
        self.throw_sound.play()
        x = self.collide_groups['penguin'].get_cord_x() + randint(-20,20)
        y = self.collide_groups['penguin'].get_cord_y() + randint(-20,20)
        pos = (x, y)
        
        randThrow = randint(0,8)
        if randThrow == 0:
            snowball_type = 2
        else:
            snowball_type = 1
        
        if snowball_type == 1:
            snowball = Enemy_Snowball((self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2), pos, 1)
            snowball.collide_groups = self.collide_groups
            snowball.change_vel(snowball_vel)
            self.collide_groups['snowballs'].add(snowball)
            self.collide_groups['all'].add(snowball)
        else:
            snowball = Enemy_Snowball((self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2), pos, 2)
            snowball.collide_groups = self.collide_groups
            snowball.change_vel(snowball_vel)
            self.collide_groups['snowballs'].add(snowball)
            self.collide_groups['all'].add(snowball)

