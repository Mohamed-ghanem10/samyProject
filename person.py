class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate  # percentage (0–100)

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50
        else:
            self.healthRate = 0

    def buy(self, items):
        total_cost = items * 10
        if self.money >= total_cost:
            self.money -= total_cost
            print(f"{self.name} bought {items} item(s). Remaining money: {self.money} L.E")
        else:
            print(f"{self.name} does not have enough money to buy {items} item(s).")
