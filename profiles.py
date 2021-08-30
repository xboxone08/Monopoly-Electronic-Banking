class Profile:
    def __init__(self, starting_money=1500):
        self.money = starting_money

    def add(self, money: int):
        self.money += money

    def subtract(self, money: int):
        self.money -= money

    def pay(self, player, money: int):
        self.money -= money
        player.money += money

    def salary(self):
        self.add(2)
