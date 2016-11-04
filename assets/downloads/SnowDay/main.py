import pygame
import sys
import math
from random import randint
from enemy import Enemy
from snowball import Snowball
from penguin import Penguin
from explosion import Explosion
from map import Map
from pygame.locals import *
from damage_text import Win, Target
import os

def main():
    """
    The objective of the game is to eliminate all enemy penguins.
    You are the black penguin, the enemy penguins are blue.
    
    You move with: WASD
    
    You can throw regular snowballs or snowbombs. Snowbombs do more damage 
    then regular snowballs.
    
    You can swtich between the 2 types of snowballs by pressing:
    1 - regular snowballs
    2 - snowbombs
    
    While throwing regular snowballs, you can throw harder by holding down the
    left mouse click. You throw snowballs by releasing a click.
    
    It takes time to reload every snowbomb.
    
    """
    pygame.init()
    FPS = 32
    fpsClock = pygame.time.Clock()
    frame_width = 1200
    frame_height = 750
    windowSize = (frame_width, frame_height)
    SCREEN = pygame.display.set_mode(windowSize)
    
    pygame.display.set_caption("Snow Day")
    
    WHITE = pygame.Color(255, 255, 255)
    BLACK = pygame.Color(0, 0, 0)
    ORANGE = pygame.Color(236, 133, 86)
    BLUE = pygame.Color(0, 200, 255)
    
    
    #ICEBURG = pygame.image.load("images/environment/iceburgBG.jpg").convert()
    __image_path = os.path.join(os.path.dirname(__file__),'images/environment/iceburgBG.jpg')
    ICEBURG = pygame.image.load(__image_path).convert_alpha()
    #screen.blit(bridge, (510, 570))
    #SCREEN.blit(ICEBURG, (0, 0))
    
    
    # sprite groups
    explosions = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    snowballs = pygame.sprite.Group()
    penguins = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.LayeredDirty()
    generate_enemies(enemies, all_sprites_list, SCREEN)
    #MAP
    MAP = Map(SCREEN, frame_width, frame_height, all_sprites_list)
    
    #PENGUIN
    penguin = Penguin(210, 150, all_sprites_list)
    penguins.add(penguin)
    collide_groups_dict = {'all': all_sprites_list,
        'penguins': penguins,  
        'penguin': penguin,              
        'snowballs': snowballs,
        'trees': MAP.tree_stump_group,
        'invisible_walls': MAP.invisible_wall_group,
        'icecubes': MAP.icecube_group,
        'icewalls': MAP.icewall_group,
        'igloowalls': MAP.igloowall_group,
        'enemies': enemies,
        'explosions': explosions}
    
    for enemy in enemies:
        enemy.collide_groups = collide_groups_dict
    
    
    penguin.draw(SCREEN)
    all_sprites_list.add(penguin)
    penguin.collide_groups = collide_groups_dict
    MAP.collide_groups = collide_groups_dict
    
    snowball_damage = 1
    move_left = False
    move_right = False
    move_down = False
    move_up = False
    
    #sounds
    throw_sound = pygame.mixer.Sound('sounds/throw.ogg')
    pygame.mixer.music.load('sounds/bgmusic.ogg')
    pygame.mixer.music.set_endevent(USEREVENT)
    pygame.mixer.music.play()
    
    #MOUSE
    target = Target((0,0))
    all_sprites_list.add(target)
    
    pygame.display.update()
    
    pygame.mouse.set_visible(0)
    
    while True:
        
        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            target_pos = pygame.mouse.get_pos()
            penguin.charge_snowball(1)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    penguin.change_snowball_type(1)
                if event.key == K_2:
                    penguin.change_snowball_type(2)
                if event.key == K_w:
                    move_up = True
                if event.key == K_s:
                    move_down = True
                if event.key == K_a:
                    move_left = True
                if event.key == K_d:
                    move_right = True
            if event.type == KEYUP:
                if event.key == K_w:
                    move_up = False
                if event.key == K_s:
                    move_down = False
                if event.key == K_a:
                    move_left = False
                if event.key == K_d:
                    move_right = False
                    
            if event.type == MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                
                if buttons[0]:
                    target_pos = pygame.mouse.get_pos()
            
                    
            if event.type == MOUSEBUTTONUP:
                throw_sound.play()
                penguin.throw_snowball(target_pos, penguin.charge)
                
                buttons = pygame.mouse.get_pressed()
                if buttons[0]:
                    target_pos = pygame.mouse.get_pos()
                    penguin.throw_snowball(target_pos, penguin.charge)  
                penguin.charge_snowball(0.0)   
                    
            if event.type == MOUSEMOTION:
                position = pygame.mouse.get_pos()
                target.change_pos(position)
                
                
            if event.type == USEREVENT:
                pygame.mixer.music.play()

        penguin.move(move_up, move_down, move_left, move_right)
        
        #PENGUIN
        penguin.update_reload()
           
        #group draw
        all_sprites_list.clear(SCREEN, ICEBURG)
        all_sprites_list.update()
        update_sprites = all_sprites_list.draw(SCREEN)
        MAP.draw_foreground(SCREEN) 
        
        pygame.display.update(update_sprites)
        
        #ENEMIES
        enemy_count = 0
        for enemy in enemies:
            enemy_count += 1
        if enemy_count == 0:
            win = Win((500, 500))

        fpsClock.tick(FPS)

def generate_enemies(enemy_group, all_sprites_list, SCREEN):
    for i in range(0,6):
        x = randint(900, 1000)
        y = randint(200, 400)
        enemy = Enemy(x, y, all_sprites_list)
        enemy_group.add(enemy)
        all_sprites_list.add(enemy)
    
 
main()
