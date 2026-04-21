"""The general configuration of the game"""

# settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# game states
STATE_MENU = "menu"
STATE_GAME = "game"

enemy_types = {
    1: "forward",
    2: "warrior",
    3: "tank"
}

images = {
    1: "assets/images/enemy.png",
    2: "assets/images/enemy2.png",
    3: "assets/images/enemy.png"
}
