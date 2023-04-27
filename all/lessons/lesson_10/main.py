# class Throoper:
#     # def __int__(self): #инициализация (magic)
#     #     x = 5
#     #
#     def __lorem(self):  #приватный метод
#         print("0karl")
#     def hi(self): #публичный метод
#         print("2u")
#         self.__lorem()
# df = Throoper()
# df.hi()
#                             GAME

import playsound
from random import choice


class Musicbox:
    def __init__(self):
        self.__variants = "sg"
        self.__sequence = choice(self.__variants)
        print(self.__sequence)

    def play(self):
        for letter in self.__sequence:
            playsound.playsound(f"sounds/{letter}.mp3")

    def next(self):
        self.__sequence += choice(self.__variants)

    def check(self, guess):
        if guess == self.__sequence:
            playsound.playsound("sounds/emd.mp3")
        else:  # не угадали нигадяи
            playsound.playsound("sounds/emd.mp3")


player = Musicbox()
player.play()
answer = input("what do u heard???").lower()
# .lower() - низкие буквы
player.check(answer)
player.next()
player.play()

# playsound.playsound("sounds/d.mp3")


#
#
# super - наследование
# магический
# метод - полиморфизм
