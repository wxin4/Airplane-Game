import os

# 项目的根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 静态文件的目录
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

# 背景图片
BG_IMG = os.path.join(ASSETS_DIR, 'image/background.png')

# 标题图片
IMG_GAME_TITLE = os.path.join(ASSETS_DIR, 'image/game_title.png')

# 开始游戏的按钮
IMG_GAME_START_BTN = os.path.join(ASSETS_DIR, 'image/game_start.png')

# 背景音乐
BG_MUSIC= os.path.join(ASSETS_DIR, 'sound/game_bg_music.wav')

# 我方飞机的静态资源
OUR_PLANE_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'image/hero1.png'),
    os.path.join(ASSETS_DIR, 'image/hero2.png')
]

# 子弹图片和发射声音
BULLET_IMG = os.path.join(ASSETS_DIR, 'image/bullet1.png')
BULLET_SHOOT_SOUND = os.path.join(ASSETS_DIR, 'sound/bullet.wav')