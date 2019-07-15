import sys, pygame

# 初始化pygame
pygame.init()

# 屏幕对象
screen = pygame.display.set_mode((500, 500))

# 加载图片
hero1 = pygame.image.load('./media/hero1.png')
hero2 = pygame.image.load('./media/hero2.png')

# 帧速率
clock = pygame.time.Clock()
count = 0

# 游戏主循环
while 1:
    count += 1
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 绘制白色屏幕以及主飞机
    screen.fill(pygame.Color(255, 255, 255))

    # 帧速率控制每秒钟执行
    clock.tick(60)
    if count % 5 == 0:
        screen.blit(hero1, (20, 20))
    else:
        screen.blit(hero2, (20, 20))

    pygame.display.flip()