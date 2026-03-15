import pygame

from constants import (
    BLACK,
    BOMB_DAMAGE,
    FPS,
    FRUIT_HEAL,
    INVENTORY_POS,
    LVL_TIME,
    OPEN_INVENTORY_DELAY,
    RED,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SHOOT_DAMAGE_TIME,
    SLOT1,
    SLOT2,
    SLOT3,
    SLOT4,
    SLOT5,
    SLOT6,
    SLOT7,
    SLOT8,
    SLOTUPGRADE,
    STATS_LINE1,
    STATS_LINE2,
    STATS_LINE3,
    STATS_LINE4,
    STATS_ROW1,
    STATS_ROW2,
    STATS_ROW3,
    TILEWIDTH,
    WHITE,
    WIN_LOSE_POS,
)
from Game_groups import *
from Game_objects import *
from Levels import lvl1, lvl2, lvl3
from Sprites import *
from Tile import Tile
from Weapon import Weapon

#######################################################################################
# Initialize the game engine
pygame.init()

# Game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Labyrinth Spiel")

# Clock to control the framerate
clock = pygame.time.Clock()

# Variablen
tickrate_counter = LVL_TIME*FPS
inventory_open_delay = 0
damage_timer = 0
can_shoot_timer = 0

# True/False statements
level_generated = False

inventory_open = False
open_inventory = False
key_found = False
bomb_found = False

upgrade_collected = False

game_state = True
game_won = False

at_lvl1 = True
at_lvl2 = False
at_lvl3 = False

# Inventory slots occupied or not
invslot_1 = False
invslot_2 = False
invslot_3 = False
invslot_4 = False
invslot_5 = False
invslot_6 = False
invslot_7 = False
invslot_8 = False

# Fonts
font = pygame.font.SysFont("Snap ITC", 15)
fontWin = pygame.font.SysFont("Snap ITC", 80)
textFont = pygame.font.SysFont("SNAP ITC", 14)

# Statistics on screen
lose_text = fontWin.render("You lose", True, RED)
win_text = fontWin.render("You win", True, WHITE)

# Enemy names
enemya_name = textFont.render("Enemy 1", True, RED)
enemyb_name = textFont.render("Enemy 2", True, RED)
enemyc_name = textFont.render("Enemy 3", True, RED)

# Enemy dead text
enemya_dead = textFont.render("Dead", True, RED)
enemyb_dead = textFont.render("Dead", True, RED)
enemyc_dead = textFont.render("Dead", True, RED)
#######################################################################################
# GAME LOOP
running = True
while running:
#######################################################################################
    # USER INTERACTION (event handling)
    for event in pygame.event.get():
        # Close the game window
        if event.type == pygame.QUIT:
            running = False

        # Stop player if he doesn't press anything
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player.stop_y()
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.stop_x()

    # Generate level 1
    if level_generated == False:
        lvl1()
        level_generated = True
    if game_state == True:
        
        # Mouse location
        mouse_position_x = pygame.mouse.get_pos()[0]
        mouse_position_y = pygame.mouse.get_pos()[1]
        # Check if left click presed
        left_clicked = pygame.mouse.get_pressed()[0]
        
        # Check if keyboard button pressed
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_w]:
            player.move_up()
        if pressed[pygame.K_s]:
            player.move_down()
        if pressed[pygame.K_a]:
            player.move_left()
        if pressed[pygame.K_d]:
            player.move_right()
        if pressed[pygame.K_SPACE] and can_shoot_timer <= 0:
            can_shoot_timer = SHOOT_DAMAGE_TIME*FPS
            laser = Weapon(player.rect.centerx, player.rect.centery, player.get_direction())
            weapon_group.add(laser)
            gameobject_group.add(laser)
        # Set bomb on field
        if inventory_open == False and left_clicked:
            for item in inventoryPlayer:
                if item == "bombPlayer":
                    bombOnField = Tile(mouse_position_x-TILEWIDTH/2, mouse_position_y-TILEWIDTH/2, bomb)
                    gameobject_group.add(bombOnField)
                    bombobject_group.add(bombOnField)
                    inventoryPlayer.remove("bombPlayer")
        # Inventory open/close
        if pressed[pygame.K_e] and inventory_open_delay <= 0:
            inventory_open_delay = OPEN_INVENTORY_DELAY*FPS
            if inventory_open == False:
                # Open Inventory
                open_inventory = True
            else:
                # Close inventory and set all variables to False
                open_inventory = False
                inventory_open = False
                
                key_found = False
                bomb_found = False
                
                invslot_1 = False
                invslot_2 = False
                invslot_3 = False
                invslot_4 = False
                invslot_5 = False
                invslot_6 = False
                invslot_7 = False
                invslot_8 = False
            
