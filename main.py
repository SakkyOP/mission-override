import arcade
from player import Player 
from constants import *

class MyGame(arcade.Window):
    
    def __init__(self):
        
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        self.player_list = None
        
        self.player = None
    
    def setup(self):
        self.player_list = arcade.SpriteList()
        
        self.player = Player()
        
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        
        self.player_list.append(self.player)
        
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        
    
    def on_draw(self):
        
        self.clear();
        
        self.player_list.draw()
        
    def on_key_press(self, key, modifier):
        
        if key in [arcade.key.UP, arcade.key.W]:
            self.player.state = 2 # switch to walking state
            
            self.player.change_y = MOVEMENT_SPEED
        elif key in [arcade.key.DOWN, arcade.key.S]:
            self.player.state = 1 # switch to walking state
            
            self.player.change_y = -MOVEMENT_SPEED
        elif key in [arcade.key.LEFT, arcade.key.A]:
            self.player.state = 1 # switch to walking state
            
            self.player.change_x = -MOVEMENT_SPEED
        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.player.state = 1 # switch to walking state
            
            self.player.change_x = MOVEMENT_SPEED
    
    def on_key_release(self, symbol: int, modifiers: int):
        
        self.player.state = 0
        
        if symbol in [arcade.key.UP, arcade.key.DOWN, arcade.key.W, arcade.key.S]:
            self.player.change_y = 0
        
        elif symbol in [arcade.key.LEFT, arcade.key.RIGHT, arcade.key.A, arcade.key.D]:
            self.player.change_x = 0
        
    
    def on_update(self, delta_time: float):
        
        self.player_list.update()
        
        self.player_list.update_animation()
        
    

def main():
    window = MyGame()
    window.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()