import sys, pygame
import constants
from game.plane import OurPlane, SmallEnemyPlane

# 游戏入口
from game.war import PlaneWar


def main():
    war = PlaneWar()
    # 添加小型敌方飞机
    war.add_small_enemies(6)
    war.run_game()


if __name__ == '__main__':
    main()