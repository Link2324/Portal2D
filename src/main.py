import sys
import os

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

        # pygame window size
        self.resolution = (1280, 720)

        # Initialize a window for display
        self.screen = pygame.display.set_mode(self.resolution)

        # Path for res
        self.path = os.path.dirname(os.getcwd())

        # Name of window
        pygame.display.set_caption("Portal2D")

        # Instance of Map class
        self.map = Map(test_chamber, f"{self.path}/res/tiles.png", tile_count=4, tile_size=64)

        # Draws map on surface
        self.map.draw_map()

        # Instance of player
        self.player = Player(f"{self.path}/res/player1.png", spawn_point=(64, 64))

    def run_game(self):
        """Game loop"""
        while True:
            self.__input()
            self.__update()
            self.__draw()

            # Clears screen
            pygame.display.flip()

            # Fps limit
            self.clock.tick(60)

    def __input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressed = pygame.key.get_pressed()
        print(pressed)
        self.player.moving_up, self.player.moving_down, self.player.moving_left, self.player.moving_right = \
            [pressed[key] for key in (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)]

    def __update(self):
        self.player.update()

    def __draw(self):
        self.screen.blit(self.map.surf, (0, 0))
        self.player.blit_me(self.screen)


if __name__ == '__main__':
    portal2D = Portal2D()
    portal2D.run_game()
