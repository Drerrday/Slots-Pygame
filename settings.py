# Display settings
DEFAULT_IMAGE_SIZE = (300, 300)
FPS = 120
HEIGHT = 1000
WIDTH = 1600
START_X, START_Y = 0, -300
X_OFFSET, Y_OFFSET = 20, 0

# Images
BG_IMAGE_PATH = 'graphics/images/bg.png'
GRID_IMAGE_PATH = 'graphics/images/gridline.png'
GAME_INDICES = [1, 2, 3] # 0 and 4 are outside of play area
SYM_PATH = 'graphics/images/symbols'
MUTED_BUTTON_IMAGE_PATH = 'graphics/images/sound_off.png'
UNMUTED_BUTTON_IMAGE_PATH = 'graphics/images/sound_on.png'

# Text
TEXT_COLOR = 'Cyan'
UI_FONT = 'graphics/font/ComicSansMS3.ttf'
UI_FONT_SIZE = 30
WIN_FONT_SIZE = 110

# 5 Symbols for a harder game
# symbols = {
#     'diamond': f"{SYM_PATH}/0_diamond.png", 
#     'floppy': f"{SYM_PATH}/0_floppy.png",
#     'hourglass': f"{SYM_PATH}/0_hourglass.png",
#     'seven': f"{SYM_PATH}/0_seven.png",
#     'telephone': f"{SYM_PATH}/0_telephone.png"
# }

# 4 Symbols for more wins
symbols = {
    'diamond': f"{SYM_PATH}/0_diamond.png", 
    'floppy': f"{SYM_PATH}/0_floppy.png",
    'hourglass': f"{SYM_PATH}/0_hourglass.png",
    'hourglass2': f"{SYM_PATH}/0_hourglass.png",
    'telephone': f"{SYM_PATH}/0_telephone.png"
}