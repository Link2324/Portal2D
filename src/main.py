import os
import sys

from entity import *
from map import Map
from map_list import *


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

        # Path for res
        self.path = os.path.dirname(__file__).split("\\src")[0]

        # Name of window
        pygame.display.set_caption("Portal2D")

        # Instance of Map class
        self.map = Map(map02, f"{self.path}/res/tiles.png", tile_count=4, tile_size=64)

        # Draws map on surface
        self.map.draw_map()

        # Instance of player
        self.player = Player(f"{self.path}/res/player1.png", self.map)

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
        self.player.moving_up, self.player.moving_down, self.player.moving_left, self.player.moving_right = \
            [pressed[key] for key in (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)]

    def __update(self):
        self.player.update()

    def __draw(self):
        self.screen.blit(self.map.surf, (-self.map.x, self.map.y))
        self.player.blit_me(self.screen)


if __name__ == '__main__':
    portal2D = Portal2D()
    portal2D.run_game()
