class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
    def __str__(self):
        total = self.__euros * 100 + self.__cents
        return f"{(total / 100):.2f} eur"
    def __eq__(self, other):
        if self.__euros == other.__euros and self.__cents == other.__cents:
            return True
        else:
            return False
    def __lt__(self, other):
        if (self.__euros * 100 + self.__cents <
                other.__euros * 100 + other.__cents):
            return True
        else:
            return False
    def __gt__(self, other):
        if (self.__euros * 100 + self.__cents >
                other.__euros * 100 + other.__cents):
            return True
        else:
            return False
    def __ne__(self, other):
        if (self.__euros * 100 + self.__cents !=
                other.__euros * 100 + other.__cents):
            return True
        else:
            return False
    def __add__(self, other):
        total_euros = self.__euros + other.__euros
        if self.__cents + other.__cents > 100:
            total_cents = self.__cents + other.__cents - 100
            total_euros += 1
        else:
            total_cents = self.__cents + other.__cents
        return Money(total_euros, total_cents)
    def __sub__(self, other):
        total_euros = self.__euros - other.__euros
        if total_euros < 0:
            raise ValueError("Negative euros")
        total_cents = self.__cents - other.__cents
        if total_cents < 0:
            total_cents = total_cents + 100
            total_euros -= 1
        return Money(total_euros, total_cents)

if __name__ == "__main__":
    e1 = Money(4, 5)
    print(e1)
    e1.euros = 1000
    print(e1)