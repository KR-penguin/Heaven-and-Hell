import pygame
import sys

class Player:
    def __init__(self, speed, image : pygame.Surface):
        self.width = image.get_rect().size[0]
        self.height = image.get_rect().size[1]
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.speed = speed
        self.image = image
        self.ToXpos = 0
        self.ToYpos = 0

    def move(self, direction : str):
        if direction == "left":
            self.ToXpos = -self.speed
        elif direction == "right":
            self.ToXpos = self.speed
        elif direction == "up":
            self.ToYpos = -self.speed
        elif direction == "down":
            self.ToYpos = self.speed
        else:
            print("error-001 : invalid direction")
            sys.exit(1)
    
    def movement_update(self, slippery):
        if self.ToXpos != 0:
            self.ToXpos *= slippery
        if self.ToYpos != 0:
            self.ToYpos *= slippery
        self.rect.x += self.ToXpos
        self.rect.y += self.ToYpos

class Border:
    def __init__(self, image : pygame.Surface):
        self.image = image
        self.width = image.get_rect().size[0]
        self.height = image.get_rect().size[1]
        self.rect = pygame.Rect(0, 0, self.width, self.height)

class Enemy:
    def __init__(self, image : pygame.Surface):
        self.width = image.get_rect().size[0]
        self.height = image.get_rect().size[1]
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.image = image