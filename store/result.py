import constants


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

    def set_history(self):
        '''记录最高分'''
        # 1. 读取文件中的存储的分数
        # 2. 如果新的分数比文件的大, 则进行存储, 如果小, 不作处理
        # 3. 存储分数不是追加的模式a+, 而是替换的模式w
        if int(self.get_max_score()) < self.score:
            with open(constants.PLAY_RESULT_STORE_FILE, 'w') as f:
                f.write('{0}'.format(self.score))

    def get_max_score(self):
        '''读取文件中的最高分'''
        rest = 0
        with open(constants.PLAY_RESULT_STORE_FILE, 'r') as f:
            r = f.read()
            if r:
                rest = r
        return rest
