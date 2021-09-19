import pygame
from pygame.math import *


# A game entity is an object that interacts with the game
# and responds to player input or other entities


class Entity:
    """Class for entity"""

    def __init__(self, image, spawn_point=(0, 0)):

        # Load entity image
        self.image = pygame.image.load(image)

        # Scale entity image
        self.height = int((64 / self.image.get_width()) * self.image.get_height())
        self.image = pygame.transform.scale(self.image, (64, self.height))

        # Rect for scaled entity image
        self.rect = self.image.get_rect()

        # Entity property
        self.mass = 10
        self.pos = Vector2(spawn_point)
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

        self.vel = Vector2((4, 2))
        self.force = Vector2((0, 0))

    def blit_me(self, screen):
        screen.blit(self.image, self.rect)


class Player(Entity):
    """Class for player """

    def __init__(self, image, spawn_point=(0, 0)):
        super().__init__(image, spawn_point)

        # Flags for player movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right:
            self.pos.x += self.vel.x
            self.rect.x = self.pos.x

        if self.moving_left:
            self.pos.x -= self.vel.x
            self.rect.x = self.pos.x

        if self.moving_up:
            self.pos.y -= self.vel.y
            self.rect.y = self.pos.y

        if self.moving_down:
            self.pos.y += self.vel.y
            self.rect.y = self.pos.y
