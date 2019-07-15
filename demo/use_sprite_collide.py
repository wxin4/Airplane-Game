# 1. 引入相关的包
import sys, pygame

# 2. pygame进行初始化
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

# 3. 得到屏幕对象Surface
screen = pygame.display.set_mode(size)

class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height, init_pos):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos

# 实例化精灵对象
sprite_1 = Block(pygame.Color(255, 0, 0), 50, 50, (50, 50))
sprite_2 = Block(pygame.Color(0, 255, 0), 50, 50, (90, 90))


# 4. 游戏主循环
while 1:
    # 处理游戏的事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # 往屏幕上画精灵
    screen.blit(sprite_1.image, sprite_1.rect)
    screen.blit(sprite_2.image, sprite_2.rect)

    # 矩形检测碰撞
    rest = pygame.sprite.collide_rect(sprite_1, sprite_2)
    print('rest', rest)
    # 更精确控制, 链式调用
    rest2 = pygame.sprite.collide_rect_ratio(0.5)(sprite_1, sprite_2)
    print('rest2', rest2)
    pygame.display.flip()