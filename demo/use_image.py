import sys, pygame

# 初始化pygame
pygame.init()

# 屏幕对象
screen = pygame.display.set_mode((500, 500))

# 加载图片
ball = pygame.image.load('/Users/xinwei/PycharmProjects/python/Step4/AirplaneGame/demo/media/intro_ball.gif')

# 红色
red = pygame.Color(255, 0, 0)

# 游戏主循环
while 1:

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 更新状态
    # 画线
    pygame.draw.line(screen, red, (10, 10), (200, 200), 10)
    # 绘制
    screen.blit(ball, (100, 100))
    pygame.display.flip()