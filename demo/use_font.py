import sys, pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

# 加载字体
fonts = pygame.font.get_fonts()
print(fonts)

red = pygame.Color(255, 0, 0)

# 不加粗 不斜体
# 方式一: 使用系统默认的字体来加载
# font = pygame.font.SysFont('XinHuaKaiTi-1.ttf', 40, False, False)
# 方式二: 自己准备好ttf字体文件, 放到项目里面
font = pygame.font.Font('./media/XinHuaKaiTi-1.ttf', 40)

# 文字对象
text = font.render('得分', True, red)

# 加载音乐
bg_music = pygame.mixer.music.load('./media/bg_music.ogg')
# 设置音量 (0-1)
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(text, (20, 20))
    pygame.display.flip()
