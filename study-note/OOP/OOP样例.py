
# 例 01
# 定义一个学生类，用来形容学生
class Student():
    pass
#定义一个对象
mingyue = Student()

#例 02
class PythonStudent():
    #使用None给不确定的值赋值
    name =None
    age =18
    course = "Python"
    #需要注意
    def doHomework(self):
        print("Do homework!")
        #推荐在函数末尾使用return语句
        return None

# yy = PythonStudent()
# print(yy.age)
# print(yy.name)
# yy.doHomework()
# print(PythonStudent.__dict__)

# 例 03
#私有成员访问测试
# class Person():
#     name = "sss"
#     __age = 33
# a = Person()
# print(a.name)
# print(a._Person__age)

# 例 04
#类继承的语法,在python中任何类都有一个父类object
class Person():
    name = "ssss"
    age = 9
    def sleep(self):
        print("Sleeping ..........")
#父类卸载括号里
class Teacher(Person):
    pass
# son = Person()
# tt = Teacher()
# print(son.age,son.name)
# print(tt.name,tt.age)

# 例 05
#子类扩充父类功能的案例
class Persons():
    name = "Na na"
    age = 18
    __score = 0  #私有
    _petname = "sec" #受保护的，子类可以用，但不能公用
    def sleep(self):
        print("sleeping...............")
    def work(self):
        print("make some money")
class Teachers(Persons):
    teacher_id = '9876'
    name = "KKkk"
    def make_tests(self):
        print("attention") 
    def work(self):
        Persons.work(self)  #调用父类的方法
        # super().work()   #和上面的功能相同，调用父类的方法
        self.make_tests()   #调用自己的方法
# ss = Teachers()
# ss.work()

# 例 06
#构造函数的概念
class Dog():
    #__init__就是构造函数
    #每次实例化的时候第一个被调用
    #因为主要工作是进行初始化，所以得名
    def __init__(self):
        print("I am init in dog")
# kk = Dog() #这里会直接打印  I am init in dog

# 例 07 
# 继承中的构造函数 -1
class Animal():
    pass
class PaxingAni(Animal):
    pass
class Dog1(PaxingAni):
    def __init__(self):
        print("I am init in dog")
# kk = Dog() 

# 例 08
# 继承中的构造函数 -2
class Animal1():
    def __init__(self):
        print("I am init in dog  die")
class PaxingAni1(Animal1):
    pass
class Dog11(PaxingAni1):
    pass
# kk = Dog11() 

# 例 09
class AA():
    pass
class BB(AA):
    pass
# 返回类的继承元组
# print(BB.__mro__)

# 例 10
#构造函数例子
class Person3():
    #确定一些属性的值
    def __init__(self):
        self.name = "NoName"
        self.age = 18
        self.address ="Student street"
        print("In init func")
# p = Person3()

# 例 11
# 扩展父类中的构造函数
class AAAA():
    def __init__(self):
        print("A")
class BBBB(AAAA):
    def __init__(self,name):
        print("B")
        print(name)
class CCCC(BBBB):
    # c中想扩展B的构造函数，记调用B的构造函数后再添加一些功能
    #有两种方法实现
    #第一种是通过父类名调用
    def __init__(self,name):
        BBBB.__init__(self,name)
        print("这是C中附加的功能")

# 例 12
# 属性案例
#创建Student类，描述学生类
#学生具有Student.name属性
#但name格式并不同意
class Student333():
    def __init__(self,name,age):
        self.name =name
        self.age = age
        #介绍下自己
    def intro(self):
        print(f"Hai ,my name is {self.name}")
# s1 = Student333("Yaaa",12)
# s2 = Student333("ffff",32)

# s1.intro()
# s2.intro()

# 例 13
#peroperty案例
#定义一个Person类，具有name，ahe属性
#对于任意输入的姓名，我们希望都用大写的方式保存
#年龄，我们希望内部统一用整数保存
# x = property(fget,fset,fdel,doc)
class Person55():
    #函数名称任意
    def fget(self):
        return self._name * 2
    def fset(self,name):
        #所有输入以大写形式保存
        self._name = name.upper()
    def fdel(self):
        self._name = "NoName"
    name = property(fget,fset,fdel,"对name输入进行处理")
# pp = Person55()
# pp.name = "xxx"
# print(pp.name)
#----------------------------
#下面这么写也能实现同样功能。区别？
class Student3334():
    '''
    说明
    '''
    def __init__(self,name,age):
        self.name =name.upper()
        self.age = int(age)
# dd = Student3334("sss",78.8)
# print(dd.name)
# print(dd.age)
# print(Student3334.__mro__)  
# print(Student3334.__bases__)

# 例 14
#类和对象三种方法的案例
class Person8:
    #实例方法
    def eat(self):
        print(self)
        print("Eatting .....")
    #类方法
    #类方法的第一个参数，一般命名为cls，区别于self
    @classmethod
    def paly(cls):
        print(cls)
        print("playing...")
    #静态方法
    #不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print("Saying.....")
# dddd = Person8()
# #实例方法
# dddd.eat()
# #类方法
# Person8.paly()
# dddd.paly()
# #静态方法
# Person8.say()
# dddd.say()

# 例 15
#变量的三种用法
class SSS():
    def __init__(self):
        self.name = "hah"
        self.age = 18
a = SSS()
#属性的三种用法
# 1 赋值
# 2 读取
# 3 删除-直接删除该属性
a.name="LLLLL"
print(a.name)
# del a.name
# print(a.name)
