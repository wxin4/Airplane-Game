import sys, pygame
import constants
from game.plane import OurPlane

# 游戏入口
def main():
    # 初始化
    pygame.init()

    # 屏幕对象
    width, height = 480, 852
    screen = pygame.display.set_mode((width, height))
    # 设置标题
    pygame.display.set_caption('飞机大战')

    # 加载背景图片
    bg = pygame.image.load(constants.BG_IMG)
    img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)
    img_game_title_rect = img_game_title.get_rect()
    # 宽度和高度
    t_width, t_height = img_game_title.get_size()
    img_game_title_rect.topleft = (int((width - t_width)/2),int(height / 2 - t_height))

    # 开始按钮
    btn_start = pygame.image.load(constants.IMG_GAME_START_BTN)
    btn_start_rect = btn_start.get_rect()
    btn_width, btn_height = btn_start.get_size()
    btn_start_rect.topleft = (int((width - btn_width) / 2), int(height / 2 + btn_height))

    # 加载背景音乐
    pygame.mixer.music.load(constants.BG_MUSIC)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

    # 游戏状态
    status = 0 # 准备中, 游戏中, 游戏结束

    our_plane = OurPlane(screen, speed=20)

    # 播放帧数
    frame = 0
    # 帧速率
    clock = pygame.time.Clock()

    while True:
        # 设置帧速率
        clock.tick(60)
        frame += 1
        if frame >= 60:
            frame = 0

        # 1. 监听事件
        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 鼠标点击进入游戏
                # 游戏正在准备中, 点击才能进入游戏
                if status == 0:
                    status = 1
            elif event.type == pygame.KEYDOWN:
                # 键盘事件
                # 游戏正在游戏中才需要控制键盘: ASWD
                if status == 1:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        our_plane.move_up()
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        our_plane.move_down()
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        our_plane.move_left()
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        our_plane.move_right()
                    # 发射子弹
                    elif event.key == pygame.K_SPACE:
                        our_plane.shoot()


        # 2. 更新游戏的状态
        if status == 0:
            # 游戏正在准备中
            # 绘制背景
            screen.blit(bg, bg.get_rect())
            # 绘制标题
            screen.blit(img_game_title, img_game_title_rect)
            # 绘制开始按钮
            screen.blit(btn_start, btn_start_rect)
        elif status == 1:
            # 游戏进行中
            # 绘制背景
            screen.blit(bg, bg.get_rect())
            # 绘制飞机
            our_plane.update(frame)
            # 绘制子弹
            our_plane.bullets.update()

        pygame.display.flip()

if __name__ == '__main__':
    main()