import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра тир")
icon=pygame.image.load("img/shooting.png")
pygame.display.set_icon(icon)
target_img=pygame.image.load("img/target.png")
target_width=80
target_height=80
target_x=random.randint(0, SCREEN_WIDTH-target_width)
target_y=random.randint(0, SCREEN_HEIGHT-target_height)
color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
running=True
res=0;
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x > target_x and mouse_x < target_x + target_width and mouse_y > target_y and mouse_y < target_y + target_height:
                target_x=random.randint(0, SCREEN_WIDTH-target_width)
                target_y=random.randint(0, SCREEN_HEIGHT-target_height)
                color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                res+=1
                pygame.display.set_caption(f"Игра тир. {res} попаданий")
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()
pygame.quit()