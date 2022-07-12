# ==[MULTIPLAYER/SINGLE PLAYER SHOOTER GAME]==
# Description: Video game where you will play as a shooter and you will need to shoot various targets (whether they be other players or single-player enemies)
# Author: Anindit Dewan 
# Date: July, 7th, 2022 

# Imported Packages 
import pygame
import random 
import os
from pathlib import Path

pygame.init()
win = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("ONE DIMENSIONAL SHOOTER SIMULATOR")
clock = pygame.time.Clock()


# Fade animation, fades the screen whenever user clicks a button. 
def fade(): 
    fade_animation = pygame.Surface((1200, 900))
    fade_animation.fill((0,0,0))
    for alpha in range(0, 75): 
        fade_animation.set_alpha(alpha)
        win.blit(fade_animation, (0,0))
        pygame.display.update()
        pygame.time.delay(5) 

# Class for player and player 2. There are two different classes as the two players have unique traits depending on the level. 
class Player():
    def __init__(self, x, y, color_1, color_2, color_3):
        self.x = x
        self.y = y
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = 50
        self.height = 50
        self.screen = win
        self.health = 100
        self.death = False
    def draw_soldier(self):
        pygame.draw.rect(self.screen, (self.color_1, self.color_2,
                         self.color_3), (self.x, self.y, self.width, self.height))
        self.hitbox = (self.x-25, self.y-25, 100, 100)
        pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox, 2)

    def move_soldier(self, x_velocity, y_velocity):
        self.x += x_velocity
        self.y += y_velocity
    def barrier(self): 
        if self.x > 1200:
            self.x = 1200 
        if self.x < 0: 
            self.x = 0 
        if self.y < 0: 
            self.y = 0 
        if self.y > 900: 
            self.y = 900 

    def hit(self):
        self.health -= 3
        if self.health < 0 and (start_game == True or start_game_3 == True):
            self.death = True
    def draw_health_bar(self): 
        pygame.draw.rect(self.screen, (255, 0, 0), 
                         (0, 0, 50 - ((50/10) * (10-self.health)), 50))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 50 -
                         ((50/10) * (10-self.health)), 50), 2)
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
class Player2():
    def __init__(self, x, y, color_1, color_2, color_3):
        self.x = x
        self.y = y
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = 50
        self.height = 50
        self.screen = win
        self.health = 100
        self.death = False
        self.death2 = False 

    def draw_soldier(self):
        pygame.draw.rect(self.screen, (self.color_1, self.color_2,
                         self.color_3), (self.x, self.y, self.width, self.height))
        self.hitbox = (self.x-25, self.y-25, 100, 100)
        pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox, 2)

    def move_soldier(self, x_velocity, y_velocity):
        self.x += x_velocity
        self.y += y_velocity

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def hit(self):
        self.health -= 5
        if self.health < 0 and start_game == True:
            self.death = True
            self.American_wins = True 
    def hit_2(self): 
        self.health -= 200 
        if self.health < 0 and start_game_2 == True: 
            self.death = True 
    def barrier(self): 
        if self.x > 1200:
            self.x = 1200 
        if self.x < 0: 
            self.x = 0 
        if self.y < 0: 
            self.y = 0 
        if self.y > 900: 
            self.y = 900 

    def draw_health_bar(self):
        pygame.draw.rect(self.screen, (0, 0, 255),
                         (0, 850, 50 - ((50/10) * (10 - self.health)), 50))
        pygame.draw.rect(self.screen, (0, 0, 0),
                         (0, 850, 50 - ((50/10) * (10-self.health)), 50), 2)


# Enemy class, only used for level 3. 
class Enemy(): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y
        self.screen = win
        self.width = 25 
        self.height = 25 
        self.hitbox = (self.x-9, self.y-9, 45, 45)
    def draw_enemy(self):
        pygame.draw.rect(self.screen,(0,0,255), (self.x, self.y, self.width, self.height))
        self.hitbox = (self.x-9, self.y-9, 45, 45)
        pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox, 2)

# Bullet class which will hit enemies. 
class Bullet():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.screen = win
        self.width = 50
        self.height = 10
        self.radius = 10
        self.vel = 5

    def draw_bullet(self):
        pygame.draw.circle(self.screen, (0, 0, 0),
                           (self.x, self.y), self.radius)
