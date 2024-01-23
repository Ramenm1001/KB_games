x = ()
print(type(x))

class A:
    def __init__(self):
        self.x = 5 # свойства, поля,
        # аттрибуты, переменные класса
        # self.x123 = 123

def new_feature():
    print("hello")

a1 = A()
setattr(a1, "x123", 123)
print(a1.x123)

lst = [11, 22, 33, 44, 55]
#      0   1   2   3   4
# 12345
print(lst)

# !Здесь был WaffleQue! >:)