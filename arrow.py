from math import acos, sqrt, atan
import pygame as pg
from sprite import Sprite


class Arrow(Sprite):

    def __init__(self, start_position, clicked_position):
        arrow_image = pg.image.load("data/img/arrow.png").convert_alpha()
        self.movement_direction = (clicked_position[0] - start_position[0], clicked_position[1] - start_position[1])
        angle = acos((1 * clicked_position[0])/(sqrt(clicked_position[0] ** 2 + clicked_position[1] ** 2)))
        angle *= 180 / 3.14
        print(angle)
        movement_direction_length = sqrt(self.movement_direction[0] ** 2 + self.movement_direction[1] ** 2)
        self.movement_direction = [(x/(movement_direction_length)) for x in self.movement_direction]
        arrow_image = pg.transform.scale(arrow_image, (arrow_image.get_width() * 10, arrow_image.get_height() * 10))
        arrow_image = pg.transform.rotate(arrow_image, angle)
        super().__init__(arrow_image)
        self.rect.center = start_position
        self.speed = 0.6

    def update(self, dt, surface):
        if self.rect.colliderect(surface.get_rect()):
            dx = self.movement_direction[0] * self.speed * dt
            dy = self.movement_direction[1] * self.speed * dt
            self.rect.x += dx
            self.rect.y += dy
        else:
            self.kill()