import pygame
import sys
from map import Map
from map_list import *


class Portal2D:
    """class for game loop"""

    def __init__(self):
        # Initialise pygame
        pygame.init()

        # Create an object to help track time
        self.clock = pygame.time.Clock()

        # pygame window size
        self.resolution = (1280, 720)

        # Initialize a window for display
        self.screen = pygame.display.set_mode(self.resolution)

        # Instance of Map class
        self.map = Map(map00, "res/tiles.png", tile_count=4, tile_size=64)

        # Name of window
        pygame.display.set_caption("Portal2D")

    def run_game(self):
        """Game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Drawing map
            self.map.draw_map(self.screen)
            pygame.display.update()

            # Fps limit
            self.clock.tick(60)


if __name__ == '__main__':
    portal2D = Portal2D()
    portal2D.run_game()