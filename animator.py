from pygame import transform


class Animator:

    def __init__(self, game_object):
        self.game_object = game_object
        self.total_images = len(self.game_object.images)
        self.image_time = 400
        self.current_time = 0
        self.current_image_index = 0

    def update(self, dt):
        self.current_time += dt
        if self.current_time > self.image_time:
            self.current_image_index = (self.current_image_index + 1) % self.total_images
            self.game_object.image = self.game_object.images[self.current_image_index]
            if not self.game_object.is_looking_right:
                self.game_object.image = transform.flip(self.game_object.image, True, False)
            self.current_time = 0
