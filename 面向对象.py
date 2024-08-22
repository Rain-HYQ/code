# 类  对象
# 创建类
# 面向对象的特点：  封装  继承   多态   重写

class Animal(object):   #定义类
    def __init__(self,name,age) -> None:
        self.__name = name # 私有属性
        self.age = age # 公有属性
    
    def eat(self):   # 公有方法
        print('动物正在吃饭')

    def run(self):
        print('正在跑')

class Cat(Animal):  # 继承


    def __init__(self, name, age) -> None:   #  初始化方法
        self.name = name
        self.age = age
        print('初始化方法正在被调用')


    def __eat(self):   #  私有方法
        print(f'{self.__name}正在吃鱼。。。')
        
    def runing(self):
        self.__eat()
    
    
    def eat(self,safe):
        print(f'{self.name}正在吃饭，吃完饭之后说，我们{safe}')


# 创建对象
tom = Cat('汤姆',3)
# print(tom.__name)
# tom.runing()
tom.eat(safe='出去玩')

