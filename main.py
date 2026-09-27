import pygame
import sys
import random

pygame.init()  # init pygame

# ---------- VARIABLES ----------
SCREEN_WIDTH = 576
SCREEN_HEIGHT = 840
FLOOR_Y = 770
floor_x = 0
gravity = 0.25  # fall speed
angel_movement = 0
obstacle_list = []
score = 0
high_score = 0
can_score = True  # flag to allow scoring

game_start = True
game_active = False
game_paused = False

angel_frame_index = 0  # animation index

# ---------- EVENTS ----------
CREATE_OBSTACLE = pygame.USEREVENT
CREATE_WING_FLAP = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_WING_FLAP, 100)  # flap animation timer
pygame.time.set_timer(CREATE_OBSTACLE, 1200)  # obstacle spawn timer
pygame.display.set_caption("Harvard Angels")  

# ---------- SOUNDS ----------
point_sound = pygame.mixer.Sound('assets/sound/smb_stomp.wav')
death_sound = pygame.mixer.Sound('assets/sound/smb_mariodie.wav')
pygame.mixer.music.load('assets/sound/background.mp3')
pygame.mixer.music.set_volume(0.8)  # lower bg music

# ---------- IMAGES ----------
background_img = pygame.transform.scale2x(pygame.image.load('assets/img/bg.png'))
floor_img = pygame.transform.scale2x(pygame.image.load('assets/img/floor.png'))

angel_img_down = pygame.transform.scale2x(pygame.image.load('assets/img/angel_down_flap.png'))
angel_img_mid = pygame.transform.scale2x(pygame.image.load('assets/img/angel_mid_flap.png'))
angel_img_up = pygame.transform.scale2x(pygame.image.load('assets/img/angel_up_flap.png'))
angel_images = [angel_img_down, angel_img_mid, angel_img_up]
current_angel_img = angel_images[angel_frame_index]

icon = pygame.image.load("assets/img/angel_up_flap.png")  
pygame.display.set_icon(icon)

obstacle_img = pygame.transform.scale2x(pygame.image.load('assets/img/pipe_red.png'))
game_over_img = pygame.transform.scale2x(pygame.image.load('assets/img/message.png'))
game_over_rect = game_over_img.get_rect(center=(288, 420))

game_font = pygame.font.Font('assets/font/Flappy.TTF', 40)

# ---------- FUNCTIONS ----------
def generate_obstacles():
    height = random.randrange(400, 700)  # random pipe height
    top_obstacle = obstacle_img.get_rect(midbottom=(700, height - 300))
    bottom_obstacle = obstacle_img.get_rect(midtop=(700, height))
    return top_obstacle, bottom_obstacle  # return tuple

def move_obstacles(obstacles):
    for obs in obstacles:
        obs.centerx -= 5  # move left
    return [obs for obs in obstacles if obs.right > -50]  # keep on screen

def draw_obstacles(obstacles):
    for obs in obstacles:
        if obs.bottom >= SCREEN_HEIGHT:  # bottom pipe
            main_screen.blit(obstacle_img, obs)
        else:  # top pipe (flipped)
            main_screen.blit(pygame.transform.flip(obstacle_img, False, True), obs)

def check_collision(obstacles):
    global can_score
    for obs in obstacles:
        if angel_rect.colliderect(obs):  # hit pipe
            death_sound.play()
            can_score = True
            return False
    if angel_rect.top <= -50 or angel_rect.bottom >= FLOOR_Y:  # hit ceiling/floor
        death_sound.play()
        can_score = True
        return False
    return True

def angel_animation():
    img = angel_images[angel_frame_index]  # pick frame
    rect = img.get_rect(center=(100, angel_rect.centery))
    return img, rect

def display_score(status):
    if status == 'active':
        text = game_font.render(str(score), True, (255, 255, 255))
        main_screen.blit(text, text.get_rect(center=(288, 100)))
    elif status == 'game_over':
        main_screen.blit(game_over_img, game_over_rect)
        text1 = game_font.render(f'Score: {score}', True, (255, 255, 255))
        main_screen.blit(text1, text1.get_rect(center=(288, 150)))
        text2 = game_font.render(f'HighScore: {high_score}', True, (255, 255, 255))
        main_screen.blit(text2, text2.get_rect(center=(288, 100)))
        restart_text = game_font.render("Press  R  to  Restart", True, (252, 100, 0))
        main_screen.blit(restart_text, restart_text.get_rect(center=(288, 750)))
    elif status == 'paused':
        paused_text = game_font.render("Game Paused", True, (255, 0, 0))
        main_screen.blit(paused_text, paused_text.get_rect(center=(288, 200)))
        resume_text = game_font.render("Press P to Resume", True, (255, 255, 0))
        main_screen.blit(resume_text, resume_text.get_rect(center=(288, 260)))

def update_score():
    global score, high_score, can_score
    if obstacle_list:
        for obs in obstacle_list:
            # score when passing bottom pipe
            if 95 < obs.centerx < 105 and can_score and obs.bottom >= SCREEN_HEIGHT:
                point_sound.play()
                score += 1
                can_score = False
            # reset scoring flag
            if obs.centerx < 0 and obs.bottom >= SCREEN_HEIGHT:
                can_score = True
    if score > high_score:
        high_score = score  # update high score

# ---------- INITIAL SETUP ----------
angel_rect = current_angel_img.get_rect(center=(100, 420))
main_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# ---------- GAME LOOP ----------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_start:
                    game_active = True
                    game_start = False
                    pygame.mixer.music.play(-1)  # start bg music
                elif game_active and not game_paused:
                    angel_movement = 0
                    angel_movement -= 8  
            if event.key == pygame.K_r and not game_active:
                # restart game
                game_active = True
                obstacle_list.clear()
                angel_rect.center = (100, 420)
                angel_movement = 0
                score = 0
                pygame.mixer.music.play(-1)
            if event.key == pygame.K_p and game_active:
                game_paused = not game_paused
                if game_paused:
                    pygame.mixer.music.pause()  # pause music
                else:
                    pygame.mixer.music.unpause() # resume music

        if event.type == CREATE_OBSTACLE and game_active and not game_paused:
            obstacle_list.extend(generate_obstacles())  # spawn pipes
        if event.type == CREATE_WING_FLAP and game_active and not game_paused:
            angel_frame_index = (angel_frame_index + 1) % 3
            current_angel_img, angel_rect = angel_animation()  # animate wings

    # ---------- DRAWING ----------
    main_screen.blit(background_img, (0, 0))  # bg

    if game_start:
        start_text = game_font.render("Press SPACE to Start", True, (255, 255, 255))
        main_screen.blit(start_text, start_text.get_rect(center=(288, 420)))
    elif game_active:
        main_screen.blit(current_angel_img, angel_rect)  # draw angel

        if not game_paused:
            angel_movement += gravity  # apply gravity
            angel_rect.centery += angel_movement

            obstacle_list = move_obstacles(obstacle_list)  # move pipes
            draw_obstacles(obstacle_list)

            game_active = check_collision(obstacle_list)
            update_score()
            display_score('active')
        else:
            draw_obstacles(obstacle_list)  # frozen pipes
            display_score('paused')

    else:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        display_score('game_over')

    # ---------- DRAW FLOOR ----------
    floor_x -= 1  # scroll floor
    main_screen.blit(floor_img, (floor_x, FLOOR_Y))
    main_screen.blit(floor_img, (floor_x + SCREEN_WIDTH, FLOOR_Y))
    if floor_x <= -SCREEN_WIDTH:
        floor_x = 0  # reset floor

    pygame.display.update()
    clock.tick(60)  # 60 FPS