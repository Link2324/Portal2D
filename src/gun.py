import pygame as pg
import pygame.math

from entity import Entity


class Gun(Entity):
    def __init__(self, image, level):
        super().__init__(image, level)
        self.rotated_surf = self.image
        self.rotated_rect = self.rect

    def update(self, x, y, angle):
        self._rotate(angle, (x, y), pygame.math.Vector2(self.rect.w / 2, 0))

    def _rotate(self, angle, pivot, offset):
        """Rotate the surface around the pivot point.

        Args:
            angle (float): Rotate by this angle.
            pivot (tuple, list, pygame.math.Vector2): The pivot point.
            offset (pygame.math.Vector2): This vector is added to the pivot.
        """
        self.rotated_surf = pg.transform.rotozoom(self.image, -angle, 1)  # Rotate the image.
        rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
        # Add the offset vector to the center/pivot point to shift the rect.
        self.rotated_rect = self.rotated_surf.get_rect(center=pivot + rotated_offset)
