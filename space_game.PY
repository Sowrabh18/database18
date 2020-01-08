import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("space.jpg")
pygame.display.set_caption("SPACE DESTROYER")
i = pygame.image.load('alien.png')
pygame.display.set_icon(i)
playerimg = pygame.image.load("airplane.png")
missileimg = pygame.image.load("missile.png")
mixer.music.load("background.wav")
mixer.music.play(-1)


playerx = 400
playery = 530
player_x = 0
player_y = 0

enemyx =[]
enemyy =[]
enemy_x =[]
enemy_y =[]
enemyimg=[]
num=3

for i in range (num):
    enemyx.append(random.randint(0, 736))
    enemyy.append(random.randint(70, 160))
    enemy_x.append(-3)
    enemy_y.append(+3)
    enemyimg.append(pygame.image.load("tiefighter.png"))

missilex = 0
missiley = 560
missile_x = 0
missile_y = 0
missile_state = ("Ready")


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(a,b,i):
    screen.blit(enemyimg[i],(a, b))


def fire_missile(a, b):
    global missile_state
    missile_state = ("fire")
    screen.blit(missileimg, (a+16, b+10))


def is_collision(enemyx,enemyy, missilex, missiley):
    dist = math.sqrt(math.pow(enemyx - missilex, 2)) + math.sqrt(math.pow(enemyy - missiley, 2))
    if dist < 27:
        return True
    else:
        False


run = True

while run:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x = -5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x = +5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x = -5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                if missile_state == ("Ready"):
                    missile_sound = mixer.Sound("laser.wav")
                    missile_sound.play()
                    missilex = playerx
                    fire_missile(missilex, missiley)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x = +0
    playerx += player_x

    missilex += missile_x

    player(playerx, playery)



    if missile_state is ("fire"):
        fire_missile(missilex, missiley)
        missile_y = +10
        missilex += missile_x
        missiley -= missile_y


    if playerx <= 0:
        playerx = 0
    elif playerx >= 740:
        playerx = 740
    if playery <= 530:
        player_y = 530

    for i in range(num):

        if enemyx[i] <= 0:
            enemy_x[i] = +3
        elif enemyx[i] >= 740:
            enemy_x[i] = -3
        if enemyy[i] <= 30:
            enemy_y[i] = +3
        elif enemyy[i] >= 160:
            enemy_y[i] = -3
        collision = is_collision(enemyx[i], enemyy[i], missilex, missiley)
        if collision:
            explosion_state = mixer.Sound("explosion.wav")
            explosion_state.play()
            missiley = 480
            missile_state = ("Ready")
            enemyx[i] = random.randint(0, 736)
            enemyy[i] = random.randint(70, 160)
        enemyx[i]+=enemy_x[i]
        enemyy[i]+=enemy_y[i]
        enemy(enemyx[i], enemyy[i], i)

    if missiley <= 0:
        missiley = 530
        missile_state = ("Ready")
    pygame.display.update()
