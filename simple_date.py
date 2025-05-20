class SimpleDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
    def __gt__(self, other):
        if self.year > other.year:
            return True
        elif self.year == other.year:
            if self.month > other.month:
                return True
            elif self.month == other.month:
                if self.day > other.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day > other.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    def __eq__(self, other):
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.year != other.year or self.month != other.month or self.day != other.day:
            return True
        else:
            return False
d1 = SimpleDate(4, 10, 2020)
d2 = SimpleDate(28, 12, 1985)
d3 = SimpleDate(28, 12, 1985)

print(d1)
print(d2)
print(d1 == d2)
print(d1 != d2)
print(d1 == d3)
print(d1 < d2)
print(d1 > d2)