# Button class 
class Button(): 
    def __init__(self, color, x, y, width, height, border): 
        self.color = color
        self.x = x
        self.y = y 
        self.width = width 
        self.height = height 
        self.border = border 
    
    def draw_button(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), self.border)

    def check_mouse_position(self, pos): 
        if pos[0] > self.x and pos[0] < self.x + self.width: 
            if pos[1] > self.y and pos[1] < self.y + self.height: 
                return True 
        return False 
run = True
# Player Objects 
bullet_list = []
American_bullet_list = []
enemy_list = [] 
Canadian_soldier = Player(200, 375, 255, 0, 0)
American_soldier = Player2(900, 375, 0, 0, 255)

# Button Objects 
start_button = Button((0,0,0), 181,263,238,61, 0)
quit_button = Button((0,0,0), 181,386, 238,61, 0)
level_1_select = Button((0,0,0), 0,0,900,250, 2)
level_2_select = Button((0,0,0), 0, 250, 900, 250, 2)
level_3_select = Button((0,0,0), 0, 500, 900, 250, 2)
back_to_start = Button((0,0,0), 0,750, 1200, 150, 2)
restart_shooter = Button((255,255,255),453,559, 300, 50, 0)
main_menu_shooter = Button((255,255,255), 453,680, 300, 50, 0)
restart_survival = Button((255,255,255),453,559, 300, 50, 0)
main_menu_survival = Button((255,255,255), 453,680, 300, 50, 0)
restart_single_player = Button((255,255,255),453,559, 300, 50, 0)
main_menu_single_player = Button((255,255,255), 453,680, 300, 50, 0)
box_1 = Button((0,0,0), 900, 0, 300, 250, 2)
box_2 = Button((0,0,0), 900, 250, 300, 250, 2)
box_3 = Button((0,0,0), 900, 500, 300, 250, 2)

# Numbers and Counters 
num_enemies = 3 
num_enemies_display = 3 
velocity_direction = 1

# Fonts 
font = pygame.font.Font("C:/Users/Anind/OneDrive/Documents/Python/Multiplayer Server Game Pygame/Polymer Caps Book.ttf", 32)
larger_font = pygame.font.Font("/Users/Anind/OneDrive/Documents/Python/Multiplayer Server Game Pygame/Polymer Caps Book.ttf", 64)

# Images 
PROJECT_ROOT = Path(__file__).parent.parent
front_page = pygame.image.load(PROJECT_ROOT / "Multiplayer Server Game Pygame/Startpage.png")
level_1_icon = pygame.image.load(PROJECT_ROOT / "Multiplayer Server Game Pygame/Level_1_Icon.png")
level_2_icon = pygame.image.load(PROJECT_ROOT / "Multiplayer Server Game Pygame/Level_2_Icon.png")
level_3_icon = pygame.image.load(PROJECT_ROOT / "Multiplayer Server Game Pygame/Level_3_Icon.png")
Arrow = pygame.image.load(PROJECT_ROOT / "Multiplayer Server Game Pygame/Back.png")

# Page Booleans 
start_page = True 
start_level_select = False 
start_game = False 
start_game_2 = False
start_game_3 = False

# Game Booleans 
shoot_left = False 
shoot_right = False 

# Timer 
time_counter = 60
survival_timer = 0 
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)
mouse_counter = 0 
start_timer = True

# Scores
single_player_score = 0 
if os.path.exists("score.txt"):
    with open("score.txt", "r") as file: 
        high_score = int(file.read())
else: 
    high_score = 0 

