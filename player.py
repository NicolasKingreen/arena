from math import sqrt
from pygame import transform, mouse, image

from sprite import AnimatedSprite


class Player(AnimatedSprite):

    def __init__(self, world):
        self.world = world
        player_images = []
        player_sprite_sheet = image.load("data/img/ranger.png").convert_alpha()
        player_images.append(player_sprite_sheet.subsurface((0, 0, 10, 12)))
        player_images.append(player_sprite_sheet.subsurface((10, 0, 10, 12)))
        super().__init__(player_images)
        self.movement_direction = [0, 0]
        self.speed = 0.35
        self.scale(10)
        self.rect.center = self.world.game_instance.settings.screen_center

    def update(self, dt):
        super().update(dt)

        # TODO: Flip sprite relative to x direction
        # self.is_looking_right = (True, False)[self.movement_direction[0] > 0]

        mouse_x = mouse.get_pos()[0]
        if mouse_x > self.rect.centerx and not self.is_looking_right:
            self.image = transform.flip(self.image, True, False)
            self.is_looking_right = True
        elif mouse_x < self.rect.centerx and self.is_looking_right:
            self.image = transform.flip(self.image, True, False)
            self.is_looking_right = False

        movement_direction_length = sqrt(self.movement_direction[0] ** 2 + self.movement_direction[1] ** 2)
        if movement_direction_length:
            normalised_movement_direction = [(x/(movement_direction_length)) for x in self.movement_direction]
            dx = normalised_movement_direction[0] * self.speed * dt
            dy = normalised_movement_direction[1] * self.speed * dt
            self.rect.x += dx
            self.rect.y += dy
            # print(f"{tuple([round(x, 1) for x in normalised_movement_direction])} v ({round(dx, 1)}, {round(dy, 1)})\r", end="")

