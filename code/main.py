import sys

import pygame
from player import Player
from settings import PATHS, WINDOW_HEIGHT, WINDOW_WIDTH
from sprites import AllSprites


class Game:
    
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Western shooter')
        self.clock = pygame.Clock()
        
        # Groups
        self.all_sprites = AllSprites()
        self.setup()
    
    def setup(self):
        self.player = Player(pos=(200, 200), groups=self.all_sprites, path=PATHS['player'], collision_sprites=None)
    
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