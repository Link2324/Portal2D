import os

from entity import *
from gun import Gun
from map import Map
from map_list import *
import math


class Portal2D:
    """class for game"""

    def __init__(self):
        # Initialise pygame
        pygame.init()

        # Create an object to help track time
        self.clock = pygame.time.Clock()

        self.MS_PER_UPDATE = 1000 / 60

        # pygame window size
        self.resolution = (1280, 720)

        # Initialize a window for display
        self.screen = pygame.display.set_mode(self.resolution)

        pygame.mouse.set_visible(False)

        # Path for res
        self.path = os.path.dirname(__file__).split("\\src")[0]

        # Name of window
        pygame.display.set_caption("Portal2D")

        # Instance of Map class
        self.map = Map(map02, f"{self.path}/res/tiles.png", tile_count=4, tile_size=64)

        # Draws map on surface
        self.map.draw_map()

        # variable for mouse cursor position
        self.pos = pygame.mouse.get_pos()

        # Image for mouse cursor
        self.cursor = pygame.image.load(f"{self.path}/res/cursor.png")
        self.cursor_rect = self.cursor.get_rect()

        self.gun = Gun(f"{self.path}/res/gun.png", self.map)

        # Instance of player
        self.player = Player(f"{self.path}/res/player2.png", self.map)

        # Flags for cursor position with respect to player
        self.facing_right = True
        self.wasFacing_right = True

    def run_game(self):
        """Game loop"""
        self.clock.tick()
        lag = 0
        while True:
            elapsed = self.clock.tick()
            lag += elapsed
            self.__input()
            while lag > self.MS_PER_UPDATE:
                self.__update()
                lag -= self.MS_PER_UPDATE
            self.__draw()

            # Clears screen
            pygame.display.flip()

    def __input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressed = pygame.key.get_pressed()
        (
            self.player.moving_up,
            self.player.moving_down,
            self.player.moving_left,
            self.player.moving_right,
            self.player.exit,
        ) = [pressed[key] for key in (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_q)]

        self.pos = pygame.mouse.get_pos()

    def __update(self):
        self.wasFacing_right = self.facing_right

        self.player.update()
        self.cursor_rect.center = self.pos
        x = self.player.rect.x + self.player.rect.w / 2
        y = self.player.rect.y + self.player.rect.h / 3

        temp = 0
        if self.pos[0] <= x:
            temp = -180
            self.facing_right = False
        else:
            self.facing_right = True

        if self.wasFacing_right:
            if not self.facing_right:
                self.player.image = pygame.transform.flip(self.player.image, True, False)
        else:
            if self.facing_right:
                self.player.image = pygame.transform.flip(self.player.image, True, False)

        try:
            angle = temp + int(math.degrees(math.atan((self.pos[1] - y) / (self.pos[0] - x))))
        except ZeroDivisionError:
            if y - self.pos[1] > 0:
                angle = - 90
            else:
                angle = 90
        self.gun.update(x, y, angle)

    def __draw(self): 
        self.screen.blit(self.map.surf, (-self.map.x, self.map.y))
        self.player.blit_me(self.screen)
        self.screen.blit(self.gun.rotated_surf, self.gun.rotated_rect)
        self.screen.blit(self.cursor, self.cursor_rect)


if __name__ == "__main__":
    portal2D = Portal2D()
    portal2D.run_game()
