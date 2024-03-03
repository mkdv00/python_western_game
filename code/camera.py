import pygame
from pygame.math import Vector2
from settings import WINDOW_HEIGHT, WINDOW_WIDTH


class AllSprites(pygame.sprite.Group):
    
    def __init__(self):
        super().__init__()
        
        self.offset = Vector2()
        self.screen = pygame.display.get_surface()
        self.bg = pygame.image.load('graphics/other/bg.png').convert()
    
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - (WINDOW_WIDTH / 2)
        self.offset.y = player.rect.centery - (WINDOW_HEIGHT / 2)
        
        self.screen.blit(source=self.bg, dest=-self.offset)
        
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_rect = sprite.image.get_rect(center=sprite.rect.center)
            offset_rect.center -= self.offset
            self.screen.blit(source=sprite.image, dest=offset_rect)
    