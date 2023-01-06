import sys
import pygame as pg

from settings import Settings
from sprite import Sprite, AnimatedSprite
from game_state import GameStateMachine
from arrow import Arrow
from world import World


class Arena:

    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.clock = pg.time.Clock()

        self.screen = pg.display.set_mode(self.settings.screen_size)
        pg.display.set_caption("Arena")

        self.is_round_started = False
        # pg.mouse.set_visible(False)

        pg.mixer.music.load("data/sound/music.mp3")

        self.font = pg.font.Font(None, 16)

        self.state_manager = GameStateMachine(self)
        self.state_manager.set_state("main_menu")


        # Cursor
        self.cursor_image = pg.image.load("data/img/cursor.png").convert_alpha()
        self.cursor_rect = self.cursor_image.get_rect()
        self.cursor_image = pg.transform.scale(self.cursor_image, (self.cursor_rect.width * 5, self.cursor_rect.height * 5))
        self.cursor_rect = self.cursor_image.get_rect()

        # Background image
        bg_image = pg.image.load("data/img/bg.png").convert_alpha()
        self.background = Sprite(bg_image)
        self.background.scale(10)

        # Game title
        title_images = []
        title_images.append(pg.image.load("data/img/outrange_1.png").convert_alpha())
        title_images.append(pg.image.load("data/img/outrange_2.png").convert_alpha())
        self.title = AnimatedSprite(title_images)
        self.title.scale(10)
        self.title.rect.center = (self.settings.screen_center_x, 180)

        # Play
        play_image = pg.image.load("data/img/play.png")
        self.play_sound = pg.mixer.Sound("data/sound/play.ogg") # TODO: remove self
        self.play_button = Sprite(play_image)
        self.play_button.scale(10)
        self.play_button.rect.center = (self.settings.screen_center_x, 600)

        self.world = World(self)

    def run(self):
        while True:
            self.state_manager.think()
            
            # self._handle_events()
            # dt = self.clock.tick_busy_loop(60)
            # self.title.update(dt)
            # self.world.update(dt)
            # # print(f"{self.flying_arrows}\r", end="")
            # self.cursor_rect.topleft = pg.mouse.get_pos()
            # self._update_screen()

    def close(self):
        pg.quit()
        sys.exit()


if __name__ == "__main__":
    arena = Arena()
    arena.run()