while run:
    pygame.time.delay(50)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        mouse_position = pygame.mouse.get_pos() 
        if event.type == pygame.QUIT:
            run = False
        # All mouse keys for buttons. 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if start_button.check_mouse_position(mouse_position) and start_page == True:
                print("START BUTTON CLICKED")
                fade()
                start_page = False 
                start_level_select = True 
            if quit_button.check_mouse_position(mouse_position) and start_page == True: 
                print("QUIT BUTTON CLICKED")
                pygame.quit() 
            if level_1_select.check_mouse_position(mouse_position) and start_level_select == True:
                print("LEVEL 1 BUTTON CLICKED")
                fade() 
                start_level_select = False 
                start_game = True 
                mouse_counter = 0 
            if level_2_select.check_mouse_position(mouse_position) and start_level_select == True: 
                mouse_counter += 1 
                print("LEVEL 2 BUTTON CLICKED")
                if (mouse_counter == 2):
                    fade() 
                    start_level_select = False  
                    start_game_2 = True 
                    mouse_counter = 0 
            if level_3_select.check_mouse_position(mouse_position) and start_level_select == True: 
                print("LEVEL 3 BUTTON CLICKED") 
                fade() 
                start_level_select = False 
                start_game_3 = True 
                mouse_counter = 0 
            if back_to_start.check_mouse_position(mouse_position) and start_level_select == True: 
                print("BACK TO HOME") 
                fade() 
                start_level_select = False 
                start_page = True 
                mouse_counter = 0 
            if main_menu_shooter.check_mouse_position(mouse_position) and start_game == True:
                print("MAIN MENU LEVEL 1")
                restart() 
                fade() 
                start_game = False 
                start_page = True  
            if restart_shooter.check_mouse_position(mouse_position) and start_game == True: 
                print("RESTART LEVEL 1")
                restart()
                fade() 
            if restart_survival.check_mouse_position(mouse_position) and start_game_2 == True: 
                print("RESTART LEVEL 2")
                restart()  
                fade() 
                time_counter = 60
            if main_menu_survival.check_mouse_position(mouse_position) and start_game_2 == True:
                print("MAIN MENU SURVIVAL") 
                restart() 
                time_counter = 60
                fade()  
                start_game_2 = False 
                start_page = True 
            if main_menu_single_player.check_mouse_position(mouse_position) and start_game_3 == True: 
                print("MAIN MENU SINGLEPLAYER")
                restart()
                num_enemies = 3 
                enemy_list = []
                single_player_score = 0 
                survival_timer = 0 
                start_timer = True 
                fade()
                start_game_3 = False 
                start_page = True 
            if restart_single_player.check_mouse_position(mouse_position) and start_game_3 == True: 
                print("RESTART LEVEL 3")
                restart() 
                num_enemies = 3 
                enemy_list = []
                single_player_score = 0 
                survival_timer = 0 
                start_timer = True 
                fade() 
        # Timer for level 2 
        if event.type == timer_event: 
            if time_counter > 0 and start_timer == True and start_game_2 == True: 
                time_counter -= 1
            if start_game_3 == True and start_timer == True: 
                survival_timer += 1 
            if start_game_3 == True and start_timer == False: 
                survival_timer = survival_timer + 0 
    # Movement functions for player(s) 1 and 2, repeated in all levels 
    def move_1(): 
        if keys[pygame.K_RIGHT]:
            Canadian_soldier.move_soldier(20, 0) 
        if keys[pygame.K_LEFT]:
            Canadian_soldier.move_soldier(-20, 0)
        if keys[pygame.K_UP]:
            Canadian_soldier.move_soldier(0, -20)
        if keys[pygame.K_DOWN]:
            Canadian_soldier.move_soldier(0, 20)
    def move_2(): 
        if keys[pygame.K_d]:
            American_soldier.move_soldier(20, 0)
        if keys[pygame.K_a]:
            American_soldier.move_soldier(-20, 0)
        if keys[pygame.K_w]:
            American_soldier.move_soldier(0, -20)
        if keys[pygame.K_s]:
            American_soldier.move_soldier(0, 20)
    # Shoots bullet, reapeted for all 3 levels. 
    def shoot(): 
        if keys[pygame.K_BACKSLASH]:
            if len(bullet_list) < 6:
                bullet_list.append(Bullet(Canadian_soldier.x, Canadian_soldier.y))
        if keys[pygame.K_SPACE]:
            if len(American_bullet_list) < 6:
                American_bullet_list.append(Bullet(American_soldier.x, American_soldier.y))
    # Create enemy NPC's randomly for level 3 
    def create_enemy(length): 
        random_x = random.randint(800,1200)
        random_y = random.randint(200,700)
        if len(enemy_list) < length: 
            enemy_list.append(Enemy(random_x, random_y))
    # Start page of the game 
    if start_page == True: 
        win.blit(front_page, (0,0))
    # Level select menu, user can choose between the three game modes. 
    if start_level_select == True: 
        win.fill((229,220,224))
        level_1_font = larger_font.render("ONE VERSUS ONE", True, (0,0,0))
        level_2_font = larger_font.render("SURVIVE", True, (0,0,0))
        level_3_font = larger_font.render("SINGLEPLAYER", True, (0,0,0))
        level_1_select.draw_button() 
        level_2_select.draw_button() 
        level_3_select.draw_button() 
        box_1.draw_button()
        box_2.draw_button()
        box_3.draw_button()
        back_to_start.draw_button()
        win.blit(level_1_font, (250, 100))
        win.blit(level_2_font, (350, 350))
        win.blit(level_3_font, (285, 600))
        win.blit(level_1_icon, (900, 0))
        win.blit(level_2_icon, (900, 250))
        win.blit(level_3_icon, (900, 500))
        win.blit(Arrow, (0,750))
    # Game #1 - Multiplayer game where two players can shoot each other and the one who dies first will lose the game. 
    if American_soldier.death == False and Canadian_soldier.death == False and start_game == True:
        for bullet in bullet_list:
            if bullet.y - bullet.radius < American_soldier.hitbox[1] + American_soldier.hitbox[3] and bullet.y + bullet.radius > American_soldier.hitbox[1]:
                if bullet.x + bullet.radius > American_soldier.hitbox[0] and bullet.x - bullet.radius < American_soldier.hitbox[0] + American_soldier.hitbox[2]:
                    American_soldier.hit()
                    bullet_list.pop(bullet_list.index(bullet))

            if bullet.x < 1200 and bullet.x > 0:
                bullet.x += 40 * velocity_direction 
            else:
                bullet_list.pop(bullet_list.index(bullet))

        for American_bullet in American_bullet_list:
            if American_bullet.y - American_bullet.radius < Canadian_soldier.hitbox[1] + Canadian_soldier.hitbox[3] and American_bullet.y + American_bullet.radius > Canadian_soldier.hitbox[1]:
                if American_bullet.x + American_bullet.radius > Canadian_soldier.hitbox[0] and American_bullet.x - American_bullet.radius < Canadian_soldier.hitbox[0] + Canadian_soldier.hitbox[2]:
                    Canadian_soldier.hit()
                    American_bullet_list.pop(American_bullet_list.index(American_bullet))

            if American_bullet.x > 0 and American_bullet.x < 1200:
                American_bullet.x -= 40
            else:
                American_bullet_list.pop(American_bullet_list.index(American_bullet))
        move_1() 
        move_2() 
        shoot()
        win.fill((255, 255, 255))
        pygame.draw.rect(win, (0,0,0), (500, 850, 700,50))
        pygame.draw.rect(win,(0,0,0), (500,0, 700, 50))
        Canadian_soldier.draw_soldier() 
        American_soldier.draw_soldier()
        American_soldier.barrier() 
        Canadian_soldier.barrier() 
        American_soldier.draw_health_bar()
        Canadian_soldier.draw_health_bar() 
        for bullet in bullet_list:
            bullet.draw_bullet()
        for American_bullet in American_bullet_list:
            American_bullet.draw_bullet()
    # Restart function which will reset all player attributes in the class.
    def restart(): 
            bullet_list.clear() 
            American_bullet_list.clear() 
            pygame.time.delay(1000)
            American_soldier.death = False
            Canadian_soldier.death = False 
            American_soldier.health = 100 
            Canadian_soldier.health = 100  
            Canadian_soldier.x = 200 
            Canadian_soldier.y = 375 
            American_soldier.x = 900 
            American_soldier.y = 375
    game_over = font.render("GAME OVER", True, (255,255,255))
    red_team_won = font.render("CANADIAN WINS", True, (255,0,0))
    blue_team_won = font.render("AMERICAN WINS", True, (0,0,255))
    text_restart_shooter = font.render("RESTART", True, (0,0,0))
    text_main_menu_shooter = font.render("MAIN MENU", True, (0,0,0))
    if (American_soldier.death == True or Canadian_soldier.death == True) and start_game == True:
        death_screen = True 
        win.fill((0,0,0)) 
        win.blit(game_over, (505,258))
        if American_soldier.death == True: 
            win.blit(red_team_won, (462, 425))
        else: 
            win.blit(blue_team_won, (462,425))
        restart_shooter.draw_button()
        main_menu_shooter.draw_button() 
        win.blit(text_restart_shooter, (545, 575))
        win.blit(text_main_menu_shooter, (525, 695))
    # Level 2 - In this game the red square can kill the blue square instantly and the goal of the blue square is to survive for 60 seconds. 
    if start_game_2 == True: 
        clock.tick(60)
        move_1()
        move_2() 
        shoot() 
        try: 
            for bullet in bullet_list:
                if bullet.y - bullet.radius < American_soldier.hitbox[1] + American_soldier.hitbox[3] and bullet.y + bullet.radius > American_soldier.hitbox[1]:
                    if bullet.x + bullet.radius > American_soldier.hitbox[0] and bullet.x - bullet.radius < American_soldier.hitbox[0] + American_soldier.hitbox[2]:
                        American_soldier.hit_2()
                        bullet_list.pop(bullet_list.index(bullet))

                if bullet.x < 1200 and bullet.x > 0:
                    bullet.x += 40
                else:
                    bullet_list.pop(bullet_list.index(bullet))
        except: 
            print("ERROR")
        time_counter_text = font.render(str(time_counter), True, (255,0,0))
        win.fill((255,255,255))
        # Draw 
        Canadian_soldier.draw_soldier()
        American_soldier.draw_soldier()
        American_soldier.barrier() 
        Canadian_soldier.barrier() 
        Canadian_soldier.draw_health_bar()
        American_soldier.draw_health_bar()  
        for bullet in bullet_list:
            bullet.draw_bullet() 
        pygame.draw.rect(win, (0,0,0), (500, 850, 700,50))
        pygame.draw.rect(win,(0,0,0), (500,0, 700, 50))
        pygame.draw.rect(win,(0,0,0), (0,0, 700, 50))
        win.blit(time_counter_text, (1000,10))
    if (American_soldier.death == True or time_counter == 0) and start_game_2 == True: 
        win.fill((0,0,0))
        win.blit(game_over, (505,258))
        if American_soldier.death == True: 
            win.blit(red_team_won, (462, 425))
            time_counter = 60 
        if time_counter == 0: 
            win.blit(blue_team_won, (462,425))
        main_menu_survival.draw_button()
        restart_survival.draw_button()
        win.blit(text_restart_shooter, (545, 575))
        win.blit(text_main_menu_shooter, (525, 695))
    # Level 3 - Single player game where the objective of the player is to kill as many blue squares as possible to improve their score. 
    # If a blue square reaches the end of the screen then the red player will lose health and more blue squares will spawn 
    if start_game_3 == True: 
        move_1()
        move_2() 
        shoot() 
        create_enemy(num_enemies) 
        try: 
            for bullet in bullet_list:
                for enemy in enemy_list: 
                    if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]: 
                        if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]: 
                            print("HIT ENEMY")
                            enemy_list.pop(enemy_list.index(enemy))
                            bullet_list.pop(bullet_list.index(bullet))
                            single_player_score += 100 

                if bullet.x < 1200 and bullet.x > 0:
                    bullet.x += 30
                else:
                    bullet_list.pop(bullet_list.index(bullet))
        except: 
            print("ERROR")
        for enemy in enemy_list: 
            if enemy.x < 1200 and enemy.x > 0: 
                enemy.x -= 18
            else: 
                enemy_list.pop(enemy_list.index(enemy))
                num_enemies += 1 
                Canadian_soldier.hit() 
        num_enemies_display = font.render(f"Enemies: {str(num_enemies)}", True, (255,255,255))
        score = font.render(f"Score: {str(single_player_score)}", True, (255,255,255))
        score_text = font.render(f"SCORE: {str(single_player_score)}", True, (255,255,255))
        high_score_text = font.render(f"HIGH SCORE: {str(high_score)}", True, (255,255,255))
        survival_time_text = font.render(f"TIME SURVIVED: {str(survival_timer)} Seconds", True, (255,255,255))
        win.fill((255,255,255))
        # Draw 
        Canadian_soldier.draw_soldier()
        Canadian_soldier.barrier() 
        Canadian_soldier.draw_health_bar()
        for enemy in enemy_list: 
            enemy.draw_enemy() 
        for bullet in bullet_list:
            bullet.draw_bullet() 
        pygame.draw.rect(win,(0,0,0), (500,0, 700, 50))
        win.blit(num_enemies_display, (700, 20))
        win.blit(score, (900, 20))
    if Canadian_soldier.death == True and start_game_3 == True: 
        start_timer = False 
        win.fill((0,0,0))
        if single_player_score > high_score: 
            high_score = single_player_score 
            with open("score.txt", "w") as file: 
                file.write(str(high_score))
        win.blit(game_over, (505,258))
        restart_single_player.draw_button()
        main_menu_single_player.draw_button() 
        win.blit(text_restart_shooter, (545, 575))
        win.blit(text_main_menu_shooter, (525, 695))
        win.blit(score_text, (505, 330))
        win.blit(high_score_text, (450, 365))
        win.blit(survival_time_text,(450, 400))
    pygame.display.update()
pygame.quit()
