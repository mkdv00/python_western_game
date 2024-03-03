import sys

import pygame
from camera import AllSprites
from player import Player
from pytmx.util_pygame import load_pygame
from settings import PATHS, WINDOW_HEIGHT, WINDOW_WIDTH
from sprite import Sprite


class Game:
    
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Western shooter')
        self.clock = pygame.Clock()
        
        # Groups
        self.all_sprites = AllSprites()
        self.obstacles = pygame.sprite.Group()
        
        self.setup()
    
    def setup(self):
        tmx_map = load_pygame(filename='data/map.tmx')
        
        # Fences
        for x, y, surf in tmx_map.get_layer_by_name('Fence').tiles():
            Sprite(pos=(x * 64, y * 64), surf=surf, groups=[self.all_sprites, self.obstacles])
        
        # Objects
        for object in tmx_map.get_layer_by_name('Objects'):
            Sprite(pos=(object.x, object.y), surf=object.image, groups=[self.all_sprites, self.obstacles])
        
        # Player
        for object in tmx_map.get_layer_by_name('Entities'):
            if object.name == 'Player':
                self.player = Player(pos=(object.x, object.y), 
                                    groups=self.all_sprites, 
                                    path=PATHS['player'], 
                                    collision_sprites=self.obstacles)
    
    def run(self):
        while True:
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Delta time
            dt = self.clock.tick() / 1000
            
            # Update groups
            self.all_sprites.update(dt)
            
            # Draw groups
            self.all_sprites.custom_draw(player=self.player)
            
            # Update the frame
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()