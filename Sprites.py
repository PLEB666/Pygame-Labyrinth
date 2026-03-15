import pygame

from constants import (
    DOOR_HEIGHT,
    GS,
    INVENTORY_SIZE,
    ITEM_LENGHT,
    ITEM_WIDTH,
    OUTOFBOUNDS,
    TILEWIDTH,
)
from Tile import Tile

# Player animations ##################################################
anim_list_img_player = []
# Bild left stay [0]
image = pygame.image.load("./Sprites/Pleftstay.png")
image = pygame.transform.scale(image, (GS, GS))
anim_list_img_player.append(image)
# Bild left 1 [1]
image = pygame.image.load("./Sprites/Pleft1.png")
image = pygame.transform.scale(image, (GS, GS))
anim_list_img_player.append(image)
# Bild left 2 [2]
image = pygame.image.load("./Sprites/Pleft2.png")
image = pygame.transform.scale(image, (GS, GS))
anim_list_img_player.append(image)

# Bild right stay [3]
image = pygame.image.load("./Sprites/Prightstay.png")
image = pygame.transform.scale(image, (GS, GS))
anim_list_img_player.append(image)
# Bild right 1 [4]
image = pygame.image.load("./Sprites/Pright1.png")
image = pygame.transform.scale(image, (GS, GS))
anim_list_img_player.append(image)
# Bild right 2 [5]
image = pygame.image.load("./Sprites/Pright2.png")
image = pygame.transform.scale(image, (GS, GS))
anim_list_img_player.append(image)

# Enemy photo #########################################################
image_enemy = pygame.image.load("./Sprites/goomba.png")
image_enemy = pygame.transform.scale(image_enemy, (TILEWIDTH, TILEWIDTH))

# Wall block photo ####################################################
wall = pygame.image.load("./Sprites/wall.png")
wall = pygame.transform.scale(wall, (TILEWIDTH, TILEWIDTH))

# Closed Door photo ###################################################
closedDoor_surface = pygame.image.load("./Sprites/closedDoor.png")
closedDoor_surface = pygame.transform.scale(closedDoor_surface, (TILEWIDTH, DOOR_HEIGHT))

# Open Door photo #####################################################
openDoor_surface = pygame.image.load("./Sprites/openDoor.png")
openDoor_surface = pygame.transform.scale(openDoor_surface, (TILEWIDTH, DOOR_HEIGHT))
openDoor_lvl1 = Tile(OUTOFBOUNDS, OUTOFBOUNDS, openDoor_surface)
openDoor_lvl2 = Tile(OUTOFBOUNDS, OUTOFBOUNDS, openDoor_surface)
openDoor_lvl3 = Tile(OUTOFBOUNDS, OUTOFBOUNDS, openDoor_surface)

# Key photo ###########################################################
key = pygame.image.load("./Sprites/key.png")
key = pygame.transform.scale(key, (TILEWIDTH, TILEWIDTH))
key_inInventory = pygame.transform.scale(key, (ITEM_LENGHT, ITEM_WIDTH))

# Full Inventory photo ################################################
inventory = pygame.image.load("./Sprites/inventory3x3.png")
inventory = pygame.transform.scale(inventory, INVENTORY_SIZE)

# Apple photo #########################################################
apple = pygame.image.load("./Sprites/apple.png")
apple = pygame.transform.scale(apple, (TILEWIDTH, TILEWIDTH))

# Clock photo #########################################################
clock_time = pygame.image.load("./Sprites/clock.png")
clock_time = pygame.transform.scale(clock_time, (TILEWIDTH, TILEWIDTH))

# Weapon Upgrade photo ################################################
upgrade = pygame.image.load("./Sprites/upgrade.png")
upgrade = pygame.transform.scale(upgrade, (TILEWIDTH, TILEWIDTH))
upgrade_inInventory = pygame.transform.scale(upgrade, (ITEM_LENGHT, ITEM_WIDTH))

# Bomb photo ##########################################################
bomb = pygame.image.load("./Sprites/bomb.png")
bomb = pygame.transform.scale(bomb, (TILEWIDTH, TILEWIDTH))
bomb_inInventory = pygame.transform.scale(bomb, (ITEM_LENGHT, ITEM_WIDTH))
