import pygame


class Map:
    """class to manage map related operation"""

    def __init__(self, level, tile_sprite, tile_count, tile_size=64):

        # level is 2D list to store map data
        self.level = level

        # width and height store map height and width in number of tiles
        self.width = len(level[0])
        self.height = len(level)

        # sprite for tiles
        self.tile_sprite = pygame.image.load(tile_sprite)

        # height and width of tile
        self.tile_size = tile_size

        # total no. of tiles
        self.tile_count = tile_count

        # List for storing tiles
        self.tile = []

        # Save Tile object in tile list
        self.__load_tiles()

    def draw_map(self, screen):
        """method for drawing map on screen"""

        for j in range(0, self.height):
            for i in range(0, self.width):
                if self.level[j][i] == 1:
                    screen.blit(self.tile[0].tile_image, (i * self.tile_size, j * self.tile_size))
                elif self.level[j][i] == 2:
                    screen.blit(self.tile[1].tile_image, (i * self.tile_size, j * self.tile_size))
                elif self.level[j][i] == 3:
                    screen.blit(self.tile[2].tile_image, (i * self.tile_size, j * self.tile_size))

    def __load_tiles(self):
        """insert Tile in tile list """
        columns = int(self.tile_sprite.get_width() / self.tile_size)
        rows = int(self.tile_count / columns)

        index = 0
        for i in range(0, rows):
            for j in range(0, columns):

                x = self.tile_size * j
                y = self.tile_size * i

                tile_rect = pygame.Rect((x, y), (self.tile_size, self.tile_size))
                tile_image = self.tile_sprite.subsurface(tile_rect)

                if index == 0:
                    tile = Tile(tile_image, portal=True, collision=False)
                elif index == 1:
                    tile = Tile(tile_image, portal=False, collision=False)
                else:
                    tile = Tile(tile_image)

                self.tile.insert(index, tile)
                index += 1


class Tile:
    """class for tiles"""

    def __init__(self, image, portal=False, collision=False):
        self.tile_image = image

        # Flag for whether portal will work on tile or not
        self.portal = portal

        # Flag for collision check
        self.collision = collision