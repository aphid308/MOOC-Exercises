

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def eat_lunch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60
        else:
            pass

    def eat_special(self):
        if self.balance >= 4.60:
            self.balance -= 4.60
        else:
            pass

    def deposit_money(self, deposit_amount: float):
        """
        :type deposit_amount: float
        """
        if deposit_amount > 0:
            self.balance += deposit_amount
        else:
            raise ValueError("You cannot deposit an amount of money less than zero")

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

if __name__ == "__main__":
    peter_card = LunchCard(20)
    grace_card = LunchCard(30)
    peter_card.eat_special()
    grace_card.eat_lunch()
    print(f"Peter: {peter_card}")
    print(f"Grace: {grace_card}")
    peter_card.deposit_money(20)
    grace_card.eat_special()
    print(f"Peter: {peter_card}")
    print(f"Grace: {grace_card}")
    peter_card.eat_lunch()
    peter_card.eat_lunch()
    grace_card.deposit_money(50)
    print(f"Peter: {peter_card}")
    print(f"Grace: {grace_card}")