from pygame.sprite import Group
from pygame import image

from player import Player


class World:

    def __init__(self, game_instance):
        self.game_instance = game_instance
        self.player = Player(self)

        # Arrows
        self.flying_arrows = Group()

        self.enemies = Group()

    def update(self, dt):
        self.player.update(dt)
        self.flying_arrows.update(dt, self.game_instance.screen)

    def draw(self, surface):
        self.player.draw(surface)
        self.flying_arrows.draw(surface)