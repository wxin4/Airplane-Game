import pygame
import sys

import constants
from game.plane import OurPlane, SmallEnemyPlane
from store.result import PlayResult


class PlaneWar(object):
    '''飞机大战'''
    # 游戏状态

    READY = 0  # 准备中
    PLAYING = 1  # 游戏中
    OVER = 2  # 游戏结束

    status = READY

    our_plane = None

    # 播放帧数
    frame = 0

    # 帧速率
    clock = pygame.time.Clock()

    # 一架飞机可以属于多个精灵组
    small_enemies = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    # 游戏结果
    rest = PlayResult()

    def __init__(self):
        # 初始化游戏
        pygame.init()
        self.width, self.height = 480, 852

        # 屏幕对象
        self.screen = pygame.display.set_mode((self.width, self.height))
        # 设置标题
        pygame.display.set_caption('飞机大战')

        # 加载背景图片
        self.bg = pygame.image.load(constants.BG_IMG)
        self.bg_over = pygame.image.load(constants.BG_IMG_OVER)

        # 游戏标题
        self.img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)
        self.img_game_title_rect = self.img_game_title.get_rect()

        # 宽度和高度
        t_width, t_height = self.img_game_title.get_size()
        self.img_game_title_rect.topleft = (int((self.width - t_width) / 2), int(self.height / 2 - t_height))

        # 开始按钮
        self.btn_start = pygame.image.load(constants.IMG_GAME_START_BTN)
        self.btn_start_rect = self.btn_start.get_rect()
        btn_width, btn_height = self.btn_start.get_size()
        self.btn_start_rect.topleft = (int((self.width - btn_width) / 2), int(self.height / 2 + btn_height))

        # 游戏文字对象
        self.score_font = pygame.font.SysFont('XinHuaKaiTi-1.ttf', 32)

        # 加载背景音乐
        pygame.mixer.music.load(constants.BG_MUSIC)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

        # 我方飞机对象
        self.our_plane = OurPlane(self.screen, speed=20)

        # 帧速率
        self.clock = pygame.time.Clock()

    def bind_event(self):
        '''绑定事件'''
        # 1. 监听事件
        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 鼠标点击进入游戏
                # 游戏正在准备中, 点击才能进入游戏
                if self.status == self.READY:
                    self.status = self.PLAYING
            elif event.type == pygame.KEYDOWN:
                # 键盘事件
                # 游戏正在游戏中才需要控制键盘: ASWD
                if self.status == self.PLAYING:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.our_plane.move_up()
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.our_plane.move_down()
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.our_plane.move_left()
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.our_plane.move_right()
                    # 发射子弹
                    elif event.key == pygame.K_SPACE:
                        self.our_plane.shoot()

    def add_small_enemies(self, num):
        '''随机添加num架小型敌机'''
        # 随机添加num架小型敌机
        for i in range(num):
            plane = SmallEnemyPlane(self.screen, 8)
            plane.add(self.small_enemies, self.enemies)

    def run_game(self):
        '''游戏主循环'''
        while True:
            # 1. 设置帧速率
            self.clock.tick(60)
            self.frame += 1
            if self.frame >= 60:
                self.frame = 0

            # 2. 绑定事件
            self.bind_event()

            # 3. 更新游戏的状态
            if self.status == self.READY:
                # 游戏正在准备中
                # 绘制背景
                self.screen.blit(self.bg, self.bg.get_rect())
                # 绘制标题
                self.screen.blit(self.img_game_title, self.img_game_title_rect)
                # 绘制开始按钮
                self.screen.blit(self.btn_start, self.btn_start_rect)
            elif self.status == self.PLAYING:
                # 游戏进行中
                # 绘制背景
                self.screen.blit(self.bg, self.bg.get_rect())
                # 绘制飞机
                self.our_plane.update(self)
                # 绘制子弹
                self.our_plane.bullets.update(self)
                # 绘制敌机
                self.small_enemies.update()
                # 游戏分数
                score_text = self.score_font.render('得分: {0}'.format(self.rest.score), False, constants.TEXT_SCORE_COLOR)
                self.screen.blit(score_text, score_text.get_rect())
            elif self.status == self.OVER:
                '''游戏结束'''
                # 游戏背景
                self.screen.blit(self.bg_over, self.bg_over.get_rect())
                # 分数统计
                # 1. 本次总分
                score_text = self.score_font.render('{0}'.format(self.rest.score), False, constants.TEXT_SCORE_COLOR)
                score_text_rect = score_text.get_rect()
                text_w, text_h = score_text.get_size()
                # 改变文字位置
                score_text_rect.topleft = (
                    int((self.width - text_h) / 2),
                    int(self.height / 2)
                )
                self.screen.blit(score_text, score_text_rect)

                # 2. 历史最高分

            pygame.display.flip()
