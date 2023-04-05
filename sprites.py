import arcade
from PIL import Image
from constants import *

"""

Instead of returning a SpriteList just return a texture pair list which contains a list of pair of texture and inverted texture for LEFT and RIGHT movement

"""

def process_sprite(path: str, dims: list[tuple[int, int, int, int]], scaling: float):
    texture_list: list[list[arcade.Texture]] = []

    for dim in dims:
        
        texture_list.append([
            arcade.load_texture(path, dim[0], dim[1], dim[2], dim[3]),
            arcade.load_texture(path, dim[0], dim[1], dim[2], dim[3], flipped_horizontally=True)
        ])
        
    return texture_list


# ================== PLAYER SPRITES ====================

PLAYER_IDLE = [
    ".\\assets\\spritesheets\\player\\Astronaut_Idle.png",
    [(x, 0, 24, 24) for x in range(0, 121, 24)]
]

PLAYER_RUN = [
    ".\\assets\\spritesheets\\player\\Astronaut_Run.png",
    [(x, 0, 24, 24) for x in range(0, 121, 24)]
]

PLAYER_JUMP = [
    ".\\assets\\spritesheets\\player\\Astronaut_Jump.png",
    [(x, 0, 24, 24) for x in range(0, 121, 24)]
]

PLAYER_DEATH = [
    ".\\assets\\spritesheets\\player\\Astronaut_Death.png",
    [(x, 0, 24, 24) for x in range(0, 121, 24)]
]

# =================== ENEMY BOTS ========================

BOT_IDLE = [
    ".\\assets\\spritesheets\\enemies\\bot\\static idle.png",
    [(10, 2, 24, 24),]
]

BOT_WAKE = [
    ".\\assets\\spritesheets\\enemies\\bot\\wake.png",
    [(10, 2, 26, 24),
    (10, 27, 26, 24),
    (10, 54, 26, 24),
    (10, 80, 26, 24),
    (10, 106, 26, 24)]
]

BOT_SHOOT = [
    ".\\assets\\spritesheets\\enemies\\bot\\shoot with FX.png",
    [(14, y, 36, 24) for y in range(2, 81, 26)]
]

BOT_MOVE = [
    ".\\assets\\spritesheets\\enemies\\bot\\move with FX.png",
    [(10, y, 26, 26) for y in range(0, 183, 26)]
]

BOT_DASH = [
    ".\\assets\\spritesheets\\enemies\\bot\\GAS dash with FX.png",
    [(21, y, 96, 23) for y in range(2, (26*6)+3, 26)]
]

BOT_CHARGE = [
    ".\\assets\\spritesheets\\enemies\\bot\\charge.png",
    [(12, y, 26, 26) for y in range(0, (26*3)+1, 26)]
]

BOT_DAMAGE = [
    ".\\assets\\spritesheets\\enemies\\bot\\damaged.png",
    [(13, 2, 24, 24),
    (13, 28, 24, 24)]
]

BOT_DEATH = [
    ".\\assets\\spritesheets\\enemies\\bot\\death.png",
    [(5, y, 28, 26) for y in range(0, (26*5)+1, 26)]
]

# =================== MINI BOSS GOLEM ========================

GOLEM_IDLE = [
    ".\\assets\\spritesheets\\enemies\\golem\\Character_sheet.png",
    [(x, 21, 52, 52) for x in range(23, (23+300)+1, 100)]
]

GOLEM_MOVE = [
    ".\\assets\\spritesheets\\enemies\\golem\\Character_sheet.png",
    [(x, 121, 52, 52) for x in range(23, (23+700)+1, 100)]
]

GOLEM_SHOOT = [
    ".\\assets\\spritesheets\\enemies\\golem\\Character_sheet.png",
    [(x, 221, 52, 52) for x in range(23, (23+800)+1, 100)]
]

GOLEM_DEACTIVATE = [
    ".\\assets\\spritesheets\\enemies\\golem\\Character_sheet.png",
    [(x, 321, 52, 52) for x in range(23, (23+700)+1, 100)]
]

GOLEM_ACTIVATE = [
    ".\\assets\\spritesheets\\enemies\\golem\\Character_sheet.png",
    [(x, 321, 52, 52) for x in range((23+700), 21, -100)]
]

# if __name__ == '__main__':

#     process_sprite(*GOLEM_ACTIVATE, CHARACTER_SCALING)
