# _*_ coding:utf-8 _*_


# 类中设置属性为私有的处理方式，在属性名称前加上两个下划线即可。
# 现在不能在外部访问__inaccessible，但是在类中使用它。
class Sercrtive:
    def __inaccessible(self):
        print("Bet you can't see me ...")

    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()

# 指定超类
class Filter:
    def init(self):
        self.blocked = []
    def filter(self,sequence):
        return [x for  x  in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']

f = Filter()
f.init()
print(f.filter([1,2,3]))

s = SPAMFilter()
s.init()
print(s.filter(['SPAM','test','SPAM']))

# 深入继承，使用内置方法
## 确定一个类是否是另一个类的子类,issubclass
print(issubclass(SPAMFilter,Filter))
print(issubclass(Filter,SPAMFilter))

## 想知道一个类的基类(父类)，__bases__
print(SPAMFilter.__bases__)
print(Filter.__bases__)

## 确定对象是否是特定类的实例，可使用isinstance
s = SPAMFilter()
print(isinstance(s,SPAMFilter))
print(isinstance(s,Filter))

## 想知道这个对象属于哪个类，__class__
print(s.__class__)

# 检查所需的方法是否存在
print(hasattr(f,'filter'))
print(hasattr(f,'talk'))
print(f.__dict__)
print(s.__dict__)

# 抽象基类，不能实例化对象的类
# @abstractmethod将方法标记为抽象，那样在子类中就必须实现的方法
from abc import ABC
class Talker(ABC):
    @staticmethod
    def talk(slef):
        pass
print(Talker())