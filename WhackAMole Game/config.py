# config.py

import pygame
pygame.init()

# -----------------------------------
#  Game Settings
# -----------------------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
GAME_LENGTH = 30
TITLE = "Whack-a-Mole"

GAME_TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(GAME_TIMER, 1000)

SCORE_GOAL = 100
POINTS_AWARD = 10

BACKGROUND_IMAGE = "assets/images/bkgd2.png"
FONT_NAME = ""
FONT_SIZE_LARGE = 64
FONT_SIZE_MEDIUM = 36
FONT_SIZE_SMALL = 24

# -----------------------------------
# color
# -----------------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
LEAF_GREEN = (117, 204, 3)

# -----------------------------------
#  Hammer Settings
# -----------------------------------
HAMMER_SPEED = 5
HAMMER_IMAGE = "assets/images/hammer.png"
HAMMER_IMAGE_HIT = "assets/images/hammer_smash.png"
HAMMER_SOUND_HIT = "assets/sounds/wooden-thud-mono-6244.mp3"
HAMMER_SOUND_MISS = "assets/sounds/whoosh-motion-243505.mp3"

# -----------------------------------
#  Mole Settings
# -----------------------------------
MOLE_SPRITES = "assets/images/mole1.png"
MOLE_SPRITES_OW = "assets/images/mole1_smash.png"
MOLE_SPAWN_SOUND = "assets/sounds/bubble-pop-5-323639.mp3"
MOLE_WIDTH = 100
MOLE_HEIGHT = 100

