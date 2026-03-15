from constants import OUTOFBOUNDS, PLAYER_SPEED
from Enemy import Enemy
from player import Player
from Sprites import anim_list_img_player

# Player = Player(pos_x, pos_y, speed, damage, animation list)
player = Player(OUTOFBOUNDS, OUTOFBOUNDS, PLAYER_SPEED, 20, anim_list_img_player)

# Enemy = Enemy(pos_x, pos_y, health, speed, damage)
# Enemys lvl 1
enemya_lvl1 = Enemy(OUTOFBOUNDS, OUTOFBOUNDS, 20, 2, 20)
enemyb_lvl1 = Enemy(OUTOFBOUNDS, OUTOFBOUNDS, 35, 3, 30)
enemyc_lvl1 = Enemy(OUTOFBOUNDS, OUTOFBOUNDS, 60, 4, 45)

# Enemys lvl 2
enemya_lvl2 = Enemy(OUTOFBOUNDS, OUTOFBOUNDS, 20, 2, 20)
enemyb_lvl2 = Enemy(OUTOFBOUNDS, OUTOFBOUNDS, 35, 3, 30)
enemyc_lvl2 = Enemy(OUTOFBOUNDS, OUTOFBOUNDS, 60, 4, 45)

# Enemys lvl 3
enemya_lvl3 = Enemy(OUTOFBOUNDS, OUTOFBOUNDS, 20, 2, 20)
enemyb_lvl3 = Enemy(OUTOFBOUNDS, OUTOFBOUNDS, 35, 3, 30)
enemyc_lvl3 = Enemy(OUTOFBOUNDS, OUTOFBOUNDS, 60, 4, 45)

# Closed doors
closedDoor_lvl1 = None
closedDoor_lvl2 = None
closedDoor_lvl3 = None

# Bomb on field
bombOnField = None
