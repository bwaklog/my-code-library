import pygame
import sys
import random

pygame.init()
fps = 30
fpsclock = pygame.time.Clock()
sur_obj = pygame.display.set_mode((210, 210))
pygame.display.set_caption("Keyboard Input")
white = (115, 75, 100)
Xp1 = 110
Yp1 = 100
Xp2 = 90
Yp2 = 100
x = random.choice(range(10, 190))
y = random.choice(range(10, 190))
step = 4

while True:
    sur_obj.fill(white)

    # Random box generator

    pygame.draw.circle(surface=sur_obj, color=(5, 15, 100), center=(x, y), radius=5)

    pygame.draw.rect(sur_obj, (255, 0, 0), (Xp1, Yp1, 10, 10))
    pygame.draw.rect(sur_obj, (0, 255, 0), (Xp2, Yp2, 10, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key_input = pygame.key.get_pressed()
    # Player 1
    if key_input[pygame.K_LEFT]:
        Xp1 -= step
    if key_input[pygame.K_RIGHT]:
        Xp1 += step
    if key_input[pygame.K_UP]:
        Yp1 -= step
    if key_input[pygame.K_DOWN]:
        Yp1 += step

    # Player 2
    if key_input[pygame.K_a]:
        Xp2 -= step
    if key_input[pygame.K_d]:
        Xp2 += step
    if key_input[pygame.K_w]:
        Yp2 -= step
    if key_input[pygame.K_s]:
        Yp2 += step

    # Wall bounce for p1
    if Xp1 < 0:
        Xp1 = 0
    elif Xp1 >= 200:
        Xp1 = 200
    if Yp1 < 0:
        Yp1 = 0
    elif Yp1 >= 200:
        Yp1 = 200
    # Wall bounce for p2
    if Xp2 < 0:
        Xp2 = 0
    elif Xp2 >= 200:
        Xp2 = 200
    if Yp2 < 0:
        Yp2 = 0
    elif Yp2 >= 200:
        Yp2 = 200



    # check for colision for p1
    if (Xp1>x-10 and Xp1 < x+10) and (Yp1 >y-10 and Yp1 < y+10):
        x = random.choice(range(10, 190))
        y = random.choice(range(10, 190))
    #check for collision for p2
    if (Xp2>x-10 and Xp2 < x+10) and (Yp2 >y-10 and Yp2 < y+10):
        x = random.choice(range(10, 190))
        y = random.choice(range(10, 190))

    print('P1 :', Xp1, Yp1, 'P2 :', Xp2, Yp2)
    pygame.display.update()
    fpsclock.tick(fps)
