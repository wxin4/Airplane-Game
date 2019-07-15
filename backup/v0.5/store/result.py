

class PlayResult(object):
    '''玩家结果统计'''
    __score = 0  # 总分
    __life = 3  # 生命数量
    __blood = 1000  # 生命值

    @property
    def score(self):
        '''单次游戏分数'''
        return self.__score

    @score.setter
    def score(self, value):
        '''设置游戏分数'''
        if value < 0:
            return None
        self.__score = value