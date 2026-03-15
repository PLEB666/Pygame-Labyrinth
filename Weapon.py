import pygame
from constants import *

class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos_x:int, pos_y:int, direction:str):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.__move_x = 0
        self.__move_y = 0
        
        if direction == "left":
            self.__move_x = -PROJECTILE_SPEED
        elif direction == "right":
            self.__move_x = PROJECTILE_SPEED
        elif direction == "up":
            self.__move_y = -PROJECTILE_SPEED
        elif direction == "down":
            self.__move_y = PROJECTILE_SPEED
        
        
    def update(self):
        self.rect.x += self.__move_x
        self.rect.y += self.__move_y