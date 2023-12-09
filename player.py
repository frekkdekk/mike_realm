import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        
        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0
        
        print(self.status)
        print(self.frame_index)
        
        # general setup
        self.image = self.animations[self.status][self.frame_index] # player image
        self.rect = self.image.get_rect(center=pos) # player rect
        
        # movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        
    def import_assets(self):
        self.animations = {'up_idle':[], 'down_idle':[], 'left_idle':[], 'right_idle':[],
                           'right_idle':[], 'left_idle':[], 'up_idle':[], 'down_idle':[],
                           'right_hoe':[], 'left_hoe':[], 'up_hoe':[], 'down_hoe':[],
                           'right_axe':[], 'left_axe':[], 'up_axe':[], 'down_axe':[],
                           'right_water':[], 'left_water':[], 'up_water':[], 'down_water':[],}
        
        for animation in self.animations.keys():
            full_path = 'assets/graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)
        
        for animation in self.animations.keys():
            full_path = 'assets/graphics/characters/player/' + animation
            self.animations[animation] = import_folder(full_path)
        
    def input(self):
        keys = pygame.key.get_pressed() # player input
        
        if keys[pygame.K_UP]:
            self.direction.y = -1    # up / down
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0    
        
        if keys[pygame.K_LEFT]:
            self.direction.x = -1   # left / right
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0
            
    def move(self, dt):
        
        # normalizing vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize() # player movement mechanics
            
        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        
        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
            
    def update(self, dt):
        self.input()
        self.move(dt)