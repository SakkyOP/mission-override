import arcade
from constants import *

class MyGame(arcade.Window):
    
    def __init__(self):
        
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
    
    def setup(self):
        pass
    
    def on_draw(self):
        
        self.clear();
    

def main():
    window = MyGame()
    window.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()