####################################################################################################################
        if inventory_open == False:
            # UPDATE
            # Update all gameobjects in the gameobject_group
            gameobject_group.update()

############# Player collisions ####################################################################################
            # Check for player collision with wall
            collided_wall = pygame.sprite.spritecollide(player, wall_group, False)
            if collided_wall:
                player.correct_player()
            # Check for player collision with enemy
            collided_player_enemy = pygame.sprite.spritecollide(player, enemy_group, False)
            if collided_player_enemy and damage_timer <= 0:
                player.damage_player(enemy.get_enemy_damage())
                damage_timer = SHOOT_DAMAGE_TIME*FPS
            # Damage timer
            damage_timer -= 1
            # Check for player collision with upgrade
            collected_upgrade = pygame.sprite.spritecollide(player, upgradeobject_group, True)
            if collected_upgrade:
                player.upgrade_player(20)
                upgrade_collected = True
            # Check for player collision with heal item
            collided_healobject = pygame.sprite.spritecollide(player, healobject_group, True)
            if collided_healobject:
                player.heal_player(FRUIT_HEAL)
            # Check for player collision with clock item
            collided_clockobject = pygame.sprite.spritecollide(player, clockobject_group, True)
            if collided_clockobject:
                tickrate_counter += 10*FPS
            # Check for player collision with bomb item
            collided_bombobject = pygame.sprite.spritecollide(player, bombobject_group, True)
            if collided_bombobject:
                inventoryPlayer.append("bombPlayer")
            # Check for player collision with key
            collected_key = pygame.sprite.spritecollide(player, key_group, True)
            if collected_key:
                inventoryPlayer.append("keyPlayer")
                if at_lvl1 == True:
                    gameobject_group.remove(closedDoor_lvl1)
                    door_group.add(openDoor_lvl1)
                elif at_lvl2 == True:
                    gameobject_group.remove(closedDoor_lvl2)
                    door_group.add(openDoor_lvl2)
                elif at_lvl3 == True:
                    gameobject_group.remove(closedDoor_lvl3)
                    door_group.add(openDoor_lvl3)
            # Check for player collision with door
            collision_openDoor = pygame.sprite.spritecollide(player, door_group, False)
            if collision_openDoor:
                # Transition to lvl 2
                if at_lvl1 == True:
                    lvl2()
                    inventoryPlayer.remove("keyPlayer")
                    at_lvl1 = False
                    at_lvl2 = True
                    at_lvl3 = False
                    tickrate_counter = LVL_TIME*FPS   
                # Transition to lvl 3
                elif at_lvl2 == True:
                    lvl3()
                    inventoryPlayer.remove("keyPlayer") 
                    at_lvl1 = False
                    at_lvl2 = False
                    at_lvl3 = True
                    tickrate_counter = LVL_TIME*FPS
                # Win screen for lvl 3
                elif at_lvl3 == True:
                    game_won = True
                    game_state = False

############# Laser collision ########################################################################################
            # Check for laser collision with wall
            collided_laser_wall = pygame.sprite.groupcollide(weapon_group, wall_group, True, False)
            if collided_laser_wall:
                weapon_group.remove(laser)
            # Delay weapon shoot time
            can_shoot_timer -= 1

