import random

import pygame

from constants import *
from Sprites import *


#######################################################################################
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x:int, pos_y:int, health:int, speed:int, damage:int):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.__move_x = 0
        self.__move_y = 0
        self.__health = health
        self.__speed = speed
        self.__damage = damage
        self.current_direction = None
        self.next_direction = None
        

    def update(self):
        self.rect.y += self.__move_y
        self.rect.x += self.__move_x
        self.current_direction = self.next_direction
        if self.current_direction is None:
            self.next_direction = random.choice(["up", "down", "left", "right"])
        elif self.current_direction == "up":
            self.__move_x = 0
            self.__move_y = -self.__speed
        elif self.current_direction == "down":
            self.__move_x = 0
            self.__move_y = self.__speed
        elif self.current_direction == "left":
            self.__move_y = 0
            self.__move_x = -self.__speed
        elif self.current_direction == "right":
            self.__move_y = 0
            self.__move_x = self.__speed
    
    # If enemy collision with wall : choose new path/way to move
    def redirect_enemy(self):
        if self.current_direction == "up" or self.current_direction == "down":
            self.next_direction = random.choice(["left", "right"])
        elif self.current_direction == "left" or self.current_direction == "right":
            self.next_direction = random.choice(["up", "down"])
    
    # If enemy collision with wall : correct enemy
    def correct_enemy(self):
        if self.current_direction == "up":
            self.rect.y += self.__speed
            self.__move_x = 0
            self.__move_y = 0
        elif self.current_direction == "down":
            self.rect.y -= self.__speed
            self.__move_x = 0
            self.__move_y = 0
        elif self.current_direction == "right":
            self.rect.x -= self.__speed
            self.__move_x = 0
            self.__move_y = 0
        elif self.current_direction == "left":
            self.rect.x += self.__speed
            self.__move_x = 0
            self.__move_y = 0
    
    def damage_enemy(self, damage_player:int):
        self.__health -= damage_player
    
    def get_enemy_damage(self) -> int:
        return self.__damage
    
    def get_enemy_health(self) -> int:
        return self.__health

    def get_enemy_speed(self) -> int:
        return self.__speed
    
    def set_enemy(self, pos_x:int, pos_y:int):
        self.rect.topleft = (pos_x, pos_y)