class LotteryNumbers:
    def __init__(self, week: int, numbers: list):
        self.week = week
        self.numbers = numbers
    def number_of_hits(self, numbers: list):
        return len([n for n in numbers if n in self.numbers])
    def hits_in_place(self, numbers: list):
        return [n if n in self.numbers else -1 for n in numbers]
week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
my_numbers = [1,4,7,10,11,20,30]

print(week8.hits_in_place(my_numbers))
