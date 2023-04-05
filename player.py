import arcade
import sprites
from constants import *


class Player(arcade.Sprite):

    # ============ Player Constants ===============
    RIGHT = 0
    LEFT = 1

    def __init__(self):

        super().__init__(self)

        self.idle_texture = sprites.process_sprite(sprites.PLAYER_IDLE[0], sprites.PLAYER_IDLE[0], CHARACTER_SCALING)
        self.walk_texture = sprites.process_sprite(sprites.PLAYER_RUN[0], sprites.PLAYER_RUN[1], CHARACTER_SCALING)
        self.jump_texture = sprites.process_sprite(sprites.PLAYER_JUMP[0], sprites.PLAYER_JUMP[1], CHARACTER_SCALING)
        self.death_texture = sprites.process_sprite(sprites.PLAYER_DEATH[0], sprites.PLAYER_DEATH[1], CHARACTER_SCALING)
        
        self.point = [
            [-3,-8],
            [4, -8],
            [-3, 8],
            [4,8]
        ]
        
        