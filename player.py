import pygame


#######################################################################################
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x: int, pos_y: int, speed: int, damage:int, anim_list_img_player:list):
        super().__init__()
        self.image = anim_list_img_player[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.__images = anim_list_img_player
        self.__anim_counter = 0
        self.__speed = speed
        self.__damage = damage
        self.__move_x = 0
        self.__move_y = 0
        self.__direction = ""
        self.__last_direction = ""
        self.__health = 100
        self.__max_health = 100
    
    def correct_player(self):
        if self.__direction == "up":
            self.rect.y += self.__speed
        elif self.__direction == "down":
            self.rect.y -= self.__speed
        elif self.__direction == "right":
            self.rect.x -= self.__speed
        elif self.__direction == "left":
            self.rect.x += self.__speed

    def update(self):
        self.rect.y += self.__move_y
        self.rect.x += self.__move_x
        
        # Animations player
        self.__anim_counter +=1
        if self.__anim_counter < 10:
            if self.__last_direction == "left":
                self.image = self.__images[1]
            else:
                self.image = self.__images[4]
        
        elif self.__anim_counter < 20:
            if self.__last_direction == "left":
                self.image = self.__images[2]
            else:
                self.image = self.__images[5]
        else:
            self.__anim_counter = 0

    def move_up(self):
        self.__move_x = 0
        self.__move_y = -self.__speed
        self.__direction = "up"

    def move_down(self):
        self.__move_x = 0
        self.__move_y = self.__speed
        self.__direction = "down"

    def move_left(self):
        self.__move_y = 0
        self.__move_x = -self.__speed
        self.__direction = "left"
        self.__last_direction = "left"

    def move_right(self):
        self.__move_y = 0
        self.__move_x = self.__speed
        self.__direction = "right"
        self.__last_direction = "right"
    
    def damage_player(self, dmg:int):
        self.__health -= dmg
    
    def heal_player(self, heal:int):
        self.__health += heal
        if self.__health > self.__max_health:
            self.__health = self.__max_health
    
    def upgrade_player(self, damage_amount:int):
        self.__damage += damage_amount
    
    def stop_x(self):
        self.__move_x = 0
  
    def stop_y(self):
        self.__move_y = 0
    
    def get_direction(self) -> str:
        return self.__direction
    
    def get_player_health(self) -> int:
        return self.__health
    
    def get_player_damage(self) -> int:
        return self.__damage
    
    def set_player(self, pos_x:int, pos_y:int):
        self.rect.topleft = (pos_x, pos_y)