import sys

import pygame
from pygame.math import *
from map import Map

# A game entity is an object that interacts with the game
# and responds to player input or other entities


class Entity:
    """Class for entity"""

    def __init__(self, image, level: Map):

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
        self.old_position = Vector2()
        self.pos = Vector2(64 * 3, 64 * 3)
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.vel = Vector2((8, 8))
        self.force = Vector2((0, 0))

        self.OnGround = False
        self.wasGround = False
        self.pushesRightWall = False
        self.pushedRightWall = False
        self.pushesLeftWall = False
        self.pushedLeftWall = False
        self.AtCeiling = False
        self.WasCeiling = False

    def blit_me(self, screen):
        screen.blit(self.image, self.rect)

    def collision(self):
        """Method for checking entity collision with map"""
        left = int((self.rect.x + self.map.x) / self.map.tile_size)
        up = int(self.rect.y / self.map.tile_size)
        right = int((self.rect.right + self.map.x) / self.map.tile_size) + 1
        down = int(self.rect.bottom / self.map.tile_size) + 1

        rect_list = []
        for m in range(left, right + 1):
            for n in range(up, down + 1):
                try:
                    tile_id = self.map.level[n][m] - 1
                except IndexError:
                    continue

                if tile_id == -1:
                    continue

                tile = self.map.tile[tile_id]
                if not tile.collision:
                    continue

                rect = pygame.Rect(m * self.map.tile_size - self.map.x, n * self.map.tile_size,
                                   self.map.tile_size, self.map.tile_size)
                if self.rect.colliderect(rect):
                    rect_list.append(rect)

        return rect_list


class Player(Entity):
    """Class for player """

    def __init__(self, image, level):
        super().__init__(image, level)

        # Flags for player movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.exit = False

    def update(self):
        # Old Position
        self.old_position.x = self.pos.x
        self.old_position.y = self.pos.y

        self.wasGround = self.OnGround
        self.pushedRightWall = self.pushesRightWall
        self.pushedLeftWall = self.pushesLeftWall
        self.WasCeiling = self.AtCeiling

        if self.moving_right:
            self.pos.x += self.vel.x

        if self.moving_left:
            self.pos.x -= self.vel.x

        if self.moving_up:
            self.pos.y -= self.vel.y

        if self.moving_down:
            self.pos.y += self.vel.y

        if self.exit:
            sys.exit(0)

        self.map.x = self.pos.x - 640 + self.vel.x
        if self.map.x < 0:
            self.map.x = 0

        if self.map.x > self.map.width * self.map.tile_size - 1280:
            self.map.x = self.map.width * self.map.tile_size - 1280

        pygame.mouse.get_pos()

        self.rect.x = self.pos.x - self.map.x
        self.rect.y = self.pos.y

        self.OnGround = False
        self.pushesRightWall = False
        self.pushesLeftWall = False
        self.AtCeiling = False

        rect = self.collision()

        if len(rect) != 0:
            self.pos.x = self.old_position.x
            self.pos.y = self.old_position.y
