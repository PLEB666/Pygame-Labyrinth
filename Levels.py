from constants import (
    APPLE,
    BOMB_ITEM,
    CLOCK_TIME,
    DOOR,
    ENEMYA,
    ENEMYB,
    ENEMYC,
    KEY,
    PLAYER,
    TILEWIDTH,
    WALL,
    WEAPON_UPGRADE,
)
from Game_groups import *
from Game_objects import *
from Sprites import *
from Tile import Tile

# 0 = Empty
# 1 = Wall
# 2 = Door
# 3 = Key
# 4 = Apple
# 5 = Weapon Upgrade item
# 6 = Extra Time
# 7 = Bomb item

# 9 = Player

# 12 = Enemy A
# 13 = Enemy B
# 14 = Enemy C

room_map_lvl1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 4, 0, 0, 0, 1, 0, 4, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 4, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 7, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 13, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 4, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 6, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 4, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 0, 1, 0, 0, 1],
    [1, 0, 14, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 1, 0, 0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

room_map_lvl2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 4, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 4, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 12, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 5, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 4, 13, 1, 1, 0, 1, 0, 0, 1, 0, 4, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 4, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 7, 0, 1],
    [1, 4, 1, 0, 0, 0, 6, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 2, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 3, 1, 1, 1, 0, 0, 4, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 4, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

room_map_lvl3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 9, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 7, 1, 0, 1, 0, 4, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 4, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 4, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 12, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 4, 6, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 13, 0, 0, 0, 4, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 7, 1, 14, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 4, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 4, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


# lvl 1
def lvl1():
    # Generate map
    for y in range(len(room_map_lvl1)):
        for x in range(len(room_map_lvl1[y])):
            # Wall
            if room_map_lvl1[y][x] == WALL:
                w = Tile(x * TILEWIDTH, y * TILEWIDTH, wall)
                wall_group.add(w)
                gameobject_group.add(w)
            # Door
            elif room_map_lvl1[y][x] == DOOR:
                closedDoor_lvl1 = Tile(x * TILEWIDTH, y * TILEWIDTH, closedDoor_surface)
                gameobject_group.add(closedDoor_lvl1)
                openDoor_lvl1.set_position(x * TILEWIDTH, y * TILEWIDTH)
            # Key
            elif room_map_lvl1[y][x] == KEY:
                key_lvl1 = Tile(x * TILEWIDTH, y * TILEWIDTH, key)
                key_group.add(key_lvl1)
                gameobject_group.add(key_lvl1)
            # Apple
            elif room_map_lvl1[y][x] == APPLE:
                a = Tile(x * TILEWIDTH, y * TILEWIDTH, apple)
                healobject_group.add(a)
                gameobject_group.add(a)
            # Clock
            elif room_map_lvl1[y][x] == CLOCK_TIME:
                c = Tile(x * TILEWIDTH, y * TILEWIDTH, clock_time)
                clockobject_group.add(c)
                gameobject_group.add(c)
            # Weapon Upgrade item
            elif room_map_lvl1[y][x] == WEAPON_UPGRADE:
                u = Tile(x * TILEWIDTH, y * TILEWIDTH, upgrade)
                upgradeobject_group.add(u)
                gameobject_group.add(u)
            # Bomb item
            elif room_map_lvl1[y][x] == BOMB_ITEM:
                b = Tile(x * TILEWIDTH, y * TILEWIDTH, bomb)
                bombobject_group.add(b)
                gameobject_group.add(b)
            # Enemy A
            elif room_map_lvl1[y][x] == ENEMYA:
                enemya_lvl1.set_enemy(x * TILEWIDTH, y * TILEWIDTH)
                gameobject_group.add(enemya_lvl1)
                enemy_group.add(enemya_lvl1)
            # Enemy B
            elif room_map_lvl1[y][x] == ENEMYB:
                enemyb_lvl1.set_enemy(x * TILEWIDTH, y * TILEWIDTH)
                enemy_group.add(enemyb_lvl1)
                gameobject_group.add(enemyb_lvl1)
            # Enemy C
            elif room_map_lvl1[y][x] == ENEMYC:
                enemyc_lvl1.set_enemy(x * TILEWIDTH, y * TILEWIDTH)
                enemy_group.add(enemyc_lvl1)
                gameobject_group.add(enemyc_lvl1)
            # Player
            elif room_map_lvl1[y][x] == PLAYER:
                player.set_player(x * TILEWIDTH, y * TILEWIDTH)
                gameobject_group.add(player)


#######################################################################################
# lvl 2
def lvl2():
    # Empty groups for next level
    gameobject_group.empty()
    enemy_group.empty()
    door_group.empty()
    wall_group.empty()
    healobject_group.empty()
    key_group.empty()

    # Generate map
    for y in range(len(room_map_lvl2)):
        for x in range(len(room_map_lvl2[y])):
            # Wall
            if room_map_lvl2[y][x] == WALL:
                w = Tile(x * TILEWIDTH, y * TILEWIDTH, wall)
                wall_group.add(w)
                gameobject_group.add(w)
            # Door
            elif room_map_lvl2[y][x] == DOOR:
                closedDoor_lvl2 = Tile(x * TILEWIDTH, y * TILEWIDTH, closedDoor_surface)
                gameobject_group.add(closedDoor_lvl2)
                openDoor_lvl2.set_position(x * TILEWIDTH, y * TILEWIDTH)
            # Key
            elif room_map_lvl2[y][x] == KEY:
                key_lvl2 = Tile(x * TILEWIDTH, y * TILEWIDTH, key)
                key_group.add(key_lvl2)
                gameobject_group.add(key_lvl2)
            # Apple
            elif room_map_lvl2[y][x] == APPLE:
                a = Tile(x * TILEWIDTH, y * TILEWIDTH, apple)
                healobject_group.add(a)
                gameobject_group.add(a)
            # Clock
            elif room_map_lvl2[y][x] == CLOCK_TIME:
                c = Tile(x * TILEWIDTH, y * TILEWIDTH, clock_time)
                clockobject_group.add(c)
                gameobject_group.add(c)
            # Bomb item
            elif room_map_lvl2[y][x] == BOMB_ITEM:
                b = Tile(x * TILEWIDTH, y * TILEWIDTH, bomb)
                bombobject_group.add(b)
                gameobject_group.add(b)
            # Weapon Upgrade item
            elif room_map_lvl2[y][x] == WEAPON_UPGRADE:
                u = Tile(x * TILEWIDTH, y * TILEWIDTH, upgrade)
                upgradeobject_group.add(u)
                gameobject_group.add(u)
            # Enemy A
            elif room_map_lvl2[y][x] == ENEMYA:
                enemya_lvl2.set_enemy(x * TILEWIDTH, y * TILEWIDTH)
                gameobject_group.add(enemya_lvl2)
                enemy_group.add(enemya_lvl2)
            # Enemy B
            elif room_map_lvl2[y][x] == ENEMYB:
                enemyb_lvl2.set_enemy(x * TILEWIDTH, y * TILEWIDTH)
                enemy_group.add(enemyb_lvl2)
                gameobject_group.add(enemyb_lvl2)
            # Enemy C
            elif room_map_lvl2[y][x] == ENEMYC:
                enemyc_lvl2.set_enemy(x * TILEWIDTH, y * TILEWIDTH)
                enemy_group.add(enemyc_lvl2)
                gameobject_group.add(enemyc_lvl2)
            # Player
            elif room_map_lvl2[y][x] == PLAYER:
                player.set_player(x * TILEWIDTH, y * TILEWIDTH)
                gameobject_group.add(player)


#######################################################################################
# lvl 3
def lvl3():
    # Empty groups for next level
    gameobject_group.empty()
    enemy_group.empty()
    door_group.empty()
    wall_group.empty()
    healobject_group.empty()
    key_group.empty()

    # Generate map
    for y in range(len(room_map_lvl3)):
        for x in range(len(room_map_lvl3[y])):
            # Wall
            if room_map_lvl3[y][x] == WALL:
                w = Tile(x * TILEWIDTH, y * TILEWIDTH, wall)
                wall_group.add(w)
                gameobject_group.add(w)
            # Door
            elif room_map_lvl3[y][x] == DOOR:
                closedDoor_lvl3 = Tile(x * TILEWIDTH, y * TILEWIDTH, closedDoor_surface)
                gameobject_group.add(closedDoor_lvl3)
                openDoor_lvl3.set_position(x * TILEWIDTH, y * TILEWIDTH)
            # Key
            elif room_map_lvl3[y][x] == KEY:
                key_lvl3 = Tile(x * TILEWIDTH, y * TILEWIDTH, key)
                key_group.add(key_lvl3)
                gameobject_group.add(key_lvl3)
            # Apple
            elif room_map_lvl3[y][x] == APPLE:
                a = Tile(x * TILEWIDTH, y * TILEWIDTH, apple)
                healobject_group.add(a)
                gameobject_group.add(a)
            # Clock
            elif room_map_lvl3[y][x] == CLOCK_TIME:
                c = Tile(x * TILEWIDTH, y * TILEWIDTH, clock_time)
                clockobject_group.add(c)
                gameobject_group.add(c)
            # Weapon Upgrade item
            elif room_map_lvl3[y][x] == WEAPON_UPGRADE:
                u = Tile(x * TILEWIDTH, y * TILEWIDTH, upgrade)
                upgradeobject_group.add(u)
                gameobject_group.add(u)
            # Bomb item
            elif room_map_lvl3[y][x] == BOMB_ITEM:
                b = Tile(x * TILEWIDTH, y * TILEWIDTH, bomb)
                bombobject_group.add(b)
                gameobject_group.add(b)
            # Enemy A
            elif room_map_lvl3[y][x] == ENEMYA:
                enemya_lvl3.set_enemy(x * TILEWIDTH, y * TILEWIDTH)
                gameobject_group.add(enemya_lvl3)
                enemy_group.add(enemya_lvl3)
            # Enemy B
            elif room_map_lvl3[y][x] == ENEMYB:
                enemyb_lvl3.set_enemy(x * TILEWIDTH, y * TILEWIDTH)
                enemy_group.add(enemyb_lvl3)
                gameobject_group.add(enemyb_lvl3)
            # Enemy C
            elif room_map_lvl3[y][x] == ENEMYC:
                enemyc_lvl3.set_enemy(x * TILEWIDTH, y * TILEWIDTH)
                enemy_group.add(enemyc_lvl3)
                gameobject_group.add(enemyc_lvl3)
            # Player
            elif room_map_lvl3[y][x] == PLAYER:
                player.set_player(x * TILEWIDTH, y * TILEWIDTH)
                gameobject_group.add(player)
