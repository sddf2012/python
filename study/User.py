class User:
    def __init__(self,name,age):
        print("初始化user")
        self.name=name
        self.age=age
    
    def __str__(self):
        return f'name:{self.name},age:{self.age}'
    
    def info(self):
        print(self)

class Student(User):
    def __init__(self, name, age,type):
        print("初始化student")
        super().__init__(name, age)
        self.type=type