#Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками. Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.
#Требования:
#1. Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
#2. Игра должна быть реализована как консольное приложение.

import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        # Уменьшаем здоровье другого героя на величину атаки
        other.health -= self.attack_power
        print(f"{self.name} атаковал {other.name} и нанес {self.attack_power} урона.")

    def is_alive(self):
        # Проверяем, жив ли герой (здоровье больше 0)
        return self.health > 0

class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Начало игры!")
        while self.player.is_alive() and self.computer.is_alive():
            # Игрок атакует
            self.player.attack(self.computer)
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")

            # Проверка на живучесть компьютера
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен! {self.player.name} победил!")
                break

            # Компьютер атакует
            self.computer.attack(self.player)
            print(f"У {self.player.name} осталось {self.player.health} здоровья.")

            # Проверка на живучесть игрока
            if not self.player.is_alive():
                print(f"{self.player.name} повержен! {self.computer.name} победил!")
                break

game = Game("Игрок Геркулес")
game.start()