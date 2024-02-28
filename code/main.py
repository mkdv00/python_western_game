import sys

import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


class Game:
    
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Western shooter')
        self.clock = pygame.Clock()
    
    def run(self):
        while True:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # delta time
            dt = self.clock.tick() / 1000
            
            # update the frame
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()