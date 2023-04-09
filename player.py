import arcade
import sprites
from constants import *

class Player(arcade.Sprite):

    # ============ Player Constants ===============
    RIGHT = 0
    LEFT = 1
    
    PLAYER_STATES = {
        "IDLE" : 0,
        "WALK" : 1,
        "JUMP" : 2,
        "DEATH" : 3
    }

    def __init__(self):
        
        super().__init__()
        
        self.scale = CHARACTER_SCALING
        
        self.character_face_direction = self.RIGHT

        self.idle_texture = sprites.process_sprite(sprites.PLAYER_IDLE[0], sprites.PLAYER_IDLE[1])
        self.walk_texture = sprites.process_sprite(sprites.PLAYER_RUN[0], sprites.PLAYER_RUN[1])
        self.jump_texture = sprites.process_sprite(sprites.PLAYER_JUMP[0], sprites.PLAYER_JUMP[1])
        self.death_texture = sprites.process_sprite(sprites.PLAYER_DEATH[0], sprites.PLAYER_DEATH[1])
        
        self.point = [
            [-3,-8],
            [4, -8],
            [-3, 8],
            [4,8]
        ]
        
        self.state = 0 # IDLE State
        
        self.cur_texture = 0
        
    def update_animation(self, delta_time: float = 1/60):
        
        if self.change_x < 0 and self.character_face_direction == self.RIGHT:
            self.character_face_direction = self.LEFT
        elif self.change_x > 0 and self.character_face_direction == self.LEFT:
            self.character_face_direction = self.RIGHT
        
        # Idle Animation
        if self.state == self.PLAYER_STATES["IDLE"]:
            self.cur_texture += 1
            if self.cur_texture > 5 * UPDATES_PER_FRAME:  # 5 -> (n-1) - n is the max no. of frames for the animation
                self.cur_texture = 0
            frame = self.cur_texture // UPDATES_PER_FRAME
            self.texture = self.idle_texture[frame][self.character_face_direction]
            return
        
        # Walking Animation
        if self.state == self.PLAYER_STATES["WALK"]:
            self.cur_texture += 1
            if self.cur_texture > 5 * UPDATES_PER_FRAME:  # 5 -> (n-1) - n is the max no. of frames for the animation
                self.cur_texture = 0
            frame = self.cur_texture // UPDATES_PER_FRAME
            self.texture = self.walk_texture[frame][self.character_face_direction]
            return
        
        # Jumping Animation
        if self.state == self.PLAYER_STATES["JUMP"]:
            self.cur_texture += self.change_y // 5
            if self.cur_texture > 4 * UPDATES_PER_FRAME:  # 5 -> (n-1) - n is the max no. of frames for the animation
                self.cur_texture = 0
            frame = self.cur_texture // UPDATES_PER_FRAME
            self.texture = self.jump_texture[frame][self.character_face_direction]
            return
        
        # Death Animation
        if self.state == self.PLAYER_STATES["DEATH"]:
            print("death")
        