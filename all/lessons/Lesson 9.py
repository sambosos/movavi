#
# class Dude: #создание класса (шаблон)
#
#     def __init__(self): # магичисекий метод инициализации
#        self.height = 190 #атрибут/поле
#     def __str__(self): #поведение при переводе в строку
#         return f"Здрасьте , Антон)) {self.height}
#     def check(self): #публичный метод
#         print('j')
#         print(self.__loooot())# вызов приватного из публичного
#     def __loooot(self): #приватный метод
#         return 'j'
#
# obj = Dude() # инициализация (создание обьекта на основе класса)
# print(obj.height+9)
# print(obj)
class Dude:
    def __int__(self):
        self.height = 190

    def __init__(self):  # магичисекий метод инициализации
         self.__money = 1000000
    def job(self):
        self.__money+=20000
    def getmoney(self):
        return self.__money

a = Dude()
print(a.getmoney())
a.job()
a.job()
a.job()
print(a.getmoney())