'''飞机的基类'''
import random

import pygame
import constants
from game.bullet import Bullet


class Plane(pygame.sprite.Sprite):
    '''
    飞机的基类
    '''
    # 飞机的图片
    plane_images = []
    # 飞机状态: True 表示活的, False 表示死了
    active = True
    # 该飞机发射子弹精灵组
    bullets = pygame.sprite.Group()

    def __init__(self, screen, speed=None):
        super().__init__()
        self.screen = screen
        # 加载静态资源
        self.img_list = []
        self.load_src()

        # 飞机飞行速度
        self.speed = speed or 10

        # 飞机的位置
        self.rect = self.img_list[0].get_rect()

        # 飞机的高度和宽度
        self.plane_w, self.plane_h = self.img_list[0].get_size()

        # 游戏窗口的宽度和高度
        self.width, self.height = self.screen.get_size()

        # 改变飞机的初始化位置, 放在屏幕的下方
        self.rect.left = int((self.width - self.plane_w) / 2)
        self.rect.top = int(self.height / 2)

    def load_src(self):
        for img in self.plane_images:
            self.img_list.append(pygame.image.load(img))

    @property
    def image(self):
        return self.img_list[0]

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def move_up(self):
        '''飞机向上移动'''
        self.rect.top -= self.speed

    def move_down(self):
        '''飞机向下移动'''
        self.rect.top += self.speed

    def move_left(self):
        '''飞机向左移动'''
        self.rect.left -= self.speed

    def move_right(self):
        '''飞机向右移动'''
        self.rect.left += self.speed

    def shoot(self):
        '''飞机发射子弹'''
        bullet = Bullet(self.screen, self, 20)
        self.bullets.add(bullet)


class OurPlane(Plane):
    '''我方的飞机'''
    # 保存飞机的图片
    plane_images = constants.OUR_PLANE_IMG_LIST

    def update(self, frame):
        '''更新动画效果'''
        # 1. 切换飞机的动画效果, 喷气式效果
        if frame % 5:
            self.screen.blit(self.img_list[0], self.rect)
        else:
            self.screen.blit(self.img_list[1], self.rect)

    def move(self, key):
        '''飞机移动自动控制'''
        if key == pygame.K_w or key == pygame.K_UP:
            self.move_up()
        elif key == pygame.K_s or key == pygame.K_DOWN:
            self.move_down()
        elif key == pygame.K_a or key == pygame.K_LEFT:
            self.move_left()
        elif key == pygame.K_d or key == pygame.K_RIGHT:
            self.move_right()

    def move_up(self):
        '''向上移动超出范围之后拉回来'''
        super().move_up()
        if self.rect.top <= 0:
            self.rect.top = 0

    def move_down(self):
        '''向上移动超出范围之后拉回来'''
        super().move_down()
        if self.rect.top >= self.height - self.plane_h:
            self.rect.top = self.height - self.plane_h

    def move_left(self):
        '''向上移动超出范围之后拉回来'''
        super().move_left()
        if self.rect.left <= 0:
            self.rect.left = 0

    def move_right(self):
        '''向上移动超出范围之后拉回来'''
        super().move_right()
        if self.rect.left >= self.width - self.plane_w:
            self.rect.left = self.width - self.plane_w