from __future__ import annotations

starting_money = 1500


class Profile:
    def __init__(self):
        self.money = starting_money

    def add(self, money: int):
        self.money += money

    def subtract(self, money: int):
        self.money -= money

    def pay(self, player: Profile, money: int):
        self.money -= money
        player.money += money

    def salary(self):
        self.add(200)
