from os import walk

import pygame
from pygame.math import Vector2


class Player(pygame.sprite.Sprite):
    
    def __init__(self, pos, groups, path, collision_sprites):
        # Base setup
        super().__init__(groups)
        self.import_assets(path=path)
        self.frame_index = 0
        self.state = 'down_idle'
        
        self.image = self.animations[self.state][self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        # Float based movement
        self.pos = Vector2(self.rect.center)
        self.direction = Vector2()
        self.speed = 200
        
        # Collisions
        self.hitbox = self.rect.inflate(0, -self.rect.height / 2)
        self.collision_sprites = collision_sprites
        
        # Attack
        self.attacking = False
    
    def get_state(self):
        if self.direction.x == 0 and self.direction.y == 0:
            self.state = self.state.split('_')[0] + "_idle"
        
        if self.attacking:
            self.state = self.state.split('_')[0] + "_attack"
    
    def import_assets(self, path):
        self.animations = {}
        
        for index, folder in enumerate(walk(path)):
            if index == 0:
                for name in folder[1]:
                    self.animations[name] = []
            else:
                for file_name in sorted(folder[2], key=lambda name: int(name.split('.')[0])):
                    path = folder[0].replace('\\', '/') + '/' + file_name
                    surf = pygame.image.load(file=path).convert_alpha()
                    key = folder[0].split('\\')[1]
                    self.animations[key].append(surf)
    
    def input(self):
        keys = pygame.key.get_pressed()
        
        if not self.attacking:
            # Horizontal direction
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.direction.x = 1
                self.state = 'right'
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.direction.x = -1
                self.state = 'left'
            else:
                self.direction.x = 0
            
            # Vertical direction
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.direction.y = 1
                self.state = 'down'
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                self.direction.y = -1
                self.state = 'up'
            else:
                self.direction.y = 0
        
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.direction = Vector2()
            self.frame_index = 0
    
    def move(self, dt):
        if self.direction.magnitude():
            self.direction = self.direction.normalize()
        
        # Horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx
        
        # Horizontal collision
        
        # Vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery
        
        # Vertical collision
    
    def animate(self, dt):
        current_animation = self.animations[self.state]
        
        self.frame_index += 7 * dt
        if self.frame_index >= len(current_animation):
            self.frame_index = 0
            
            if self.attacking:
                self.attacking = False
        
        self.image = current_animation[int(self.frame_index)]
    
    def update(self, dt):
        self.input()
        self.get_state()
        self.move(dt)
        self.animate(dt)
        