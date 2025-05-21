import pygame
import game_class
import os
import math
import time
from package.pyvidplayer import Video


pygame.init()

WIDTH, HEIGHT = 1200, 900
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heaven and Hell")

Clock = pygame.time.Clock()

# load images
BasicImagePath = os.path.abspath('.') + '/' + "source/image/"
PlayerCharacterImage = pygame.image.load(BasicImagePath + "heart.png").convert_alpha()
PlayerCharacterImage = pygame.transform.scale(PlayerCharacterImage, (PlayerCharacterImage.get_rect().size[0] / 4.5, PlayerCharacterImage.get_rect().size[1] / 4.5))
EnemyCharacterImage = pygame.image.load(BasicImagePath + "angel.png").convert_alpha()
EnemyCharacterImage = pygame.transform.scale(EnemyCharacterImage, (EnemyCharacterImage.get_rect().size[0] / 2, EnemyCharacterImage.get_rect().size[1] / 2))
BorderImage = pygame.image.load(BasicImagePath + "border.png").convert_alpha()
BorderImage = pygame.transform.scale(BorderImage, (BorderImage.get_rect().size[0] / 3, BorderImage.get_rect().size[1] / 3))

# load video
BasicVideoPath = os.path.abspath('.') + '/' + "source/video/"
BackgroundVideo = Video(BasicVideoPath + "HAH.mov")
BackgroundVideo.set_size((WIDTH, HEIGHT))

# create instances
PlayerCharacter = game_class.Player(speed=4, image=PlayerCharacterImage)
PlayerCharacter.rect.x = WIDTH / 2 - PlayerCharacter.width / 2
PlayerCharacter.rect.y = HEIGHT / 1.5
EnemyCharacter = game_class.Enemy(image=EnemyCharacterImage)
EnemyCharacter.rect.x = WIDTH / 2 - EnemyCharacter.width / 2
Border = game_class.Border(image=BorderImage)
Border.rect.x = WIDTH / 2 - Border.width / 2
Border.rect.y = HEIGHT / 2

# begin play
BackgroundVideo.set_volume(0.5)

# game loop
running = True
while running:
    # system loop
    Clock.tick(120) # set frame
    DeltaTime = pygame.time.get_ticks() / 1000

    # update
    PlayerCharacter.movement_update(slippery = 0.8)
    EnemyCharacter.rect.y = HEIGHT / 7 - math.sin(DeltaTime * 2) * 30


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and PlayerCharacter.rect.left > Border.rect.left - 20:
        PlayerCharacter.move("left")
    if keys[pygame.K_d] and PlayerCharacter.rect.right < Border.rect.right + 20:
        PlayerCharacter.move("right")
    if keys[pygame.K_w] and PlayerCharacter.rect.top > Border.rect.top:        PlayerCharacter.move("up")
    if keys[pygame.K_s] and PlayerCharacter.rect.bottom < Border.rect.bottom:
        PlayerCharacter.move("down")
    if keys[pygame.K_q]:
        pygame.quit()

    # Update display
    pygame.display.flip()
    Screen.fill((0, 0, 0))
    BackgroundVideo.draw(Screen, (0, 0))
    Screen.blit(PlayerCharacter.image, (PlayerCharacter.rect.x, PlayerCharacter.rect.y))
    Screen.blit(EnemyCharacter.image, (EnemyCharacter.rect.x, EnemyCharacter.rect.y))
    Screen.blit(Border.image, (Border.rect.x, Border.rect.y))
    pygame.display.update()

pygame.quit()