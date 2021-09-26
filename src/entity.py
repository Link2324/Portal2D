import pygame
from pygame.math import *
from map import Map


# A game entity is an object that interacts with the game
# and responds to player input or other entities


class Entity:
    """Class for entity"""

    def __init__(self, image, level: Map, spawn_point=(0, 0)):

        # Load entity image
        self.image = pygame.image.load(image)

        # Instance of Map which will used for collision
        self.map = level

        # Scale entity image
        self.height = int((64 / self.image.get_width()) * self.image.get_height())
        self.image = pygame.transform.scale(self.image, (64, self.height))

        # Rect for scaled entity image
        self.rect = self.image.get_rect()

        # Entity property
        self.mass = 10

        self.pos = Vector2(spawn_point[0], spawn_point[1])
        self.rect.x = spawn_point[0]
        self.rect.y = spawn_point[1]
        self.vel = Vector2((4, 4))
        self.force = Vector2((0, 0))

    def blit_me(self, screen):
        screen.blit(self.image, self.rect)

    def collision(self):
        """Method for checking entity collision with map"""
        left = int(self.rect.x / self.map.tile_size)
        up = int(self.rect.y / self.map.tile_size)
        right = int(self.rect.right / self.map.tile_size) + 1
        down = int(self.rect.bottom / self.map.tile_size) + 1

        for m in range(left, right + 1):
            for n in range(up, down + 1):
                tile_id = self.map.level[n][m] - 1

                if tile_id == -1:
                    continue

                tile = self.map.tile[tile_id]
                if not tile.collision:
                    continue

                rect = pygame.Rect(m * self.map.tile_size, n * self.map.tile_size,
                                   self.map.tile_size, self.map.tile_size)
                if self.rect.colliderect(rect):
                    return True
        return False


class Player(Entity):
    """Class for player """

    def __init__(self, image, level, spawn_point=(0, 0)):
        super().__init__(image, level, spawn_point)

        # Flags for player movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # Old Position
        self.pos.x = self.rect.x
        self.pos.y = self.rect.y

        if self.moving_right:
            self.rect.x += self.vel.x

        if self.moving_left:
            self.rect.x -= self.vel.x

        if self.moving_up:
            self.rect.y -= self.vel.y

        if self.moving_down:
            self.rect.y += self.vel.y

        if self.collision():
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
