from sprite_obj import *
from npc import *


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc'
        self.static_sprite_path = 'resources/sprites/static_sprites'
        self.animated_sprite_path = 'resources/sprites/animated_sprites'
        add_sprite = self.add_sprite
        add_npc = self.add_npc

        add_sprite(SpriteObject(game))
        add_sprite(Animated_sprite(game))
        add_sprite(Animated_sprite(game, pos=(14.9, 1.1)))
        add_sprite(Animated_sprite(game, pos=(5.9, 4.9)))
        add_sprite(Animated_sprite(game, pos=(5.9, 3.1)))
        add_sprite(Animated_sprite(game, pos=(9.9, 8.9)))
        add_sprite(Animated_sprite(game, pos=(9.9, 10.1)))
        add_sprite(Animated_sprite(game, pos=(11.1, 8.9)))
        add_sprite(Animated_sprite(game, pos=(11.1, 10.1)))
        add_sprite(Animated_sprite(game, path=self.animated_sprite_path
                                              + '/red_candle_animated_sprite/red_candle_sprite_1.png', pos=(1.1, 1.1)))
        add_sprite(Animated_sprite(game, pos=(1.1, 12.9)))
        add_sprite(Animated_sprite(game, pos=(14.9, 1.1)))
        add_sprite(Animated_sprite(game, path=self.animated_sprite_path
                                              + '/red_candle_animated_sprite/red_candle_sprite_1.png', pos=(14.9, 12.9)))

        add_npc(NPC(game))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

