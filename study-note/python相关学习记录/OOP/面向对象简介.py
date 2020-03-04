# -*- coding: utf-8 -*-

import random
import time
#定义类
#python2  写法,object是所有类的副类，python3中是默认值
class Orr(object):
    pass
#魔术方法是给解释器用的。
#python3
class Orc:
    #类属性
    skin = 'green'
    #实例属性
    def __init__(self,name,HP,ACT):#初始化，生成实例
        self.name=name
        self.HP=HP
        self.ACT=ACT
        self.wupin=['1sadsa','2sadsad','3sadasd','4sadsa']
        self.f = False#标记位
        self.skill=['1','2','3']
    #类中的函数叫类的方法
    def death(self):
        return self.wupin[random.randint(0,3)]
    def check_f(self):
        if self.HP<3:
            self.f = True
            self.into_f()
    def into_f(self):
        self.skill.append('5')
        self.skill.append('4')

class Aorc(Orc):
    def sep(self):
        return '特殊'

orc3 = Aorc('wwwdd',135,135)
print(orc3.sep())
#
orc1 = Orc('ss',5,5)
orc2 = Orc('dd',15,15)
print(orc1.skin+'   '+str(orc1.ACT)+' '+str(orc1.HP))
print(orc2.skin+'   '+str(orc2.ACT)+' '+str(orc2.HP))
#
orc2.HP = orc2.HP - 10
print(orc2.HP)
#
print(orc2.death())
#
print(f'我去{orc2.name}，宝贝{orc2.death()}')
#
#
for i in range(1,10):
    time.sleep(1)
    print(orc2.HP)
    orc2.HP = orc2.HP -1
    orc2.check_f()
    print(orc2.skill)





# class dog:
#     def __init__(self,age,name):
#         self.age=age
#         self.name=name
#
#
# dog1 = dog(2,'nbon')
# dog2 = dog(6,'nboskjdba')
# dog3 = dog(5,'nbonkjsah')

