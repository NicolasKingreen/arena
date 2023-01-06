import pygame.sprite
import pygame.transform

from animator import Animator


class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

    def scale(self, ratio):
        if hasattr(self, "images"):
            scaled_images = []
            for image in self.images:
                scaled_image = pygame.transform.scale(image, (image.get_width() * ratio, image.get_height() * ratio))
                scaled_images.append(scaled_image)
            self.images = scaled_images
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * ratio, self.image.get_height() * ratio)) # TODO: set self image as one from scaled ones
        else:
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * ratio, self.image.get_height() * ratio))
        self.rect.width *= ratio
        self.rect.height *= ratio

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class AnimatedSprite(Sprite):

    def __init__(self, images):
        super().__init__(images[0])
        self.is_looking_right = True # TODO: flip player sprite right in the file
        self.images = images
        self.animator = Animator(self)

    def update(self, dt):
        self.animator.update(dt)

    