############# Enemy collision #########################################################################################
            # Check for enemy collision with wall
            collided_enemy_wall = pygame.sprite.groupcollide(enemy_group, wall_group, False, False)
            if collided_enemy_wall:
                for enemy in collided_enemy_wall:
                    enemy.correct_enemy()
                    enemy.redirect_enemy()
            # Check for laser collision with enemy
            collided_laser_enemy = pygame.sprite.groupcollide(enemy_group, weapon_group, False, True)
            if collided_laser_enemy:
                for enemy in collided_laser_enemy:
                    damage_player = player.get_player_damage()
                    enemy.damage_enemy(damage_player)
            # Check for enemy collision with bomb
            collided_enemy_bomb = pygame.sprite.groupcollide(enemy_group, bombobject_group, False, True)
            if collided_enemy_bomb:
                for enemy in collided_enemy_bomb:
                    enemy.damage_enemy(BOMB_DAMAGE)
                    gameobject_group.remove(bombOnField)
                    bombobject_group.remove(bombOnField)
            # Check if enemy is at 0 health
            for enemy in enemy_group:
                if enemy.get_enemy_health() <= 1:
                    enemy_group.remove(enemy)
                    gameobject_group.remove(enemy)

############# Update time #############################################################################################  
            # Time, Score text
            tickrate_counter -= 1
            game_time = tickrate_counter//FPS
            time_text = font.render("Time: " + str(game_time) + " Seconds", True, WHITE)

######### Update enemy stats ##########################################################################################
        # Enemy stats in inventory
        if at_lvl1:
            # Enemy a health, damage, speed stats
            enemya_lvl1_health = textFont.render("Health: " + str(enemya_lvl1.get_enemy_health()), True, WHITE)
            enemya_lvl1_damage = textFont.render("Damage: " + str(enemya_lvl1.get_enemy_damage()), True, WHITE)
            enemya_lvl1_speed = textFont.render("Speed: " + str(enemya_lvl1.get_enemy_speed()), True, WHITE)
            # Enemy b health, damage, speed stats
            enemyb_lvl1_health = textFont.render("Health: " + str(enemyb_lvl1.get_enemy_health()), True, WHITE)
            enemyb_lvl1_damage = textFont.render("Damage: " + str(enemyb_lvl1.get_enemy_damage()), True, WHITE)
            enemyb_lvl1_speed = textFont.render("Speed: " + str(enemyb_lvl1.get_enemy_speed()), True, WHITE)
            # Enemy c health, damage, speed stats
            enemyc_lvl1_health = textFont.render("Health: " + str(enemyc_lvl1.get_enemy_health()), True, WHITE)
            enemyc_lvl1_damage = textFont.render("Damage: " + str(enemyc_lvl1.get_enemy_damage()), True, WHITE)
            enemyc_lvl1_speed = textFont.render("Speed: " + str(enemyc_lvl1.get_enemy_speed()), True, WHITE)
        if at_lvl2:
            # Enemy a health, damage, speed stats
            enemya_lvl2_health = textFont.render("Health: " + str(enemya_lvl2.get_enemy_health()), True, WHITE)
            enemya_lvl2_damage = textFont.render("Damage: " + str(enemya_lvl2.get_enemy_damage()), True, WHITE)
            enemya_lvl2_speed = textFont.render("Speed: " + str(enemya_lvl2.get_enemy_speed()), True, WHITE)
            # Enemy b health, damage, speed stats
            enemyb_lvl2_health = textFont.render("Health: " + str(enemyb_lvl2.get_enemy_health()), True, WHITE)
            enemyb_lvl2_damage = textFont.render("Damage: " + str(enemyb_lvl2.get_enemy_damage()), True, WHITE)
            enemyb_lvl2_speed = textFont.render("Speed: " + str(enemyb_lvl2.get_enemy_speed()), True, WHITE)
            # Enemy c health, damage, speed stats
            enemyc_lvl2_health = textFont.render("Health: " + str(enemyc_lvl2.get_enemy_health()), True, WHITE)
            enemyc_lvl2_damage = textFont.render("Damage: " + str(enemyc_lvl2.get_enemy_damage()), True, WHITE)
            enemyc_lvl2_speed = textFont.render("Speed: " + str(enemyc_lvl2.get_enemy_speed()), True, WHITE)
        if at_lvl3:
            # Enemy a health, damage, speed stats
            enemya_lvl3_health = textFont.render("Health: " + str(enemya_lvl3.get_enemy_health()), True, WHITE)
            enemya_lvl3_damage = textFont.render("Damage: " + str(enemya_lvl3.get_enemy_damage()), True, WHITE)
            enemya_lvl3_speed = textFont.render("Speed: " + str(enemya_lvl3.get_enemy_speed()), True, WHITE)
            # Enemy b health, damage, speed stats
            enemyb_lvl3_health = textFont.render("Health: " + str(enemyb_lvl3.get_enemy_health()), True, WHITE)
            enemyb_lvl3_damage = textFont.render("Damage: " + str(enemyb_lvl3.get_enemy_damage()), True, WHITE)
            enemyb_lvl3_speed = textFont.render("Speed: " + str(enemyb_lvl3.get_enemy_speed()), True, WHITE)
            # Enemy c health, damage, speed stats
            enemyc_lvl3_health = textFont.render("Health: " + str(enemyc_lvl3.get_enemy_health()), True, WHITE)
            enemyc_lvl3_damage = textFont.render("Damage: " + str(enemyc_lvl3.get_enemy_damage()), True, WHITE)
            enemyc_lvl3_speed = textFont.render("Speed: " + str(enemyc_lvl3.get_enemy_speed()), True, WHITE)
        
        # Delay to open inventory
        inventory_open_delay -= 1
