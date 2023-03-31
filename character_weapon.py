from sprite_obj import *

class Weapon(Animated_sprite):
    def __init__(self, game, path='resources/sprites/weapon/shotgun/weapon_firing_1.png', scale=0.4, animation_time=90):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pg.transform.smoothscale(current_image, (self.image.get_width() * scale, self.image.get_height() * scale))
             for current_image in self.images])
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
        pass
