class Base1:
    def __init__(self):
        print("Base1 初始化")

class Base2:
    def __init__(self):
        print("Base2 初始化")

class Derived(Base1, Base2):
    def __init__(self):
        print("在 Derived 中调用 super() 之前")
        super().__init__()  # 调用 Base1 的 __init__()
        print("在 Base1 的 __init__() 之后")

# 创建 Derived 类的实例
d = Derived()
print(Derived.__mro__)