#######################################################################################
        # RENDER
        # Clear the screen
        screen.fill(BLACK)

        # Draw game texts, walls, doors, collected items
        gameobject_group.draw(screen)
        door_group.draw(screen)
        # Draw game Time text
        screen.blit(time_text, (1, 1))
        # Draw Player health
        health_text = font.render("Health: " + str(player.get_player_health()) + "/100", True, WHITE)
        screen.blit(health_text, (1, 19*TILEWIDTH))
    	
        # Inventory
        if open_inventory == True:
            inventory_open = True
            screen.blit(inventory, (INVENTORY_POS))
            # Check for upgrade in inventory and draw
            if upgrade_collected:
                screen.blit(upgrade_inInventory, (SLOTUPGRADE))
            
            # Check for all items in inventory to draw
            for item in inventoryPlayer:
                # Check for key in inventory and draw
                if item == "keyPlayer":
                    if key_found == False:
                        if invslot_1 == False:
                            key_found = True
                            invslot_1 = True
                            slot_key = SLOT1
                        elif invslot_2 == False:
                            key_found = True
                            invslot_2 = True
                            slot_key = SLOT2
                        elif invslot_3 == False:
                            key_found = True
                            invslot_3 = True
                            slot_key = SLOT3
                        elif invslot_4 == False:
                            key_found = True
                            invslot_4 = True
                            slot_key = SLOT4
                        elif invslot_5 == False:
                            key_found = True
                            invslot_5 = True
                            slot_key = SLOT5
                        elif invslot_6 == False:
                            key_found = True
                            invslot_6 = True
                            slot_key = SLOT6
                        elif invslot_7 == False:
                            key_found = True
                            invslot_7 = True
                            slot_key = SLOT7
                        elif invslot_8 == False:
                            key_found = True
                            invslot_8 = True
                            slot_key = SLOT8
                    else:
                        screen.blit(key_inInventory, (slot_key))
                # Check for bomb in inventory and draw
                elif item == "bombPlayer":
                    if bomb_found == False:
                        if invslot_1 == False:
                            bomb_found = True
                            invslot_1 = True
                            bomb_slot = SLOT1
                        elif invslot_2 == False:
                            bomb_found = True
                            invslot_2 = True
                            bomb_slot = SLOT2
                        elif invslot_3 == False:
                            bomb_found = True
                            invslot_3 = True
                            bomb_slot = SLOT3
                        elif invslot_4 == False:
                            bomb_found = True
                            invslot_4 = True
                            bomb_slot = SLOT4
                        elif invslot_5 == False:
                            bomb_found = True
                            invslot_5 = True
                            bomb_slot = SLOT5
                        elif invslot_6 == False:
                            bomb_found = True
                            invslot_6 = True
                            bomb_slot = SLOT6
                        elif invslot_7 == False:
                            bomb_found = True
                            invslot_7 = True
                            bomb_slot = SLOT7
                        elif invslot_8 == False:
                            bomb_found = True
                            invslot_8 = True
                            bomb_slot = SLOT8
                    else:
                        screen.blit(bomb_inInventory, (bomb_slot))
            
            # Draw enemy stats near inventoy
            if at_lvl1:
                # Show enemy A stats or alive status
                if enemya_lvl1.get_enemy_health() >= 1:
                    screen.blit(enemya_name,  (STATS_ROW1,STATS_LINE1))
                    screen.blit(enemya_lvl1_health, (STATS_ROW1,STATS_LINE2))
                    screen.blit(enemya_lvl1_damage, (STATS_ROW1,STATS_LINE3))
                    screen.blit(enemya_lvl1_speed, (STATS_ROW1,STATS_LINE4))
                else:
                    screen.blit(enemya_name,  (STATS_ROW1,STATS_LINE1))
                    screen.blit(enemya_dead, (STATS_ROW1,STATS_LINE2))
                # Show enemy B stats or alive status
                if enemyb_lvl1.get_enemy_health() >= 1:
                    screen.blit(enemyb_name,  (STATS_ROW2,STATS_LINE1))
                    screen.blit(enemyb_lvl1_health, (STATS_ROW2,STATS_LINE2))
                    screen.blit(enemyb_lvl1_damage, (STATS_ROW2,STATS_LINE3))
                    screen.blit(enemyb_lvl1_speed, (STATS_ROW2,STATS_LINE4))
                else:
                    screen.blit(enemyb_name, (STATS_ROW2,STATS_LINE1))
                    screen.blit(enemyb_dead, (STATS_ROW2,STATS_LINE2))
                # Show enemy C stats or alive status
                if enemyc_lvl1.get_enemy_health() >= 1:
                    screen.blit(enemyc_name,  (STATS_ROW3,STATS_LINE1))
                    screen.blit(enemyc_lvl1_health, (STATS_ROW3,STATS_LINE2))
                    screen.blit(enemyc_lvl1_damage, (STATS_ROW3,STATS_LINE3))
                    screen.blit(enemyc_lvl1_speed, (STATS_ROW3,STATS_LINE4))
                else:
                    screen.blit(enemyc_name, (STATS_ROW3,STATS_LINE1))
                    screen.blit(enemyc_dead, (STATS_ROW3,STATS_LINE2))
            if at_lvl2:
                # Show enemy A stats or alive status
                if enemya_lvl2.get_enemy_health() >= 1:
                    screen.blit(enemya_name,  (STATS_ROW1,STATS_LINE1))
                    screen.blit(enemya_lvl2_health, (STATS_ROW1,STATS_LINE2))
                    screen.blit(enemya_lvl2_damage, (STATS_ROW1,STATS_LINE3))
                    screen.blit(enemya_lvl2_speed, (STATS_ROW1,STATS_LINE4))
                else:
                    screen.blit(enemya_name,  (STATS_ROW1,STATS_LINE1))
                    screen.blit(enemya_dead, (STATS_ROW1,STATS_LINE2))
                # Show enemy B stats or alive status
                if enemyb_lvl2.get_enemy_health() >= 1:
                    screen.blit(enemyb_name,  (STATS_ROW2,STATS_LINE1))
                    screen.blit(enemyb_lvl2_health, (STATS_ROW2,STATS_LINE2))
                    screen.blit(enemyb_lvl2_damage, (STATS_ROW2,STATS_LINE3))
                    screen.blit(enemyb_lvl2_speed, (STATS_ROW2,STATS_LINE4))
                else:
                    screen.blit(enemyb_name, (STATS_ROW2,STATS_LINE1))
                    screen.blit(enemyb_dead, (STATS_ROW2,STATS_LINE2))
                # Show enemy C stats or alive status
                if enemyc_lvl2.get_enemy_health() >= 1:
                    screen.blit(enemyc_name,  (STATS_ROW3,STATS_LINE1))
                    screen.blit(enemyc_lvl2_health, (STATS_ROW3,STATS_LINE2))
                    screen.blit(enemyc_lvl2_damage, (STATS_ROW3,STATS_LINE3))
                    screen.blit(enemyc_lvl2_speed, (STATS_ROW3,STATS_LINE4))
                else:
                    screen.blit(enemyc_name, (STATS_ROW3,STATS_LINE1))
                    screen.blit(enemyc_dead, (STATS_ROW3,STATS_LINE2))
            if at_lvl3:
                # Show enemy A stats or alive status
                if enemya_lvl3.get_enemy_health() >= 1:
                    screen.blit(enemya_name,  (STATS_ROW1,STATS_LINE1))
                    screen.blit(enemya_lvl3_health, (STATS_ROW1,STATS_LINE2))
                    screen.blit(enemya_lvl3_damage, (STATS_ROW1,STATS_LINE3))
                    screen.blit(enemya_lvl3_speed, (STATS_ROW1,STATS_LINE4))
                else:
                    screen.blit(enemya_name,  (STATS_ROW1,STATS_LINE1))
                    screen.blit(enemya_dead, (STATS_ROW1,STATS_LINE2))
                # Show enemy B stats or alive status
                if enemyb_lvl3.get_enemy_health() >= 1:
                    screen.blit(enemyb_name,  (STATS_ROW2,STATS_LINE1))
                    screen.blit(enemyb_lvl3_health, (STATS_ROW2,STATS_LINE2))
                    screen.blit(enemyb_lvl3_damage, (STATS_ROW2,STATS_LINE3))
                    screen.blit(enemyb_lvl3_speed, (STATS_ROW2,STATS_LINE4))
                else:
                    screen.blit(enemyb_name, (STATS_ROW2,STATS_LINE1))
                    screen.blit(enemyb_dead, (STATS_ROW2,STATS_LINE2))
                # Show enemy C stats or alive status
                if enemyc_lvl3.get_enemy_health() >= 1:
                    screen.blit(enemyc_name,  (STATS_ROW3,STATS_LINE1))
                    screen.blit(enemyc_lvl3_health, (STATS_ROW3,STATS_LINE2))
                    screen.blit(enemyc_lvl3_damage, (STATS_ROW3,STATS_LINE3))
                    screen.blit(enemyc_lvl3_speed, (STATS_ROW3,STATS_LINE4))
                else:
                    screen.blit(enemyc_name, (STATS_ROW3,STATS_LINE1))
                    screen.blit(enemyc_dead, (STATS_ROW3,STATS_LINE2))
            
        # Draw lose/win condition
        if tickrate_counter <= 0 or player.get_player_health() <= 0:
            screen.blit(lose_text, WIN_LOSE_POS)
            game_state = False
        if game_won == True:
            screen.blit(win_text, WIN_LOSE_POS)
        
        # Update the screen
        pygame.display.flip()

#######################################################################################
        # Time management
        clock.tick(FPS)

pygame.quit()