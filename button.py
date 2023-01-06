from pygame import draw


class Button:

    def __init__(self, game_instance, bg_color, rect=(200, 150, 0, 0)):
        self.game_instance = game_instance
        self.bg_color = bg_color
        self.rect = rect
        
    def update(self):
        pass

    def draw(self, surface):
        draw.rect(surface, self.bg_color, self.rect)


class TextButton(Button):

    def __init__(self, game_instance, text, color=(255, 255, 255), bg_color=(24, 234, 23), rect=(200, 150, 0, 0)):
        super().__init__(game_instance, bg_color, rect)
        self.text = text
        self.color = color
        self.bg_color = bg_color

        self.text_surface = self.game_instance.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = self.rect.center

    def draw(self, surface):
        super().draw(surface)
        surface.blit(self.text_surface, self.text_rect)


# class SpriteButton(Button, Sprite):
#     pass