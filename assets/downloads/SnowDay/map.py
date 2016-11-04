import pygame
import math
import os
from rock import Rock, Icecube
from tree import Tree_Stump
from invisible_wall import Invisible_Wall

class Map:
    """
    Creates the map
    """
    collide_groups = None
    
    rock_group = None
    tree_stump_group = None
    invisible_wall_group = None
    icecube_group = None
    icewall_group = None
    igloowall_group = None
    
    def __init__(self, screen, width, height, all_sprites_group):
        """Create groups of obstacles in the 1200x750 environment"""
        colnum = width / 30
        rownum = height / 30
        
        tilemap = [
                   [1,1,1,1,1,0,0,1,1,0,0,0,0,0,4,1,1,1,1,0,0,0,0,0,0,4,0,0,1,1,1,1,1,1,1,0,0,1,1,1],
                   [1,0,0,0,0,0,5,5,5,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,5,5,5,0,0,0,0,0,1],
                   [1,1,0,0,0,5,0,0,0,5,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,5,0,0,0,5,0,0,0,0,1],
                   [1,1,0,0,0,5,0,0,0,5,0,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,5,0,0,0,5,0,0,0,1,1],
                   [1,0,0,0,0,5,0,0,0,5,0,0,0,3,0,0,0,0,0,3,3,3,0,0,0,0,0,3,0,0,5,0,0,0,5,0,0,0,1,1],
                   [0,0,0,0,0,0,0,0,5,5,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,5,5,0,0,0,0,0],
                   [0,2,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,2,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,4,3,3,0,0,0,0,0,0,0,3,0,0,0,0,0,3,0,0,0,0,0,0,0,3,3,4,0,0,0,0,0,1],
                   [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,1],
                   [1,0,0,0,0,0,0,0,0,0,4,0,0,0,2,0,0,0,3,0,0,0,3,0,0,2,0,0,0,0,4,0,0,0,0,0,0,0,0,1],
                   [1,1,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,4,0,0,0,0,0,0,0,0,1,1],
                   [1,1,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,1,1],
                   [1,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,1,1],
                   [0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,3,3,0,0,0,0,1,1],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                   [0,0,0,3,3,2,0,0,0,0,0,0,3,2,0,3,0,0,1,1,1,1,1,0,0,3,2,0,3,0,0,0,0,0,0,2,0,3,0,1],
                   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [1,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0],
                   [1,1,0,0,0,0,4,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0],
                   [1,1,0,0,0,0,3,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,1],
                   [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1],
                   [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1],
                   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                  ]
        
        
        
        self.tree_stump_group = pygame.sprite.Group()
        self.invisible_wall_group = pygame.sprite.Group()
        self.icecube_group = pygame.sprite.Group()
        self.icewall_group = pygame.sprite.Group()
        self.igloowall_group = pygame.sprite.Group()
        self.grid_scale = 30
        
        for row in range(rownum):
            for col in range(colnum):
                if tilemap[row][col] == 1:
                    inv_wall = Invisible_Wall((col * self.grid_scale, row * self.grid_scale), screen)
                    self.invisible_wall_group.add(inv_wall)
                if tilemap[row][col] == 2:
                    tree = Tree_Stump((col * self.grid_scale, row * self.grid_scale), screen)
                    self.tree_stump_group.add(tree)
                if tilemap[row][col] == 3:
                    icecube = Invisible_Wall((col * self.grid_scale, row * self.grid_scale), screen)
                    self.icecube_group.add(icecube)
                    all_sprites_group.add(icecube)
                if tilemap[row][col] == 4:
                    icewall = Invisible_Wall((col * self.grid_scale, row * self.grid_scale), screen)
                    self.icewall_group.add(icewall)
                    all_sprites_group.add(icewall)
                if tilemap[row][col] == 5:
                    igloowall = Invisible_Wall((col * self.grid_scale, row * self.grid_scale), screen)
                    self.igloowall_group.add(igloowall)
                    all_sprites_group.add(igloowall)
                   
        #igloo entrance
        igloowall1 = Invisible_Wall((174, 150), screen)
        self.igloowall_group.add(igloowall1)
        all_sprites_group.add(igloowall1)
        igloowall2 = Invisible_Wall((924, 150), screen)
        self.igloowall_group.add(igloowall2)
        all_sprites_group.add(igloowall2)
            
        
    def draw_grid(self, screen):
        """draws a grid on a 1200x750 display. 1 line per 30 pixels"""
        for x in range(0, 40):
            pygame.draw.line(screen, pygame.Color(0, 0, 0), (x * self.grid_scale, 0), (x * self.grid_scale, 750), 1)
        for y in range(0, 25):
            pygame.draw.line(screen, pygame.Color(0, 0, 0), (0, y * self.grid_scale), (1200, y * self.grid_scale), 1)
    
    def draw_iceburg(self, screen):
        """draws background which is a giant iceburg"""
        #ICEBURG = pygame.image.load("iceburgBG.jpg").convert()
        screen.blit(ICEBURG, (0, 0))   
    
    def draw_foreground(self, screen):
        """draws the items that appear in the foreground"""
        __image_path = os.path.join(os.path.dirname(__file__),'images/interface/dashboard.jpg')
        bridge_edges = pygame.image.load(__image_path).convert_alpha()
        screen.blit(bridge_edges, (30, 660))
        __image_path = os.path.join(os.path.dirname(__file__),'images/environment/bridge_edges.png')
        bridge_edges = pygame.image.load(__image_path).convert_alpha()
        screen.blit(bridge_edges, (510, 550))
        __image_path = os.path.join(os.path.dirname(__file__),'images/environment/igloo.png')
        igloo = pygame.image.load(__image_path).convert_alpha()
        screen.blit(igloo, (150, 0))
        __image_path = os.path.join(os.path.dirname(__file__),'images/environment/igloo2.png')
        igloo = pygame.image.load(__image_path).convert_alpha()
        screen.blit(igloo, (900,0))
        #self.draw_grid(screen)
        self.tree_stump_group.draw(screen)
        self.invisible_wall_group.draw(screen)
        for tree_stump in self.tree_stump_group:
            image = pygame.image.load("images/environment/sd_tree.png").convert_alpha()
            screen.blit(image, (tree_stump.rect.x, tree_stump.rect.y - 30))
        for icecube in self.icecube_group:
            icecube.image = pygame.image.load("images/environment/icecube.png").convert_alpha()
        for icewall in self.icewall_group:
            image = pygame.image.load("images/environment/icewall.png").convert_alpha()
            screen.blit(image, (icewall.rect.x, icewall.rect.y - 10))
    
    