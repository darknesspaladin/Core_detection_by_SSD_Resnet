from abc import ABCMeta, abstractmethod
from random import randint,randrange

class Fighter(metaclass=ABCMeta):
    '''创建战斗对象'''

    #通过__slots__魔法限定对象可以绑定的成员变量
    __slots__ = ('_name','_hp')

    def __init__(self, name, hp):
        '''
        :param name: ID
        :param hp: 生命值
        '''
        self._name = name
        self._hp = hp
        @property
        def name(self):
            return self._name
        @property
        def hp(self):
            return self._hp
        @hp.setter
        def hp(self):
            self._hp = hp if hp >= 0 else 0
        @property
        def alive(self):
            return self._hp > 0
        @abstractmethod
        def attack(self, other):
            '''攻击
            :param other: 被攻击的对象
            '''
            pass
class Ultraman(Fighter):
    '''奥特曼'''
    __slots__ = ('_name', '_hp', '_mp')
    def __init__(self,name,hp,mp):
        super().__init__(name,hp)
        self._mp = mp

    def attack(self,other):
        other.hp -= randint(15,25)
    def huge_attack(self,other):
        '''究极必杀技(打掉对方至少50点或者四分之三的)
        :param other:被攻击对象
        :return: 成功返回True否则返回False
        '''
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3//4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self,others):
        '''魔法攻击
        :param others: 被攻击的群体
        return:使用魔法成功返回Ture否则返回False
        '''
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10,15)
            return True
        else:
            return False
    def resume(self):
        '''恢复魔法值'''
        incr_point = randint(1,100)
        self._mp += incr_point
        return incr_point
    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp

    class Monster(Fighter):
        '''小怪兽'''
        __slots__ = ('_name', '_hp')
        def attack(self,other):
            other.hp -= randint(10,20)
        def __str__(self):
            return '~~~%s小怪兽~~~\n' % self._name + \
                '生命值'


